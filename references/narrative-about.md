# narrative-about.md

#### L2-NARR-01 — Fotos instantâneas com manifesto em recibo

- **Categoria destino** — `narrative-about.md`
- **ID sugerido** — `L2-NARR-01`
- **Nome do padrão** — Fotos instantâneas com manifesto em recibo
- **Fonte** — [Gribble](https://gribble.framer.website/)
- **Nichos indicados** — hamburguerias, bares e marcas gastronômicas autorais

##### Requisitos de Mídia e Copy

Três fotos de momentos distintos, com recortes retrato e legendas de até quatro palavras. Manifesto de cerca de 25 palavras e recibo com linhas sintéticas.

##### Ordem obrigatória do DOM

1. Pilha de fotos legendadas.
2. Comando de avanço e seletores.
3. H2, módulo de recibo, parágrafo, link de história e botão de reimpressão.

##### Comportamento Mobile-First observado (375px)

Pilha primeiro e narrativa abaixo. Margens de 20 px e palco de 352 × 394 px (0,89:1). Molduras claras com sobreposição e fitas em fundo creme. A seção mediu pelo menos 967 px e ultrapassa 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

O grid de 12 trilhas cria duas metades de 630 px, com vão de 24 px e margens de 32 px. Palco fotográfico de 433 × 485 px. Parágrafo com 412 px. Na captura, o recibo expandido mostrou tipografia monoespaçada e linhas de papel térmico. O CSS da página tem faixa em 810 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Pilha interativa precede narrativa no DOM. Recibo funciona como peça da narrativa.
- **Adaptáveis** — Fotos, cores e grafismos do papel.

##### Animações & Interações observadas

- Clique na pilha → mudou a foto em primeiro plano e o marcador ativo. Gatilho da impressão inicial e reação ao botão de reimpressão [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Escolher fotos que sugiram situações distintas. O recibo deve acrescentar informação ou voz, sem repetir o parágrafo.

#### L3-NARR-01 — Painel de ofício com números em círculos

- **Categoria destino** — `narrative-about.md`
- **ID sugerido** — `L3-NARR-01`
- **Nome do padrão** — Painel de ofício com números em círculos
- **Fonte** — [Ruota](https://ruota-template.framer.website/)
- **Nichos indicados** — cantinas artesanais, padarias e torrefações

##### Requisitos de Mídia e Copy

Dispensa fotografia. Rótulo de duas ou três palavras, título de até duas linhas, parágrafo de cerca de 35 palavras e três dados operacionais com legendas breves.

##### Ordem obrigatória do DOM

1. Identificador e título.
2. Parágrafo de contexto.
3. Três pares de valor e legenda na ordem de leitura.

##### Comportamento Mobile-First observado (375px)

Painel de 429 px com raio de 28 px e conteúdo de 389 px. Título e parágrafo empilhados. A faixa dos indicadores passa para uma coluna e mede 752 px. Título, parágrafo e os três indicadores excedem a dobra local de 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Painel vermelho de 1300 × 860 px com raio de 40 px e conteúdo de 1204 px. Blocos superiores de 700 e 440 px, com vão de 64 px. Os três círculos se distribuem em linha; as caixas podem variar durante a entrada. O CSS da página declara faixas em 810 e 1200 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Três dados explicam o mesmo ofício e aparecem depois do contexto.
- **Adaptáveis** — Cor de superfície, tipografia, tamanho e contorno dos círculos.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Escolher dados que informem algo concreto sobre produção e atendimento. Reservar área suficiente para cada legenda sem sobrepor os valores.

#### L3-NARR-02 — Retratos da equipe com ficha de função

- **Categoria destino** — `narrative-about.md`
- **ID sugerido** — `L3-NARR-02`
- **Nome do padrão** — Retratos da equipe com ficha de função
- **Fonte** — [Foodee](https://foodee.framer.website/)
- **Nichos indicados** — restaurantes autorais, confeitaria e hospitalidade

##### Requisitos de Mídia e Copy

Quatro retratos verticais, nome e função em uma linha sempre que possível e descrição de aproximadamente 15–25 palavras.

##### Ordem obrigatória do DOM

1. Identificador, título, descrição e link da equipe.
2. Lista de pessoas.
3. Por pessoa: mídia com descrição associada, nome e função, depois elemento de ação.

##### Comportamento Mobile-First observado (375px)

Coluna única de 401 px com margem de 24 px. Módulo por pessoa de 459 px, retrato de 300 × 380 px (0,79:1). O primeiro cartão cabe isoladamente em 812 px, mas cabeçalho mais cartão e espaçamentos ultrapassam a dobra local a partir do topo da seção.

##### Expansão Desktop observada (1024px+ / 1440px)

Quatro retratos na mesma linha dentro de 1152 px. Área de nome com cerca de 270 px por cartão. Retratos de 300 × 380 px. A seção usa sticky no desktop e relativa na variante estreita. CSS da página inclui 810 e 1200 px; limiar específico não isolado.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Cada retrato precisa carregar nome, função e descrição da mesma pessoa.
- **Adaptáveis** — Direção dos retratos, fonte, fundo e ícone.

##### Animações & Interações observadas

- Controle presente na estrutura do cartão estreito. Resposta visual ao acionamento [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Dirigir os retratos em escala e enquadramento coerentes. Manter o nome e a função legíveis mesmo sem interagir.

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
