# showcase-media.md

#### L1-SHOW-01 — Mosaico compacto de imagens com legenda embutida

- **Categoria destino** — `showcase-media.md`
- **ID sugerido** — `L1-SHOW-01`
- **Nome do padrão** — Mosaico compacto de imagens com legenda embutida
- **Fonte** — [Spector](https://spector.framer.website/)
- **Nichos indicados** — portfólios de branding, campanhas, fotografia comercial

##### Requisitos de Mídia e Copy

Fotos de projetos que aceitem corte quase quadrado e 16:9. Título e cliente curtos por imagem.

##### Ordem obrigatória do DOM

1. Título e linha de curadoria.
2. Galeria de links de projetos. Cada link contém imagem, título e cliente.
3. Link para a coleção completa.

##### Comportamento Mobile-First observado de fato (449 px)

Uma coluna e três projetos visíveis, com margens de 8 px. Cada imagem mede 433 × 244 px, aproximadamente 16:9, com cantos de 8 px e intervalo vertical de 8 px. Depois das três imagens aparece o link para mais projetos.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, o DOM expôs seis links em duas filas de três. Uma medição em repouso retornou quadros de 353 × 358 px com cerca de 3 px de intervalo. Em outra posição da rolagem apareceu uma distribuição visual mais larga, com larguras desiguais. O mecanismo exato dessa mudança ficou sem confirmação. Preto e intervalos estreitos deixam as cores das imagens definirem cada quadro. Títulos e clientes aparecem sobre a mídia.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter título e cliente dentro de cada link de projeto, com acesso à coleção após a galeria.
- **Adaptáveis** — Foto, tratamento de contraste, cor e fonte.

##### Animações & Interações observadas

- O ponteiro sobre um quadro mostrou o destino do link na barra de status. A transição visual própria de hover e o gatilho da mudança de composição ficaram [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Priorizar fotos com paletas distintas e enquadramentos que funcionem tanto próximos do quadrado quanto em 16:9.
- Usar escurecimento localizado para legibilidade de título e cliente.
- Selecionar os projetos que entram na versão estreita e conservar acesso claro à coleção inteira.

#### L1-SHOW-02 — Pares editoriais alternados de projetos

- **Categoria destino** — `showcase-media.md`
- **ID sugerido** — `L1-SHOW-02`
- **Nome do padrão** — Pares editoriais alternados de projetos
- **Fonte** — [Billie](https://billie-duvalle.framer.website/)
- **Nichos indicados** — estúdios de branding, design de embalagem, portfólios de direção de arte

##### Requisitos de Mídia e Copy

Imagens de projetos que aceitem recortes próximos de 4:3. Usar um título e uma categoria por mídia.

##### Ordem obrigatória do DOM

1. Título da seleção.
2. Seis projetos em ordem editorial. Cada item agrupa mídia vinculada, título e categoria.
3. Continuação para a próxima seção após o último par.

##### Comportamento Mobile-First observado de fato (449 px)

Os seis projetos se empilham na mesma sequência, em uma coluna de 409 px com margens de 20 px. As mídias medem aproximadamente 409 × 305–320 px. As legendas ficam abaixo e a distância entre caixas consecutivas é de cerca de 48 px nos primeiros pares. A mídia mantém borda reta.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, área útil de 1252 px com margens de 48 px. Colunas de 385 e 819 px, cerca de 32/68 da largura descontado o vão de 48 px. A coluna dominante alterna direita, esquerda, direita. A mídia pequena fica perto de 4:3 e a grande perto de 1,28:1 nos primeiros pares. Títulos e categorias permanecem externos às imagens sobre fundo escuro.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Preservar pares com domínio alternado no desktop e ordem estável nos itens empilhados.
- **Adaptáveis** — Fotografias, paleta e tipografia das legendas.

##### Animações & Interações observadas

- Os projetos estão vinculados no DOM. Uma reação visual específica ao hover do cartão ficou [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Alternar o peso da imagem por par e manter o alinhamento superior dos dois projetos.
- Usar o mesmo tratamento de legenda em ambas as larguras.
- Preservar a ordem de leitura quando o grid virar uma pilha. Evitar alturas iguais forçadas que apaguem a diferença de peso editorial.

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

#### L3-SHOW-01 — Sequência de cenas com títulos sobre fotografia

- **Categoria destino** — `showcase-media.md`
- **ID sugerido** — `L3-SHOW-01`
- **Nome do padrão** — Sequência de cenas com títulos sobre fotografia
- **Fonte** — [Cafenza](https://cafenza.framer.website/)
- **Nichos indicados** — cafeterias, hotéis e espaços de convivência

##### Requisitos de Mídia e Copy

Quatro imagens que mostrem ambientes e serviços distintos. Um título de até quatro palavras por fotografia.

##### Ordem obrigatória do DOM

1. Identificador e título da seção.
2. Sequência de cartões.
3. Em cada cartão: foto, título sobreposto, máscara e borda interna.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 409 px, margens de 20 px. Imagens de 409 × 250 px (1,64:1), raio de 12 px. Cabe o primeiro painel e seu título em 812 px. A sequência de quatro exige rolagem.

##### Expansão Desktop observada (1024px+ / 1440px)

Faixa de 1308 px com quatro cenas em sequência, mantendo uma imagem por linha. Em uma amostra de entrada, as caixas de imagem renderizadas variaram de 523 × 300 a 916 × 524 px, cerca de 1,75:1. Na captura do painel em foco, a foto se expandiu até perto das margens de 20 px. CSS de página em 810 e 1200 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Título sobre a própria imagem, máscara de contraste e borda interna recuada.
- **Adaptáveis** — Assunto das fotos, cor da máscara e tipografia.

##### Animações & Interações observadas

- A captura inicial mostrou a região clara antes da entrada e a posterior mostrou o painel ocupando a largura útil. Gatilho e curva exatos [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Selecionar cenas que comprovem cada destaque. Reservar área de baixa atividade atrás do texto em todos os recortes.

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

#### L6-SHOW-01 — Catálogo de cortes com sequência fotográfica

- **Categoria destino** — `showcase-media.md`
- **ID sugerido** — `L6-SHOW-01`
- **Nome do padrão** — Catálogo de cortes com sequência fotográfica
- **Fonte** — [Silenus](https://silenus.framer.website/)
- **Nichos indicados** — barbearias, salões e estúdios de beleza

##### Requisitos de Mídia e Copy

Seis fotos em enquadramento vertical e um nome curto por serviço. Introdução em um parágrafo.

##### Ordem obrigatória do DOM

1. Identificador, título e descrição.
2. Sequência de serviços com mídia e nome por item.

##### Comportamento Mobile-First observado (375px)

Área de 409 px e margem de 20 px. Trilha de conteúdo de aproximadamente 3216 px. Imagens internas podem superar o recorte útil, com caixa medida de 491 × 576 px. A sequência excede 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Área de 1268 px. Fotos medidas em grupos de 407 × 480 e 488 × 576 px, mantendo proporção aproximada de 0,85:1. O título e a descrição ocupam grupos distintos no cabeçalho.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Associar cada nome à sua foto e manter organização consistente dos serviços.
- **Adaptáveis** — Direção de foto, tipografia e número de opções.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Mostrar cortes realmente distintos. Preservar o rosto ou a área do corte no recorte estreito.
