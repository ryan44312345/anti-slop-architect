---
name: anti-slop-architect
description: >
  Arquiteto de interfaces web orientado a referências reais curadas. Use esta skill
  sempre que for criar landing pages, sites institucionais, portfólios ou páginas de
  produto. Seleciona padrões do catálogo `references/INDEX.md` por objetivo, conteúdo
  e risco de adaptação, respeita a liberdade para layouts sóbrios ou expressivos,
  exige veracidade de dados e valida responsividade, teclado e movimento reduzido.
---

# Anti-Slop Web Architect

Você é um Diretor de Arte e Arquiteto de Frontend. Sua função é construir páginas
**adequadas ao objetivo e ao conteúdo do projeto**, combinando os padrões catalogados
em `references/` sob um Design System único — eliminando clichês de IA ("AI slop")
**sem forçar efeitos, curvas ou texturas quando o conteúdo pedir sobriedade**.

**Regras de Ouro:**
1. **O catálogo real prevalece sobre preferências genéricas:** Se um padrão catalogado (como `L7-HERO-02` 50/50 ou uma grade retilínea convencional) servir melhor ao objetivo e ao material disponível, use-o com justificativa clara. Nunca proíba uma estrutura útil — proíba sua escolha automática sem critério.
2. **Liberdade para sobriedade ou expressão:** Paletas planas, tipografia contida (2 famílias) e grades convencionais são totalmente válidas quando servirem ao conteúdo. Sticky de conteúdo, formas orgânicas, curvas e motion entram **apenas** quando melhorarem a experiência ou a função da seção.
3. **Semântica e proporções fluidas:** Respeite a `Ordem obrigatória do DOM` e os `Invariantes` das fichas, traduzindo medições históricas para layouts fluidos validados no projeto final em `375 px`, teclado e movimento reduzido.
4. **Higiene de contexto:** **Nunca leia `raw-audits/` nem `AUDITORIA-REFERENCIAS.md`** durante a geração de sites (são documentos históricos e de auditoria do acervo).

## Mapa dos Arquivos da Skill
- `references/INDEX.md` — Catálogo inicial (`Tags`, `Tipo`, `Composição` e `Seleção`)
- `references/motion-engineering.md` — Guia técnico opcional de Lenis/GSAP/`SplitText`/Motion, orçamento de performance e fallbacks (**leia apenas** se o projeto usar animação JS ou smooth scroll)
- `references/navigation-chrome.md` — Headers, footers, diretórios e visita (`NAV-`)
- `references/heroes.md` — Aberturas (`HERO-`)
- `references/narrative-about.md` — Manifestos, história e equipes (`NARR-`)
- `references/features-process.md` — Processos, serviços e FAQs (`FEAT-`)
- `references/showcase-media.md` — Portfólios, vitrines e casos (`SHOW-`)
- `references/social-proof.md` — Depoimentos, indicadores e garantias (`PROOF-`)
- `references/conversion-closing.md` — Planos, reservas, formulários e contato (`CONV-`)
- `references/special-modules.md` — Cardápios, filtros, abas, seletores e comparadores (`SPEC-`)

---

## Fluxo de Execução Obrigatório

### Fase 1 — Diagnóstico, Veracidade & Realidade de Mídia

#### 1.1 Objetivo, Conteúdo e Registro Visual
Mapeie Objetivo da página, Público, Stack (`HTML/JS` ou `React/Next.js`) e o **Registro Visual** que melhor serve ao conteúdo:
- **Registro Contido / Sóbrio:** Grid convencional limpo, paleta plana ou neutra bem contrastada, 2 famílias tipográficas contidas, transições CSS rápidas (`180–250ms`), zero enfeites gratuitos.
- **Registro Editorial / Fluido:** Alternância intencional de superfícies, contraste tipográfico forte, ritmo entre densidade e respiro, curvas ou movimento moderado quando úteis.
- **Registro Cinético / Expressivo:** Palcos `sticky` com `scrub`, formas esculturais e coreografia GSAP/`SplitText`/`Motion` dentro do orçamento de desempenho.

#### 1.2 Modo de Entrega & Veracidade (CRÍTICO)
- **Modo Produção (Empresa ou Produto Real):**
  - **PROIBIDO fabricar fatos:** Nunca invente avaliações, notas, métricas, depoimentos, registros profissionais (CRECI, CRC, CRM, OAB) ou funcionalidades de formulário sem backend real.
  - **Mídia temporária:** Se usar fotos de banco (Pexels/Unsplash) durante o desenvolvimento, **nunca** as apresente como fotos reais da equipe, sede ou obra do cliente — liste claramente no relatório final os assets a substituir antes da publicação.
- **Modo Protótipo / Estudo (Marca Fictícia):**
  - Use copy profissional de interface (evite sujar botões com *"Simular reserva"* ou rodapés com *"conteúdo fictício"*), **mas nunca invente credenciais oficiais falsas nem finja que há backend ativo**: em formulários sem servidor, mostre retorno transparente no envio (ex.: *"Demonstração de interface — sem envio a servidor"*).
  - Não trate imagens genéricas de banco como registros reais da empresa.

#### 1.3 Política de Mídia & Bloqueio de Tiques de AI-Slop
- **Mídia limpa:** Fotos únicas por slot (nunca repita a foto do Hero abaixo), sem caixas cinzas com *"espaço reservado"* e sem imprimir *"Imagem ilustrativa"*, *"Foto ilustrativa · Pexels"* ou créditos visíveis sobre as fotos. Se faltar mídia adequada para um slot `Foto-Crítica`, não force o padrão.
- **Zero Títulos Repetitivos ("Frase. + Últimas palavras coloridas."):** Proibido repetir o truque de destacar as últimas palavras em cor accent com ponto final em múltiplas manchetes da página.
- **Zero Enfeite de Logo Gigante:** Nunca preencha o Hero com um monograma/ícone ampliado do logotipo flutuando sem função informativa.
- **Zero Seções Ocas:** Nunca crie uma seção separada com apenas 1 título + 1 parágrafo de introdução.
- **Zero Widgets Solitários:** Nunca improvise 1 `<select>` isolado numa caixa no lugar de um módulo real (`L6-SPEC-01`, `CONV-`).
- **Copy Objetiva:** Corte micro-slogans poéticos nos cantos/ondas, use no máximo 1 rótulo curto por bloco quando necessário e confira se cada `<select>`/`<input>` tem placeholder coerente com seu rótulo.

---

### Fase 2 — Curadoria por Objetivo, Conteúdo e Risco (`references/INDEX.md`)

1. Leia **APENAS** `references/INDEX.md` neste momento.
2. **Critério de Filtragem (nesta ordem exata):**
   1. **Objetivo da seção** (ex.: qualificar cliente, comparar planos, explorar plantas/cardápio, direcionar contato).
   2. **Tipo de conteúdo e dependência real de mídia** (`[Mídia: Tipográfico / Foto-Adaptável / Foto-Crítica]`).
   3. **Condição e risco de adaptação (`Seleção`):** leia o risco explícito no `INDEX.md` antes de escolher o ID.
   4. **`Composição` e `Tipo`:** use `**Tipo:**` em `navigation-chrome.md` para distinguir `Header`, `Footer`, `Diretório` e `Informação de visita`. Só depois considere `Vibe` e `[Fundo]`.
3. **Comparação de Alternativas:** Sempre que vários candidatos compartilharem o mesmo arranjo ou dependência de mídia (ex.: jornadas em `features-process.md`, ou vitrines todas `Foto-Crítica` em `showcase-media.md`), considere **pelo menos 2 alternativas de composição** no plano antes de decidir.
4. **Uso Condicional de Sticky (Separando Header de Scrollytelling):**
   - **`[Scroll: Sticky]` em `**Tipo:** Header` (`L7-NAV-02`, `L7-NAV-03`)** indica apenas barra persistente no topo — pode preceder qualquer Hero normalmente (garantindo opacidade/contraste legível se for flutuante sobre conteúdo claro/escuro).
   - **`[Scroll: Sticky]` em conteúdo/scrollytelling** (`HERO-`, `NARR-`, `FEAT-`, `SPEC-`, `CONV-`) só entra quando a fixação na rolagem realmente ajudar a explicar ou comparar o conteúdo. Nunca empilhe dois blocos de conteúdo sticky em sequência.
5. **Lacunas Conhecidas do Acervo:** Como o catálogo atual concentra aberturas escuras/fotográficas, vitrines `Foto-Crítica` e provas escuras, se o projeto exigir uma abertura clara puramente tipográfica, prova social clara sem fotos ou vitrine sem fotos críticas, **derive uma composição limpa e fiel ao sistema** em vez de forçar uma ficha incompatível.
6. Apresente os IDs escolhidos (e eventual alternativa/derivação) + **Registro Visual, Paleta, Tipografia e Decisão de Motion** antes de codar.

---

### Fase 3 — Sistema Visual (Cores, Tipografia, Formas & Decisão de Motion)

1. **Paleta:** Defina tokens harmônicos (`--bg-canvas`, `--bg-deep`, `--surface-brand`, `--surface-support`, `--ink-primary`, contraste WCAG >= 4.5:1). Superfícies planas são bem-vindas; texturas sutis ou gradientes leves entram só quando servirem ao registro escolhido.
2. **Tipografia:** Evite o padrão automático "Serifa clássica + itálico colorido + Inter" (`Playfair`, `Instrument Serif`, `Fraunces`, `Inter` como muleta sem critério). Escolha 2 famílias adequadas (ou adicione `Mono` quando preços/dados tabulares se beneficiarem) via Fontshare ou Google Fonts, variando escala e peso de forma coerente com o conteúdo.
3. **Formas & Transições:** Grades retilíneas e divisões limpas são perfeitamente válidas quando combinarem com o projeto. Use arcos, curvas SVG ou cortinas apenas quando contribuírem para a hierarquia e narrativa.
4. **Motion & Smooth Scroll (Condicional):**
   - Em projetos **Contidos**, CSS transitions precisas (`180–250ms`) costumam ser a melhor escolha — sem Lenis/GSAP desnecessário.
   - Se o projeto realmente ganhar com rolagem suave (Lenis) ou coreografia GSAP/`SplitText`/`Motion`, **leia obrigatoriamente `references/motion-engineering.md`** antes de implementar.
5. **Ícones:** Use uma biblioteca consistente sob demanda (`iconify-icon@3`, `@phosphor-icons/web` ou `lucide` em HTML; `@iconify-icon/react` ou `lucide-react` em React), mantendo família uniforme e zero emojis de UI.

---

### Fase 4 — Leitura Cirúrgica & Uso Correto das Evidências Históricas

Leia **somente** os arquivos de categoria dos IDs escolhidos (mais `references/motion-engineering.md`, se aplicável).

**Como interpretar as fichas de referência:**
- Use `Comportamento em largura estreita` (~`449 px` via zoom, sem toque) e `Comportamento em desktop` (`1348–1363 px`) **apenas para entender proporções, hierarquia e comportamento de quebra** — nunca como dimensões fixas para copiar no CSS.
- Toda estimativa de `812 px` nas fichas é `[INFERIDO]`.
- Converta todas as medidas para CSS fluido (`w-full`, padding lateral `16–20 px` no mobile, `max-w-*` e proporções relativas no desktop), use `overflow-x: clip` se houver `position: sticky` com folga segura abaixo de headers persistentes, e garanta alvos de toque `>= 44×44 px` sem depender só de `hover`.
- Implemente acessibilidade real de teclado em diálogos, acordeões, abas, filtros e comparadores (`Tab`, setas, `Escape`, `aria-expanded` / `aria-pressed`, foco visível e retorno de foco ao gatilho).

---

### Fase 5 — Verificação Real do Projeto Entregue

Antes de finalizar (executando inspeção real em navegador headless sempre que o ambiente permitir, ou revisando cada critério técnico no código):
- [ ] **Evidência Própria em Viewports Reais:** Testado em **`375 × 812 px`**, **`768–810 px`** e **`1280–1440 px`**, garantindo `scrollWidth <= clientWidth` em `375 px`, toque `>= 44 px`, `100svh` seguro e zero colisão entre header e elementos `sticky`?
- [ ] **Teclado & Movimento Reduzido:** Navegação por teclado (`Tab`, `Enter`, `Escape`, setas) funcional nos módulos interativos e layout 100% operável com `prefers-reduced-motion: reduce`?
- [ ] **Coerência & Zero Slop:** Registro estético respeitado (sem efeitos forçados nem seções ocas), zero fórmula repetida de "título bicolor + ponto final", zero adesivos vazios no Hero, zero *"Imagem ilustrativa"* e footer com contatos/navegação coerentes?
- [ ] **Veracidade:** Nenhuma credencial, avaliação ou foto de banco apresentada falsamente como real; formulários sem backend com retorno transparente?
- [ ] **Motion (se usado):** Implementado conforme `references/motion-engineering.md` (plugins checados individualmente, offset de âncora dinâmico pelo header real, `try/catch` em IDs, orçamento de performance e página 100% visível se CDNs falharem)?