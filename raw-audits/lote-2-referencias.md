# Lote 2 — Referências web

## Páginas inspecionadas

| Site | URL inspecionada | Desktop | Mobile | Overflow horizontal |
| --- | --- | --- | --- | --- |
| Ligatra | https://only-instance-526558.framer.app/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Gribble | https://gribble.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| FineDine Home | https://finedine-template.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| FineDine /menu | https://finedine-template.framer.website/menu | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |

Dimensões medidas por `innerWidth × innerHeight`. Overflow compara `scrollWidth` com `clientWidth` na raiz. Os quatro endereços abriram diretamente. O DevTools ficou bloqueado e o redimensionamento não alterou o viewport. A coleta usou o fallback autorizado de zoom a 300%, com leitura do DOM renderizado, capturas pontuais e rolagem amostrada até o rodapé. A área útil foi de 1348 px no desktop e 449 px no mobile. O cabeçalho das fichas segue o formato solicitado. O viewport de 375 px e a emulação de toque não foram testados. A dobra de 812 px é estimada a partir do topo de cada seção pelas dimensões internas. Proporções são das caixas renderizadas. Alturas de conteúdo dinâmico podem variar após o carregamento. Os breakpoints são apresentados como confirmados por amostras ou como faixas de CSS, conforme a evidência.

## Fichas por categoria

### `features-process.md`

#### L2-FEAT-01 — Palco sticky com quatro etapas de preparo

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L2-FEAT-01`
- **Nome do padrão** — Palco sticky com quatro etapas de preparo
- **Fonte** — [Ligatra](https://only-instance-526558.framer.app/)
- **Nichos indicados** — hamburguerias, torrefações e marcas artesanais

##### Requisitos de Mídia e Copy

Uma mídia por etapa, com recorte paisagem. Um verbo e uma frase de até 15 palavras por etapa.

##### Ordem obrigatória do DOM

1. Identificador e H2.
2. Palco com janela de mídia e quatro chips.
3. Lista com número, título e frase em cada etapa.

##### Comportamento Mobile-First observado (375px)

Coluna única com margem de 20 px. Janela de 409 × 230 px (16:9), raio de 20 px. Palco e primeira etapa somam cerca de 527 px e cabem em uma dobra local de 812 px. Só a lista completa ocupa 880 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Palco de 776 px e lista de 340 px, proporção aproximada 70/30, separados por 64 px. Janela de 776 × 520 px (1,49:1), raio de 32 px. Cada etapa reserva 540 px de percurso. A pilha já estava ativa a 1090 px, compatível com a faixa CSS que muda a 1200 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Palco antes das etapas, um chip e uma mídia por etapa.
- **Adaptáveis** — Paleta, fonte, raios e linguagem fotográfica.

##### Animações & Interações observadas

- O palco tem posição sticky no DOM. A reação específica da mídia ao clicar nos chips ficou [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Justificar o trecho de rolagem com mudanças reais de preparo. Manter verbo, mídia e etapa atual sincronizados.

##### Linha pronta para o `INDEX.md`

- **L2-FEAT-01 | Palco sticky com quatro etapas de preparo** — Melhor para: hamburguerias, torrefações e marcas artesanais. Vibe: cinematográfica e didática. (Fonte: Ligatra) | Tags: [Mídia: Foto-Crítica] [Scroll: Sticky] [Fundo: Escuro]

#### L2-FEAT-02 — Cinco verbos do ofício em colunas editoriais

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L2-FEAT-02`
- **Nome do padrão** — Cinco verbos do ofício em colunas editoriais
- **Fonte** — [FineDine Home](https://finedine-template.framer.website/)
- **Nichos indicados** — restaurantes autorais, cafés especiais e ateliês

##### Requisitos de Mídia e Copy

Cinco fotos documentais de etapas distintas. Um verbo, uma leitura ou tradução curta e cerca de 15–25 palavras por painel.

##### Ordem obrigatória do DOM

1. Título e subtítulo.
2. Lista de painéis.
3. Em cada painel: inscrição, fotografia, H3, leitura do termo e descrição.
4. Link de aprofundamento.

##### Comportamento Mobile-First observado (375px)

Uma coluna em faixa de 409 px com margem de 20 px. Fotos de 365 × 300 px (1,22:1), com 22 px de recuo interno. Painéis de 749–770 px cabem isoladamente em 812 px. Fundo escuro com separadores discretos.

##### Expansão Desktop observada (1024px+ / 1440px)

Cinco colunas de aproximadamente 250 px em 1252 px. Imagens de 206 × 300 px (0,69:1), separadores verticais e inscrição âmbar sobre fundo escuro. CSS contém faixas em 810 e 1200 px. O limiar específico da grade de cinco colunas não foi isolado.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Uma foto por verbo e a mesma sequência de inscrição, foto e explicação.
- **Adaptáveis** — Idioma, cor, fontes e assunto fotográfico.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Usar inscrição em outro idioma quando tiver função informativa. Planejar foco fotográfico que aceite cortes vertical e horizontal.

##### Linha pronta para o `INDEX.md`

- **L2-FEAT-02 | Cinco verbos do ofício em colunas editoriais** — Melhor para: restaurantes autorais, cafés especiais e ateliês. Vibe: sóbria e artesanal. (Fonte: FineDine Home) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Escuro]

### `conversion-closing.md`

#### L2-CONV-01 — Unidades com pedido e rota por loja

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L2-CONV-01`
- **Nome do padrão** — Unidades com pedido e rota por loja
- **Fonte** — [Ligatra](https://only-instance-526558.framer.app/)
- **Nichos indicados** — redes de restaurantes, cafeterias e lojas físicas

##### Requisitos de Mídia e Copy

Uma foto por unidade, endereço completo, horários em linhas separadas e dois rótulos curtos de ação.

##### Ordem obrigatória do DOM

1. Identificador da seção e H2.
2. Lista de unidades.
3. Em cada unidade: foto, nome, endereço, horários e ações de pedido e rota.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 409 px com margem de 20 px e raio de 22 px. Imagens de aproximadamente 409 × 200 px (2,05:1). Cartões de 412–449 px cabem isoladamente em 812 px. A lista completa excede a dobra.

##### Expansão Desktop observada (1024px+ / 1440px)

Três colunas de 380 px com vão de 20 px, superfície clara e cartões com raio de 28 px. Imagens de 380 × 240 px (1,58:1). A 1090 px já havia uma coluna, compatível com a faixa CSS de 1200 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Cada ação pertence à unidade no mesmo cartão. A foto precede os dados operacionais.
- **Adaptáveis** — Paleta, imagens e estilos de botão.

##### Animações & Interações observadas

- Links de pedido e rota identificados no DOM. Efeito visual de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Permitir alturas diferentes conforme os horários. Direcionar pedido e rota à unidade correta.

##### Linha pronta para o `INDEX.md`

- **L2-CONV-01 | Unidades com pedido e rota por loja** — Melhor para: redes de restaurantes, cafeterias e lojas físicas. Vibe: direta e acolhedora. (Fonte: Ligatra) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Claro]

### `social-proof.md`

#### L2-PROOF-01 — Nota agregada com trilha de depoimentos

- **Categoria destino** — `social-proof.md`
- **ID sugerido** — `L2-PROOF-01`
- **Nome do padrão** — Nota agregada com trilha de depoimentos
- **Fonte** — [Ligatra](https://only-instance-526558.framer.app/)
- **Nichos indicados** — restaurantes, serviços locais e franquias

##### Requisitos de Mídia e Copy

Nota e volume em duas linhas. Citações de cerca de 10–20 palavras com nome e fonte.

##### Ordem obrigatória do DOM

1. Nota e volume de avaliações.
2. Controles anterior e próximo.
3. Trilha horizontal com estrelas, citação, nome e fonte em cada cartão.

##### Comportamento Mobile-First observado (375px)

Controles de 48 px abaixo do título. Cartão de 300 × 320 px, raio de 22 px, recuo inicial de 20 px e vão de 14 px. Parte do próximo cartão fica visível. A caixa da seção mediu 692 px e cabe em 812 px a partir de seu topo.

##### Expansão Desktop observada (1024px+ / 1440px)

Título e setas na mesma linha. Cartões de 380 × 360 px, raios de 28 px, recuo inicial de 84 px e vãos de 20 px. Três cartões mais parte do quarto. A trilha permanece horizontal nas amostras intermediárias.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Resumo precede relatos. Manter navegação acessível e pista visual do próximo cartão.
- **Adaptáveis** — Cor das estrelas, fundo, fonte e tamanho dos cartões.

##### Animações & Interações observadas

- Clique em Next no desktop → a trilha avançou cerca de 399 px, um cartão mais o vão. Efeito específico de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar nota e volume com origem verificável. Manter os controles fora da caixa de citação.

##### Linha pronta para o `INDEX.md`

- **L2-PROOF-01 | Nota agregada com trilha de depoimentos** — Melhor para: restaurantes, serviços locais e franquias. Vibe: enfática e calorosa. (Fonte: Ligatra) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Escuro]

### `narrative-about.md`

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

##### Linha pronta para o `INDEX.md`

- **L2-NARR-01 | Fotos instantâneas com manifesto em recibo** — Melhor para: hamburguerias, bares e marcas gastronômicas autorais. Vibe: retrô e social. (Fonte: Gribble) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Claro]

### `showcase-media.md`

#### L2-SHOW-01 — Vitrine de mais vendidos com produtos recortados

- **Categoria destino** — `showcase-media.md`
- **ID sugerido** — `L2-SHOW-01`
- **Nome do padrão** — Vitrine de mais vendidos com produtos recortados
- **Fonte** — [Gribble](https://gribble.framer.website/)
- **Nichos indicados** — hamburguerias, sorveterias e lojas de alimentos

##### Requisitos de Mídia e Copy

Fotos recortadas em escala visual equivalente. Nome curto, preço em uma linha e selo opcional.

##### Ordem obrigatória do DOM

1. H2 e link para cardápio completo.
2. Grade de produtos.
3. Em cada cartão: mídia, nome, preço e selo opcional.

##### Comportamento Mobile-First observado (375px)

Coluna de 385 px com margem de 32 px. Cartões de aproximadamente 385 × 380 px (quase quadrados), raio de 16 px. CTA abaixo do título. Cabe o cabeçalho e um cartão em 812 px, com parte do segundo.

##### Expansão Desktop observada (1024px+ / 1440px)

Duas colunas de 634 px, vão de 16 px, cartões de 380 px de altura. Título à esquerda e CTA à direita. A grade ainda tinha duas colunas em 909 px e uma em 779 px, coerente com o breakpoint CSS de 810 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Centro visual consistente para as fotos, sequência nome e preço, saída única para o cardápio completo.
- **Adaptáveis** — Fundo, letras, cor de preço e forma dos selos.

##### Animações & Interações observadas

- Link do cardápio presente. Resposta visual ao ponteiro nos cartões [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Reservar selos para distinções reais. Equalizar a escala aparente dos produtos, inclusive quando seus recortes diferirem.

##### Linha pronta para o `INDEX.md`

- **L2-SHOW-01 | Vitrine de mais vendidos com produtos recortados** — Melhor para: hamburguerias, sorveterias e lojas de alimentos. Vibe: pop e limpa. (Fonte: Gribble) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Claro]

### `navigation-chrome.md`

#### L2-NAV-01 — Diretório de unidades com mapa expansível

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L2-NAV-01`
- **Nome do padrão** — Diretório de unidades com mapa expansível
- **Fonte** — [FineDine Home](https://finedine-template.framer.website/)
- **Nichos indicados** — restaurantes com filiais, hotéis e espaços de atendimento

##### Requisitos de Mídia e Copy

Um mapa por unidade, texto de rota e dados operacionais. Nome, endereço e horário visíveis mesmo com o painel fechado.

##### Ordem obrigatória do DOM

1. Identificador, H2 e explicação.
2. Lista de unidades com botão contendo nome, endereço, horário e ícone.
3. Painel com mapa, dados de transporte e acesso, telefone, email e ações de rota e reserva.

##### Comportamento Mobile-First observado (375px)

Lista de 409 px com margens de 20 px. Cabeçalho de aproximadamente 175 px. No painel aberto o mapa de 165 × 400 px ficou ao lado dos dados, que quebraram em várias linhas. Cabe um cabeçalho fechado em 812 px. O encaixe do painel aberto depende das quebras e do conteúdo.

##### Expansão Desktop observada (1024px+ / 1440px)

Faixa de 1252 px. Cabeçalho de cerca de 109 px, com nome, endereço e horários em grupos horizontais. Mapa aberto de 586 × 400 px ao lado dos detalhes. Divisórias finas em fundo escuro. CSS inclui 810 e 1200 px, com limiar do componente sem isolamento.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Dados operacionais no estado fechado. Mapa e ações vinculados à unidade correspondente.
- **Adaptáveis** — Arte do mapa, paleta, separadores e textos dos botões.

##### Animações & Interações observadas

- Clique em Park Slope → o traço vertical do ícone girou em direção à posição horizontal. Exibição final dos detalhes da unidade [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Dimensionar a área de texto para preservar telefone e email. Acompanhar o mapa com instruções textuais.

##### Linha pronta para o `INDEX.md`

- **L2-NAV-01 | Diretório de unidades com mapa expansível** — Melhor para: restaurantes com filiais, hotéis e espaços de atendimento. Vibe: precisa e discreta. (Fonte: FineDine Home) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Escuro]

### `special-modules.md`

#### L2-SPEC-01 — Índice de categorias com fotografia lateral do cardápio

- **Categoria destino** — `special-modules.md`
- **ID sugerido** — `L2-SPEC-01`
- **Nome do padrão** — Índice de categorias com fotografia lateral do cardápio
- **Fonte** — [FineDine /menu](https://finedine-template.framer.website/menu)
- **Nichos indicados** — fine dining, restaurantes omakase e cardápios sazonais

##### Requisitos de Mídia e Copy

Foto dedicada por prato, nome e preço com leitura próxima, descrição de 8–18 palavras e ingredientes em lista breve.

##### Ordem obrigatória do DOM

1. Coluna fotográfica na variante larga.
2. Índice de categorias.
3. Categorias com título, subtítulo e lista de pratos.
4. Em cada registro: nome, nome original, preço, descrição e ingredientes, com foto antes do conteúdo na variante empilhada e selo opcional.

##### Comportamento Mobile-First observado (375px)

Índice horizontal no início da coluna. Registros em área de 409 px e margens de 20 px. A coluna lateral tem altura zero e a mídia do prato passa a ocupar 409 × 320 px (1,28:1). Registros de 512–533 px cabem isoladamente em 812 px. Fundo escuro e separadores finos, sem cartões arredondados.

##### Expansão Desktop observada (1024px+ / 1440px)

Coluna sticky de 567 × 936 px, lista de 661 px e vão de 72 px. Proporção aproximada 46/54 sem o vão. Linhas de cerca de 119 px com preço à direita. CSS tem faixas em 810 e 1200 px. O limiar específico da supressão do palco lateral não foi isolado.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Associação entre categoria, prato, preço, foto e link de detalhe. Índice conduz ao grupo correspondente.
- **Adaptáveis** — Idiomas, tipografia, paleta e direção de fotografia.

##### Animações & Interações observadas

- Clique em Robata → a página rolou até a categoria, com H2 a cerca de 206 px do topo e hash inalterado. Gatilho exato da troca da imagem lateral [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Reservar espaço após o salto para o título. Manter preço próximo ao nome e associar a foto ao prato correto.

##### Linha pronta para o `INDEX.md`

- **L2-SPEC-01 | Índice de categorias com fotografia lateral do cardápio** — Melhor para: fine dining, restaurantes omakase e cardápios sazonais. Vibe: editorial e imersiva. (Fonte: FineDine /menu) | Tags: [Mídia: Foto-Crítica] [Scroll: Sticky] [Fundo: Escuro]

#### L2-SPEC-02 — Filtro de alergênicos por grupos de pratos

- **Categoria destino** — `special-modules.md`
- **ID sugerido** — `L2-SPEC-02`
- **Nome do padrão** — Filtro de alergênicos por grupos de pratos
- **Fonte** — [FineDine /menu](https://finedine-template.framer.website/menu)
- **Nichos indicados** — restaurantes com carta extensa, menus sazonais e hospitalidade

##### Requisitos de Mídia e Copy

Dispensa mídia. Use rótulos curtos, orientação em uma frase, nome do prato e marcações objetivas.

##### Ordem obrigatória do DOM

1. H2 e orientação.
2. Controles de restrição e contador.
3. Grupos por categoria com nome do prato e marcações em cada linha.
4. Nota final.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 409 px e margens de 20 px. Opções de 28 px de altura distribuídas em três linhas. Caixa de filtros de cerca de 265 px. Título, filtros e primeiro grupo somam cerca de 737 px antes dos vãos. Seção com cerca de 1937 px, superfície escura e divisórias finas.

##### Expansão Desktop observada (1024px+ / 1440px)

Área de 1252 px com três trilhas de aproximadamente 391 px. Duas trilhas a 1090 e 909 px, uma a 779 px. Resultados coerentes com as faixas CSS em 1200 e 810 px. Caixa de filtros de cerca de 190 px no desktop.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Expor estado pressionado, contador e agrupamento. Separar dados do prato e orientação geral.
- **Adaptáveis** — Paleta, tipografia e rótulos das categorias.

##### Animações & Interações observadas

- Clique em Raw fish → a opção ficou pressionada e o contador caiu de 27 para 18. Segundo clique → opção desmarcada e contador voltou a 27.

##### Regras Anti-Slop específicas daquela seção

- Atualizar as marcações sempre que o preparo mudar. Manter a consulta à equipe explícita ao lado dos resultados.

##### Linha pronta para o `INDEX.md`

- **L2-SPEC-02 | Filtro de alergênicos por grupos de pratos** — Melhor para: restaurantes com carta extensa, menus sazonais e hospitalidade. Vibe: informativa e discreta. (Fonte: FineDine /menu) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Escuro]
