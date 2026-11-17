# Lote 1 — Referências web

## Páginas inspecionadas

| Site | URL inspecionada | Desktop | Largura estreita | Overflow horizontal estreito |
| --- | --- | --- | --- | --- |
| Spector | https://spector.framer.website/ | 1348 × 936 px CSS | 449 × 312 px CSS | 449 = 449 |
| Alter | https://alter.framer.photos/ | 1348 × 936 px CSS | 449 × 312 px CSS | 449 = 449 |
| Billie | https://billie-duvalle.framer.website/ | 1348 × 936 px CSS | 449 × 312 px CSS | 449 = 449 |
| Ligatra | https://only-instance-526558.framer.app/ | 1348 × 936 px CSS | 449 × 312 px CSS | 449 = 449 |

O botão **Show Preview** do Marketplace abriu o Billie em uma aba própria. O iframe remanescente no Marketplace estava oculto e sem `src`.

Método: Chrome virtual, zoom, capturas pontuais, rolagem amostrada até o fim e leitura do DOM renderizado. As dimensões da tabela são `clientWidth × clientHeight` e a coluna de overflow compara `scrollWidth` com `clientWidth` no elemento raiz. A altura reduzida pelo zoom só descreve o ambiente de teste. A primeira dobra em 812 px é uma estimativa baseada no DOM. Mouse disponível nas duas larguras. Toque, 375 px e 1440 px ficaram fora da medição. Um documento sem overflow horizontal na raiz ainda pode ter mídia recortada dentro de um componente.

As folhas de estilo dos quatro sites contêm faixas com limites em 810 e 1200 px. Ligatra também contém regras com limite em 1440 px. As fichas descrevem os estados efetivamente comparados em 449 e 1348 px. O limiar de mudança de cada componente não foi isolado pixel a pixel. A ordem a seguir é a estrutura obrigatória para reutilizar o padrão, sintetizada a partir dos elementos e da composição inspecionados.

## Fichas por categoria

### `heroes.md`

#### L1-HERO-01 — Retrato integral com manifesto sobreposto

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L1-HERO-01`
- **Nome do padrão** — Retrato integral com manifesto sobreposto
- **Fonte** — [Spector](https://spector.framer.website/)
- **Nichos indicados** — estúdios de branding, agências criativas, produtoras de moda

##### Ordem obrigatória do DOM

1. Identificação editorial, H1 e localização.
2. Ano e lista curta de disciplinas.
3. Manifesto em linhas e marca lateral opcional.
4. Camada de retrato e textura, posicionada atrás do conteúdo.

##### Comportamento Mobile-First observado de fato (449 px)

Blocos de conteúdo empilhados, margem lateral de 16 px e H1 de 48 px. O retrato cobre o palco com recorte fechado. A caixa superior vai de y=120 a y≈551, com a lista de disciplinas terminando perto de y=511. O manifesto continua no DOM. A caixa externa usa `100vh` e recorte, por isso parte do conteúdo interno ultrapassa o palco no teste com 312 px de altura. Em uma tela de 812 px, os blocos superiores medidos têm espaço geométrico para caber se mantiverem suas dimensões. A integração do manifesto completo nessa altura não foi confirmada.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, o palco mede 1348 × 936 px, com retrato sangrado e grade fina sobre fundo próximo de #050609. Dois agrupamentos superiores partem da margem esquerda de 24 px e da região central. O manifesto em vermelho e creme ocupa a base esquerda e a marca com código vertical ocupa a borda direita. O H1 usa Plus Jakarta Sans a 48 px.

##### Animações & Interações observadas

- [NÃO OBSERVADO] para animação específica do retrato ou para hover na seção.

##### Regras Anti-Slop específicas daquela seção

- Escolher um único retrato com espaço para o título e recorte dirigido pelo rosto.
- Manter as disciplinas em um bloco de leitura distinto do manifesto e testar contraste por linha sobre a fotografia.
- Conferir o limite do recorte em telas estreitas antes de travar a altura em `100vh`.

##### Linha pronta para o `INDEX.md`

- **L1-HERO-01 | Retrato integral com manifesto sobreposto** — Melhor para: estúdios de branding, agências criativas e produtoras de moda. Vibe: editorial, técnica e provocadora. (Fonte: Spector)

#### L1-HERO-02 — Retrato com identidade em transformação

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L1-HERO-02`
- **Nome do padrão** — Retrato com identidade em transformação
- **Fonte** — [Alter](https://alter.framer.photos/)
- **Nichos indicados** — portfólios autorais, direção criativa, motion design

##### Ordem obrigatória do DOM

1. H1 semântico acessível.
2. Nome visual em duas camadas e retrato central.
3. Moldura de mira, estado do personagem e texto de apresentação.
4. Indicador de transformação e pista de rolagem onde houver espaço.

##### Comportamento Mobile-First observado de fato (449 px)

Palco sticky de 449 × 312 px na janela de teste, dentro de um trecho de cerca de 562 px. O retrato medido tem 137 × 243 px, proporção aproximada de 9:16. Nome contornado e sobrenome laranja se sobrepõem à foto. A intro aparece dentro da moldura junto aos estados. O palco acompanha a altura da janela e o trecho usa `180vh`. Em uma tela de 812 px o palco inicial tenderia a ocupar a primeira dobra, enquanto a transformação completa teria um trecho de cerca de 1462 px. A relação de sobreposição nessa altura é uma estimativa.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, retrato de 474 × 842 px no eixo central. Nome contornado à esquerda e sobrenome maciço laranja à direita. Intro de 300 px de largura no canto inferior esquerdo e estado no inferior direito. A moldura traça só os cantos. O trecho de 2059 px corresponde a cerca de 2,2 alturas da janela. Fundo preto, retrato monocromático, Switzer na apresentação e detalhe monoespaçado nos dados.

##### Animações & Interações observadas

- Rolagem → palco sticky → estado visível mudou de `CIVILIAN` para `TRANSFORMING`, com avanço da barra laranja e troca de letras na composição do nome. Duração e curva [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Reservar o laranja para o nome ativo e o progresso. A foto precisa permanecer reconhecível em ambos os estados.
- Posicionar os indicadores nos limites da moldura e manter apenas os dados que narram a transformação.
- Dar ao H1 um texto legível por tecnologia assistiva mesmo quando a identidade visual estiver repartida em camadas.

##### Linha pronta para o `INDEX.md`

- **L1-HERO-02 | Retrato com identidade em transformação** — Melhor para: portfólios autorais, direção criativa e motion design. Vibe: cinematográfica, tecnológica e laranja de alto contraste. (Fonte: Alter)

#### L1-HERO-03 — Nome monumental com janela de projetos

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L1-HERO-03`
- **Nome do padrão** — Nome monumental com janela de projetos
- **Fonte** — [Billie](https://billie-duvalle.framer.website/)
- **Nichos indicados** — portfólios individuais, direção de arte, estúdios de embalagem

##### Ordem obrigatória do DOM

1. Identidade no cabeçalho e navegação da página.
2. Nome principal, com equivalente textual acessível se for desenhado como imagem.
3. Janela de imagens de projetos entre as linhas do nome na versão estreita.
4. Mini bio em caixa alta.

##### Comportamento Mobile-First observado de fato (449 px)

Nome dividido em duas linhas com mídia central. A janela medida em uma amostra tinha 240 × 130 px, cerca de 1,85:1. No teste, a bio sobrepôs parte da linha inferior e os botões fixos promocionais cobriram parte da mídia e do texto. O palco externo usa `100vh` e começa cerca de 10 px abaixo do topo. Uma janela de 812 px dá cerca de 500 px adicionais ao palco, mas o arranjo sobreposto não permite garantir um encaixe confortável sem testar essa altura.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, nome branco em uma linha sobre fundo quase preto, ocupando caixa de aproximadamente 924 × 137 px. Cabeçalho distribui assinatura, três links e ano em eixo horizontal. Bio central em três linhas perto da base. Na captura inicial, o nome domina o palco e a mídia de projeto não aparecia no centro.

##### Animações & Interações observadas

- Quadros diferentes apareceram na janela de imagens em capturas distintas, e as dimensões internas variaram. O gatilho e o encadeamento completo ficaram [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Preservar a escala do nome e usar a mini bio para informar especialidade e localização.
- Manter as mídias da janela vinculadas ao portfólio real.
- Reservar zonas independentes para a bio e a linha inferior quando a viewport for baixa. Evitar controles promocionais que cubram a composição.

##### Linha pronta para o `INDEX.md`

- **L1-HERO-03 | Nome monumental com janela de projetos** — Melhor para: portfólios individuais, direção de arte e estúdios de embalagem. Vibe: minimalista, tipográfica e autoral. (Fonte: Billie)

#### L1-HERO-04 — Chamada de produto com montagem na rolagem

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L1-HERO-04`
- **Nome do padrão** — Chamada de produto com montagem na rolagem
- **Fonte** — [Ligatra](https://only-instance-526558.framer.app/)
- **Nichos indicados** — hamburguerias, marcas de alimentação, lançamentos de produto

##### Ordem obrigatória do DOM

1. Identificação do produto.
2. H1 e descrição de ingredientes.
3. CTA primário de pedido.
4. Seção visual separada com palco sticky e camadas fotográficas do produto.

##### Comportamento Mobile-First observado de fato (449 px)

Intro de 342 px, margem de 20 px e H1 Bowlby One de 60 px. A descrição ocupa duas linhas e o botão amarelo mede 127 × 52 px, terminando em y≈330. A montagem começa em y≈342. A caixa inicial do hambúrguer no DOM foi medida perto de y=486–640, com 125 × 154 px. A parte textual e o CTA caberiam na primeira dobra de 812 px pelas medidas. A mídia começaria nessa dobra, mas a posição exata depende do palco sticky e do estado da rolagem.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, intro com 466 px de altura e título de 144 px com gradiente de amarelo para laranja sobre #0b0806. CTA em cápsula de 132 × 52 px. Na sequência, a caixa do hambúrguer mede cerca de 447 × 551 px em uma das medições. A captura mostra os ingredientes separados em profundidade vertical abaixo do CTA.

##### Animações & Interações observadas

- Rolagem → palco da montagem → ingredientes aparecem em estados com espaçamentos verticais distintos. A distância de rolagem de cada camada e a curva ficaram [NÃO OBSERVADO].
- CTA de pedido identificado no DOM. Transição específica de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Colocar a ação de pedido antes do trecho sticky.
- Usar recortes fotográficos coerentes em luz, escala e eixo vertical para que os ingredientes leiam como o mesmo produto.
- Fazer a cor de destaque acompanhar a paleta da fotografia. Manter um único CTA principal na composição.

##### Linha pronta para o `INDEX.md`

- **L1-HERO-04 | Chamada de produto com montagem na rolagem** — Melhor para: hamburguerias, marcas de alimentação e lançamentos de produto. Vibe: pop, tátil e apetitosa. (Fonte: Ligatra)

### `showcase-media.md`

#### L1-SHOW-01 — Mosaico compacto de imagens com legenda embutida

- **Categoria destino** — `showcase-media.md`
- **ID sugerido** — `L1-SHOW-01`
- **Nome do padrão** — Mosaico compacto de imagens com legenda embutida
- **Fonte** — [Spector](https://spector.framer.website/)
- **Nichos indicados** — portfólios de branding, campanhas, fotografia comercial

##### Ordem obrigatória do DOM

1. Título e linha de curadoria.
2. Galeria de links de projetos. Cada link contém imagem, título e cliente.
3. Link para a coleção completa.

##### Comportamento Mobile-First observado de fato (449 px)

Uma coluna e três projetos visíveis, com margens de 8 px. Cada imagem mede 433 × 244 px, aproximadamente 16:9, com cantos de 8 px e intervalo vertical de 8 px. Depois das três imagens aparece o link para mais projetos.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, o DOM expôs seis links em duas filas de três. Uma medição em repouso retornou quadros de 353 × 358 px com cerca de 3 px de intervalo. Em outra posição da rolagem apareceu uma distribuição visual mais larga, com larguras desiguais. O mecanismo exato dessa mudança ficou sem confirmação. Preto e intervalos estreitos deixam as cores das imagens definirem cada quadro. Títulos e clientes aparecem sobre a mídia.

##### Animações & Interações observadas

- O ponteiro sobre um quadro mostrou o destino do link na barra de status. A transição visual própria de hover e o gatilho da mudança de composição ficaram [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Priorizar fotos com paletas distintas e enquadramentos que funcionem tanto próximos do quadrado quanto em 16:9.
- Usar escurecimento localizado para legibilidade de título e cliente.
- Selecionar os projetos que entram na versão estreita e conservar acesso claro à coleção inteira.

##### Linha pronta para o `INDEX.md`

- **L1-SHOW-01 | Mosaico compacto de imagens com legenda embutida** — Melhor para: portfólios de branding, campanhas e fotografia comercial. Vibe: gráfica, densa e contrastante. (Fonte: Spector)

#### L1-SHOW-02 — Pares editoriais alternados de projetos

- **Categoria destino** — `showcase-media.md`
- **ID sugerido** — `L1-SHOW-02`
- **Nome do padrão** — Pares editoriais alternados de projetos
- **Fonte** — [Billie](https://billie-duvalle.framer.website/)
- **Nichos indicados** — estúdios de branding, design de embalagem, portfólios de direção de arte

##### Ordem obrigatória do DOM

1. Título da seleção.
2. Seis projetos em ordem editorial. Cada item agrupa mídia vinculada, título e categoria.
3. Continuação para a próxima seção após o último par.

##### Comportamento Mobile-First observado de fato (449 px)

Os seis projetos se empilham na mesma sequência, em uma coluna de 409 px com margens de 20 px. As mídias medem aproximadamente 409 × 305–320 px. As legendas ficam abaixo e a distância entre caixas consecutivas é de cerca de 48 px nos primeiros pares. A mídia mantém borda reta.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, área útil de 1252 px com margens de 48 px. Colunas de 385 e 819 px, cerca de 32/68 da largura descontado o vão de 48 px. A coluna dominante alterna direita, esquerda, direita. A mídia pequena fica perto de 4:3 e a grande perto de 1,28:1 nos primeiros pares. Títulos e categorias permanecem externos às imagens sobre fundo escuro.

##### Animações & Interações observadas

- Os projetos estão vinculados no DOM. Uma reação visual específica ao hover do cartão ficou [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Alternar o peso da imagem por par e manter o alinhamento superior dos dois projetos.
- Usar o mesmo tratamento de legenda em ambas as larguras.
- Preservar a ordem de leitura quando o grid virar uma pilha. Evitar alturas iguais forçadas que apaguem a diferença de peso editorial.

##### Linha pronta para o `INDEX.md`

- **L1-SHOW-02 | Pares editoriais alternados de projetos** — Melhor para: estúdios de branding, design de embalagem e portfólios de direção de arte. Vibe: editorial, espaçada e centrada na fotografia. (Fonte: Billie)

### `conversion-closing.md`

#### L1-CONV-01 — Fechamento de contato com palco e email visível

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L1-CONV-01`
- **Nome do padrão** — Fechamento de contato com palco e email visível
- **Fonte** — [Alter](https://alter.framer.photos/)
- **Nichos indicados** — designers independentes, consultorias criativas, pequenos estúdios

##### Ordem obrigatória do DOM

1. Título semântico de contato e link para a página de contato.
2. Estado de disponibilidade e convite curto.
3. Email clicável.
4. Links sociais.

##### Comportamento Mobile-First observado de fato (449 px)

Palco escuro de 449 × 640 px. A faixa de contato começa a cerca de 435 px do início da seção, ocupa 409 px e tem margem de 20 px. Email em Switzer a 22 px. Os quatro links sociais aparecem depois, em linha, com caixas de 44 px de altura e fonte monoespaçada de 11 px. A área do link de fundo mede a seção inteira no DOM.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, palco de 936 px de altura. O convite e o email estão próximos ao canto inferior esquerdo, com margem de 40 px e email de cerca de 35 px com sublinhado laranja. Redes no canto oposto. O conteúdo de contato continua legível mesmo quando a região central fotografada aparece vazia. O título semântico de contato tem caixa de 1 × 1 px.

##### Animações & Interações observadas

- O email usa `mailto:` e há um link absoluto no palco para a página de contato. Animação do fundo e reação visual de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Dar ao email peso visual suficiente para funcionar como ação principal.
- Usar um endereço real no projeto final e manter as redes como ações secundárias.
- Garantir que o link amplo do palco preserve acesso por mouse e teclado aos links de email e redes.

##### Linha pronta para o `INDEX.md`

- **L1-CONV-01 | Fechamento de contato com palco e email visível** — Melhor para: designers independentes, consultorias criativas e pequenos estúdios. Vibe: sóbria, técnica e espaçada. (Fonte: Alter)

#### L1-CONV-02 — Comparação de combos com ação por opção

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L1-CONV-02`
- **Nome do padrão** — Comparação de combos com ação por opção
- **Fonte** — [Ligatra](https://only-instance-526558.framer.app/)
- **Nichos indicados** — hamburguerias, delivery, cardápios com combos

##### Ordem obrigatória do DOM

1. Título de escolha.
2. Lista de combos. Cada item contém imagem, etiqueta curta, nome, descrição, preço, ação de pedido e lista de itens incluídos.

##### Comportamento Mobile-First observado de fato (449 px)

Três cartões em uma coluna de 409 px com margem de 20 px. Título Bowlby One de 34 px em duas linhas. Cada imagem mede 365 × 200 px, aproximadamente 1,83:1. O CTA mede cerca de 180 × 52 px. Os cartões usam planos largos em marrom muito escuro, com cantos arredondados e foto recortada do produto.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, três colunas iguais de cerca de 380 px dentro de uma faixa de 1180 px, com vãos de cerca de 20 px. Título de 52 px. Imagens de 324 × 230 px, cerca de 1,41:1. Chamadas amarelas de 188 × 52 px. Preços e botões alinhados entre as três opções na amostra desktop.

##### Animações & Interações observadas

- Os três CTAs apontam para um endereço de demonstração no DOM. Fluxo de pedido e mudança visual específica ao hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar o mesmo tamanho aparente e o mesmo eixo para as fotos dos produtos.
- Aplicar a mesma ordem de informações em todos os cartões para facilitar a comparação de preço e composição.
- Usar rótulos curtos que indiquem uma diferença real e trocar o destino demonstrativo pelo pedido da opção correspondente.

##### Linha pronta para o `INDEX.md`

- **L1-CONV-02 | Comparação de combos com ação por opção** — Melhor para: hamburguerias, delivery e cardápios com combos. Vibe: quente, direta e gastronômica. (Fonte: Ligatra)
