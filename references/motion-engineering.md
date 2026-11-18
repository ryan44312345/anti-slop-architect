# Engenharia de Motion, Smooth Scroll & Performance

Leia este guia **apenas** quando o projeto utilizar rolagem suave (Lenis) ou coreografia JS (GSAP / `ScrollTrigger` / `SplitText` / `Motion`). Em projetos de **Registro Contido** que usam apenas CSS transitions (`180–250ms`), este arquivo não é necessário.

---

## 1. Orçamento de Desempenho (Performance Budget)

Para evitar engasgos (especialmente em mobile intermediário):
- **Propriedades permitidas (GPU-only):** anime exclusivamente `transform` (`x`, `y`, `scale`, `rotate`), `opacity` e `clip-path` pontual. **Proibido** animar `width`, `height`, `top`, `left`, `margin` ou `padding` no scroll.
- **Limite de gatilhos pesados simultâneos:**
  - Máximo **1** seção `[Scroll: Sticky]` com `scrub` por faixa de viewport visível.
  - Máximo **3 a 4** imagens grandes com parallax ativo na página inteira (desative parallax e `scrub` complexo abaixo de `768 px` se não forem essenciais ao padrão).
  - Evite rodar `SplitText` em parágrafos longos — aplique apenas em `H1` e em no máximo `H2`s principais curtos.
- **Tolerância a Falhas de Rede / CDN (Zero Conteúdo Preso Invisível):**
  - **NUNCA** defina `opacity: 0` no CSS base dos elementos esperando o JS revelar.
  - Adicione a classe `.motion-enabled` ao `<html>` **somente depois** de confirmar que `window.gsap` e `window.ScrollTrigger` carregaram e que `prefers-reduced-motion` está desligado — ou use animações `gsap.from(...)` protegidas, garantindo que qualquer falha de CDN deixe 100% da página visível e funcional.

---

## 2. Implementação Blindada para HTML / Tailwind / JS

### Importação (final do `<body>`, versões pinned)
Inclua apenas os scripts que realmente vai usar no projeto:
```html
<script src="https://cdn.jsdelivr.net/npm/lenis@1/dist/lenis.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15/dist/gsap.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15/dist/ScrollTrigger.min.js"></script>
<!-- Inclua SplitText apenas se for animar linhas/palavras de títulos: -->
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15/dist/SplitText.min.js"></script>
```

### Inicialização Segura, Sincronia & Navegação de Âncoras
Resolve: (1) verificação individual de cada plugin; (2) cálculo dinâmico da altura real do `<header>`; (3) `getElementById` seguro sem quebrar em seletores inválidos; (4) `scroll-behavior: auto` enquanto Lenis estiver ativo; (5) cleanup automático em `prefers-reduced-motion`.

```js
(() => {
  const prefersReduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  let lenis = null;

  const getHeaderOffset = () => {
    const header = document.querySelector('header');
    if (!header) return 16;
    const style = window.getComputedStyle(header);
    const isPinned = style.position === 'fixed' || style.position === 'sticky';
    if (!isPinned) return 16;
    const rect = header.getBoundingClientRect();
    return rect.height > 0 ? Math.min(Math.round(rect.height + 16), 140) : 16;
  };

  if (!prefersReduced && window.Lenis) {
    try {
      document.documentElement.style.scrollBehavior = 'auto';
      lenis = new Lenis({ duration: 1.05, smoothWheel: true });

      if (window.gsap && window.ScrollTrigger) {
        gsap.registerPlugin(ScrollTrigger);
        if (window.SplitText) gsap.registerPlugin(SplitText);

        lenis.on('scroll', ScrollTrigger.update);
        gsap.ticker.add((time) => lenis && lenis.raf(time * 1000));
        gsap.ticker.lagSmoothing(0);
      } else {
        const raf = (time) => {
          if (!lenis) return;
          lenis.raf(time);
          requestAnimationFrame(raf);
        };
        requestAnimationFrame(raf);
      }
    } catch (err) {
      console.warn('Fallback para scroll nativo:', err);
      lenis = null;
    }
  } else if (window.gsap && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);
    if (window.SplitText) gsap.registerPlugin(SplitText);
  }

  // Navegação segura de âncoras (#id) por delegação de eventos
  document.addEventListener('click', (event) => {
    const anchor = event.target.closest('a[href^="#"]');
    if (!anchor) return;
    const rawHref = anchor.getAttribute('href');
    if (!rawHref || rawHref === '#' || rawHref.length < 2) return;

    const rawId = rawHref.slice(1);
    let target = null;
    try {
      target = document.getElementById(decodeURIComponent(rawId));
    } catch {
      target = document.getElementById(rawId);
    }
    if (!target) return;

    event.preventDefault();
    const offset = getHeaderOffset();

    if (lenis) {
      lenis.scrollTo(target, { offset: -offset, duration: 1.05 });
    } else {
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({
        top: Math.max(0, top),
        behavior: prefersReduced ? 'auto' : 'smooth'
      });
    }
  });

  // Inicialize animações pesadas somente quando GSAP + ScrollTrigger existirem e sem reduced-motion
  if (!prefersReduced && window.gsap && window.ScrollTrigger) {
    document.documentElement.classList.add('motion-ready');

    // Exemplo seguro de SplitText (só roda se SplitText realmente carregou)
    if (window.SplitText) {
      document.querySelectorAll('[data-split-reveal]').forEach((el) => {
        try {
          SplitText.create(el, {
            type: 'lines',
            mask: 'lines',
            autoSplit: true,
            onSplit(self) {
              return gsap.from(self.lines, {
                yPercent: 105,
                duration: 0.75,
                stagger: 0.08,
                ease: 'power3.out',
                scrollTrigger: { trigger: el, start: 'top 88%', once: true }
              });
            }
          });
        } catch {
          // Falha silenciosa mantém o título visível normalmente
        }
      });
    }
  }
})();
```

---

## 3. Implementação para React / Next.js
- Envolva o layout raiz com `<ReactLenis root options={{ duration: 1.05, smoothWheel: true }}>` apenas quando `!prefersReducedMotion`.
- Use `@gsap/react` (`useGSAP(..., { scope: containerRef })`) para cleanup automático no unmount, ou `motion/react` (`MotionConfig reducedMotion="user"`) para `AnimatePresence` e `layoutId`.
- Use `overflow-x: clip` (nunca `hidden`) em wrappers ancestrais de qualquer `position: sticky`.