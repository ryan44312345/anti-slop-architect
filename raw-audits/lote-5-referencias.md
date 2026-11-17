# Lote 5 — Referências web

## Páginas inspecionadas

| Site | URL inspecionada | Desktop | Mobile | Overflow horizontal |
| --- | --- | --- | --- | --- |
| Caldren | https://caldren.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1363 = 1363 · Mobile 449 = 449 |
| Dental Point | https://dental-point-clinic.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Advocacy | https://advocacy-template.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Koddam | https://koddam.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |

Dimensões em `innerWidth × innerHeight`. Overflow compara `scrollWidth` e `clientWidth` da raiz. Inspeção no navegador virtual com capturas pontuais, rolagem amostrada até o rodapé e leitura do DOM. A variante estreita foi verificada com o fallback aprovado a 300%, com 449 px de área útil. Os rótulos seguem o modelo anterior. 375 px e toque não foram testados. A dobra de 812 px foi estimada pelas caixas renderizadas, a partir do topo de cada seção. Os breakpoints específicos dos módulos não foram isolados. As URLs da tabela são as páginas de origem, sem redirecionamento na abertura.

## Fichas por categoria

### `special-modules.md`

#### L5-SPEC-01 — Ficha de imóvel com fotografia dominante e dados de venda

- **Categoria destino** — `special-modules.md`
- **ID sugerido** — `L5-SPEC-01`
- **Nome do padrão** — Ficha de imóvel com fotografia dominante e dados de venda
- **Fonte** — [Caldren](https://caldren.framer.website/)
- **Nichos indicados** — incorporadoras, imobiliárias e lançamentos

##### Requisitos de Mídia e Copy

Uma foto principal e três complementares. Nome curto, introdução de uma frase, preço, localização e cerca de cinco especificações.

##### Ordem obrigatória do DOM

1. Nome e introdução com link.
2. Corpo com foto principal e painel de venda.
3. No painel: condição, local, preço, especificações e CTAs.
4. Galeria de apoio com legendas.

##### Comportamento Mobile-First observado (375px)

Coluna de 409 px, margem de 20 px. Foto principal de 409 × 300 px (1,36:1), painel de cerca de 499 px e fotos secundárias de 409 × 240 px (1,70:1). Foto mais painel já somam cerca de 799 px sem vãos ou cabeçalho. A ficha inteira ultrapassa 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Faixa de 1235 px. Foto de 803 × 620 px e painel cinza-claro de 408 × 620 px, cerca de 66/34 sem o vão de 24 px. Três fotos secundárias de 396 × 260 px em linha.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Cada valor mantém seu rótulo. Ações pertencem ao mesmo imóvel que as imagens e os dados.
- **Adaptáveis** — Paleta, tipografia e estilo dos botões.

##### Animações & Interações observadas

- Clique em Details → abriu a página do imóvel em /properties/caldren-residence-07. Efeito visual próprio ao hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Separar condição comercial, preço e características físicas. Dar contexto diferente a cada imagem secundária.

##### Linha pronta para o `INDEX.md`

- **L5-SPEC-01 | Ficha de imóvel com fotografia dominante e dados de venda** — Melhor para: incorporadoras, imobiliárias e lançamentos. Vibe: arquitetônica e precisa. (Fonte: Caldren) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Claro]

### `narrative-about.md`

#### L5-NARR-01 — Manifesto imobiliário com quatro princípios numerados

- **Categoria destino** — `narrative-about.md`
- **ID sugerido** — `L5-NARR-01`
- **Nome do padrão** — Manifesto imobiliário com quatro princípios numerados
- **Fonte** — [Caldren](https://caldren.framer.website/)
- **Nichos indicados** — imobiliárias autorais, arquitetura e serviços premium

##### Requisitos de Mídia e Copy

Uma foto arquitetônica. Título de até três linhas, quatro princípios com nome curto e uma frase explicativa cada.

##### Ordem obrigatória do DOM

1. Introdução com título e imagem.
2. Lista de quatro princípios.
3. Em cada item: número, título e descrição.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 409 px, margem de 20 px. Foto de 409 × 320 px (1,28:1). Introdução de cerca de 474 px seguida por uma lista de 664 px. A seção excede 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Introdução de 520 px e lista de 619 px, cerca de 46/54, com vão de 96 px. Foto de 520 × 560 px. As quatro linhas usam números em faixa separada à esquerda dos textos.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Cada princípio precisa de um exemplo concreto no texto. Preservar a ordem título, imagem e lista.
- **Adaptáveis** — Fotografia, tipografia, numeração e separadores.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Descrever critérios reais de seleção, apresentação e atendimento. Preparar a foto para os recortes vertical e horizontal.

##### Linha pronta para o `INDEX.md`

- **L5-NARR-01 | Manifesto imobiliário com quatro princípios numerados** — Melhor para: imobiliárias autorais, arquitetura e serviços premium. Vibe: editorial e metódica. (Fonte: Caldren) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Claro]

#### L5-NARR-02 — Equipe em grade com título ocupando a primeira célula

- **Categoria destino** — `narrative-about.md`
- **ID sugerido** — `L5-NARR-02`
- **Nome do padrão** — Equipe em grade com título ocupando a primeira célula
- **Fonte** — [Advocacy](https://advocacy-template.framer.website/)
- **Nichos indicados** — escritórios, consultorias e equipes institucionais

##### Requisitos de Mídia e Copy

Retratos com foco central para recorte quadrado e horizontal. Um nome e um cargo por perfil.

##### Ordem obrigatória do DOM

1. Título do conjunto como primeiro item.
2. Cartões de pessoas em ordem de leitura.
3. Em cada cartão: retrato, nome e cargo.

##### Comportamento Mobile-First observado (375px)

Grade de uma coluna útil de 409 px e margem de 20 px. Retrato de 369 × 260 px (1,42:1), cartão de 386 px de altura. O título precede o primeiro retrato. Um perfil cabe em 812 px e o conjunto requer rolagem.

##### Expansão Desktop observada (1024px+ / 1440px)

Três colunas de cerca de 383 px com vão de 20 px. Título ocupa a primeira célula, seguido de dois perfis na primeira linha. Retratos de 260 × 260 px dentro dos cartões de 393 px de altura.

##### Invariantes vs. Adaptáveis

- **Invariantes** — O título é o primeiro item semântico da grade. Nome e cargo permanecem ligados ao retrato.
- **Adaptáveis** — Fundo, tipografia, enquadramento e quantidade de perfis.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Alinhar escala e altura dos rostos. Usar a célula inicial para introduzir a equipe com texto curto.

##### Linha pronta para o `INDEX.md`

- **L5-NARR-02 | Equipe em grade com título ocupando a primeira célula** — Melhor para: escritórios, consultorias e equipes institucionais. Vibe: editorial e humana. (Fonte: Advocacy) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Adaptável]

### `features-process.md`

#### L5-FEAT-01 — Etapas de atendimento com fotografia da jornada

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L5-FEAT-01`
- **Nome do padrão** — Etapas de atendimento com fotografia da jornada
- **Fonte** — [Dental Point](https://dental-point-clinic.framer.website/)
- **Nichos indicados** — clínicas, estúdios e serviços agendados

##### Requisitos de Mídia e Copy

Três fotos que representem momentos distintos do atendimento. Um título e uma frase operacional por etapa.

##### Ordem obrigatória do DOM

1. Identificador e título da seção.
2. Três etapas numeradas.
3. Em cada etapa: número, título, texto curto e imagem.

##### Comportamento Mobile-First observado (375px)

Trilho estreito com cartão ativo perto de 417 × 624 px e imagem de 417 × 334 px (1,25:1). Bordas suavizadas na foto. O cabeçalho de 190 px mais o cartão e o vão ultrapassam a dobra de 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Três blocos sucessivos. Cada linha de 1284 × 680 px tem grupos de 308, 462 e 514 px, cerca de 24/36/40. A fotografia é vertical (514 × 680 px), com número isolado e título e texto no bloco central.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Número, descrição e foto identificam a mesma etapa. Manter a leitura em sequência.
- **Adaptáveis** — Direção fotográfica, tipo de numeração e paleta.

##### Animações & Interações observadas

- O trilho mostrou uma etapa em destaque e bordas das vizinhas na largura estreita. Gatilho exato da troca [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar o texto para explicar o que a pessoa faz ou encontra. Evitar repetir a mesma descrição entre etapas.

##### Linha pronta para o `INDEX.md`

- **L5-FEAT-01 | Etapas de atendimento com fotografia da jornada** — Melhor para: clínicas, estúdios e serviços agendados. Vibe: humana e editorial. (Fonte: Dental Point) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Claro]

### `conversion-closing.md`

#### L5-CONV-01 — Comparação de dois pacotes por visita

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L5-CONV-01`
- **Nome do padrão** — Comparação de dois pacotes por visita
- **Fonte** — [Dental Point](https://dental-point-clinic.framer.website/)
- **Nichos indicados** — clínicas, estúdios e serviços com pacotes

##### Requisitos de Mídia e Copy

Nome e público de cada pacote, preço com unidade, cerca de quatro inclusões e um CTA por opção. Dispensa fotos.

##### Ordem obrigatória do DOM

1. Título e introdução.
2. Dois planos.
3. Em cada plano: nome, perfil indicado, preço e unidade, lista de itens e CTA.

##### Comportamento Mobile-First observado (375px)

Os planos se empilham em faixa de 417 px. O primeiro cartão mede 385 × 516 px, com área interna de 353 px e CTA de 48 px de altura. Um cartão cabe isoladamente em 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Dois cartões de cerca de 618 × 622 px. Superfície creme no primeiro e preto no segundo. Conteúdo interno de 538 px e botões de largura própria.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter unidade do preço ao lado do valor e repetir a sequência de leitura nos dois planos.
- **Adaptáveis** — Cores, tipografia, ícones e destaque visual.

##### Animações & Interações observadas

- Links de agendamento identificados. Hover e conclusão do agendamento [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Explicitar o que está incluído e se o preço é por visita. Usar contraste para hierarquia, com leitura equivalente nos dois planos.

##### Linha pronta para o `INDEX.md`

- **L5-CONV-01 | Comparação de dois pacotes por visita** — Melhor para: clínicas, estúdios e serviços com pacotes. Vibe: editorial e objetiva. (Fonte: Dental Point) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Adaptável]

#### L5-CONV-02 — Três níveis de consultoria com plano central destacado

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L5-CONV-02`
- **Nome do padrão** — Três níveis de consultoria com plano central destacado
- **Fonte** — [Koddam](https://koddam.framer.website/)
- **Nichos indicados** — consultorias, serviços recorrentes e SaaS

##### Requisitos de Mídia e Copy

Nome, público-alvo em uma frase, valor com recorrência, cerca de quatro inclusões e CTA por plano.

##### Ordem obrigatória do DOM

1. Identificador, título e introdução.
2. Grade de planos.
3. Em cada plano: nome, descrição, preço, inclusões e ação.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 419 px, margem de 15 px. Cada cartão mede cerca de 467 px de altura e tem CTA de 379 × 40 px. Cabe o título e um plano em aproximadamente 812 px, conforme os espaçamentos medidos.

##### Expansão Desktop observada (1024px+ / 1440px)

Três cartões de 416 × 481 px com vão de 20 px. Cartão central verde-claro e dois brancos. CTAs pretos de 376 × 40 px alinhados na base.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Mesma hierarquia de preço e inclusões nos três cartões. A comparação preserva a ordem dos planos.
- **Adaptáveis** — Cores, tipografia, recorrência e quantidade de benefícios.

##### Animações & Interações observadas

- Links Get Started presentes. Transição visual de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar o destaque para justificar a escolha central com uma diferença concreta de escopo. Alinhar preço e botão mesmo quando o texto variar.

##### Linha pronta para o `INDEX.md`

- **L5-CONV-02 | Três níveis de consultoria com plano central destacado** — Melhor para: consultorias, serviços recorrentes e SaaS. Vibe: comercial e limpa. (Fonte: Koddam) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Claro]

### `showcase-media.md`

#### L5-SHOW-01 — Cartões altos de serviços com texto sobre fotografia

- **Categoria destino** — `showcase-media.md`
- **ID sugerido** — `L5-SHOW-01`
- **Nome do padrão** — Cartões altos de serviços com texto sobre fotografia
- **Fonte** — [Advocacy](https://advocacy-template.framer.website/)
- **Nichos indicados** — advocacia, consultorias e escritórios especializados

##### Requisitos de Mídia e Copy

Uma foto vertical diferente por especialidade. Nome em até duas linhas, descrição de cerca de 20 palavras e CTA curto.

##### Ordem obrigatória do DOM

1. Identificador e título.
2. Lista de cartões.
3. Em cada cartão: imagem de fundo, número e título, descrição e link.

##### Comportamento Mobile-First observado (375px)

Dois cartões visíveis no DOM estreito mediam 360 × 450 px (0,80:1) com recuo de 15 px. Conteúdo branco sobre foto escurecida. Um cartão cabe em 812 px. O terceiro serviço apareceu na variante larga.

##### Expansão Desktop observada (1024px+ / 1440px)

Três cartões de 426 × 600 px (0,71:1), lado a lado, com intervalos de 20 px. Número e título no topo, descrição e botão perto da base. Contornos retos.

##### Invariantes vs. Adaptáveis

- **Invariantes** — O título e a ação permanecem dentro do mesmo cartão e legíveis sobre a foto.
- **Adaptáveis** — Número de serviços, imagens, paleta e tipografia.

##### Animações & Interações observadas

- O primeiro link Learn more apontava para /services/litigation-support. Efeito visual próprio ao hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Reservar no recorte duas áreas tranquilas para texto. Na adaptação estreita, garantir uma rota para cada serviço do desktop.

##### Linha pronta para o `INDEX.md`

- **L5-SHOW-01 | Cartões altos de serviços com texto sobre fotografia** — Melhor para: advocacia, consultorias e escritórios especializados. Vibe: sóbria e fotográfica. (Fonte: Advocacy) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Escuro]

### `social-proof.md`

#### L5-PROOF-01 — Indicadores de impacto com gráfico de quatro períodos

- **Categoria destino** — `social-proof.md`
- **ID sugerido** — `L5-PROOF-01`
- **Nome do padrão** — Indicadores de impacto com gráfico de quatro períodos
- **Fonte** — [Koddam](https://koddam.framer.website/)
- **Nichos indicados** — consultorias, serviços B2B e empresas de tecnologia

##### Requisitos de Mídia e Copy

Três valores com unidade, rótulo e frase. Quatro barras com percentual e período. Dispensa fotos.

##### Ordem obrigatória do DOM

1. Identificador da seção.
2. Três indicadores com valor, rótulo e explicação.
3. Gráfico com quatro valores e respectivos períodos.

##### Comportamento Mobile-First observado (375px)

Faixa de 419 px com margem de 15 px. Indicadores empilhados em área de 593 px. Gráfico abaixo com 300 px e quatro barras de cerca de 97 px. O conjunto ultrapassa 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Faixa de 1288 px e altura de seção de 746 px. Identificador e três indicadores em linha com divisórias. Gráfico de 1006 × 300 px, deslocado para alinhar com os indicadores. Uma barra verde-clara contrasta com as demais brancas sobre verde escuro.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Cada barra mantém valor e período. A escala visual deve representar os números proporcionalmente.
- **Adaptáveis** — Paleta, fontes, períodos e métricas.

##### Animações & Interações observadas

- Barra destacada visualmente. Gatilho de destaque e resposta ao hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Identificar a grandeza, período e fonte do gráfico. Usar números verificáveis ao adaptar o módulo.

##### Linha pronta para o `INDEX.md`

- **L5-PROOF-01 | Indicadores de impacto com gráfico de quatro períodos** — Melhor para: consultorias, serviços B2B e empresas de tecnologia. Vibe: analítica e sóbria. (Fonte: Koddam) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Escuro]
