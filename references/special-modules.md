# special-modules.md

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

#### L3-SPEC-01 — Cardápio diário em cartões sticky sobrepostos

- **Categoria destino** — `special-modules.md`
- **ID sugerido** — `L3-SPEC-01`
- **Nome do padrão** — Cardápio diário em cartões sticky sobrepostos
- **Fonte** — [Ruota](https://ruota-template.framer.website/)
- **Nichos indicados** — cantinas, menus do dia e restaurantes sazonais

##### Requisitos de Mídia e Copy

Uma foto quadrada por prato com corte compatível com máscara circular. Usar nome, descrição de até 12 palavras, preço e horário de preparo quando for relevante.

##### Ordem obrigatória do DOM

1. Título, introdução e link para cardápio completo.
2. Lista de cartões em ordem.
3. Em cada cartão: foto e bloco de horário, nome, descrição e preço.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 409 px com recuo lateral de 20 px. Foto quadrada de cerca de 390 px em máscara circular. Cartões de 606–642 px, com superfícies creme e vermelho e contornos finos. Cada cartão cabe isoladamente em 812 px; a pilha completa exige rolagem.

##### Expansão Desktop observada (1024px+ / 1440px)

Cartões de 1252 × 560 px com intervalos de 28 px. Foto e texto ficam lado a lado. A imagem quadrada medida no DOM era 624 × 624 px, com recorte interno na composição visível. CSS de página em 810 e 1200 px; limiar exato da troca de orientação não isolado.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Lista em ordem e foto vinculada ao prato correspondente. Manter preço acessível durante a passagem entre cartões.
- **Adaptáveis** — Tipo de prato, paleta, fontes e pose fotográfica.

##### Animações & Interações observadas

- Rolagem → o primeiro cartão ficou a cerca de 40 px do topo enquanto o segundo se aproximou e passou a cobri-lo. A sobreposição foi confirmada visualmente no desktop.

##### Regras Anti-Slop específicas daquela seção

- Manter os dados essenciais juntos antes da sobreposição. Preparar fotos com enquadramento e escalas comparáveis.

#### L3-SPEC-02 — Lista de pizzas com preços alinhados por tamanho

- **Categoria destino** — `special-modules.md`
- **ID sugerido** — `L3-SPEC-02`
- **Nome do padrão** — Lista de pizzas com preços alinhados por tamanho
- **Fonte** — [Slice Town](https://slice-town-wbs.framer.website/)
- **Nichos indicados** — pizzarias, padarias e cardápios por porção

##### Requisitos de Mídia e Copy

Sem foto por item. Nome curto, descrição de aproximadamente 8–15 palavras e valores de cada tamanho. Ilustrações culinárias periféricas são opcionais.

##### Ordem obrigatória do DOM

1. H2 de cardápio.
2. Grupos de itens, com categoria e nomes dos tamanhos antes das linhas.
3. Em cada linha: nome e descrição, preços na mesma ordem do cabeçalho e separador.

##### Comportamento Mobile-First observado (375px)

Lista empilhada com linha de 393 px. Título e descrição em 243 px, preços em 140 px. Um registro mediu 76 px. A seção completa excede 812 px; o cabeçalho e as primeiras opções cabem. Fundo marrom, contraste ocre nos preços e divisores discretos.

##### Expansão Desktop observada (1024px+ / 1440px)

Grupos de 585 px dentro de uma área maior. Linha útil de 561 px e coluna de preços de 140 px. A descrição e os preços continuam associados na horizontal. A captura de entrada mostra o grupo vegetariano à esquerda. CSS de página em 810 e 1200 px; limiar do agrupamento não isolado.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Ordem dos tamanhos consistente e preços nos mesmos eixos do cabeçalho.
- **Adaptáveis** — Paleta, tipografia, nomes dos grupos e decoração periférica.

##### Animações & Interações observadas

- Clique em Menu → URL passou a `/#menu`. Animação própria de item ou filtro [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Nunca ocultar o tamanho correspondente a um preço. Usar rótulos textuais para distinguir categorias além dos marcadores coloridos.

#### L3-SPEC-03 — Seleção de pratos com miniaturas circulares e preço em destaque

- **Categoria destino** — `special-modules.md`
- **ID sugerido** — `L3-SPEC-03`
- **Nome do padrão** — Seleção de pratos com miniaturas circulares e preço em destaque
- **Fonte** — [Foodee](https://foodee.framer.website/)
- **Nichos indicados** — restaurantes vegetarianos, bistrôs e menus de degustação

##### Requisitos de Mídia e Copy

Fotos com leitura em máscara circular. Nome curto, preço e uma frase de até 10–12 palavras por prato. Selos ocasionais para novidades ou intensidade.

##### Ordem obrigatória do DOM

1. Identificador, título, descrição e link para o menu.
2. Grade de pratos.
3. Em cada item: imagem e selo quando houver, nome, preço e descrição.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 401 px com margens de 24 px. Linhas de 122 px. Imagem quadrada no DOM com 171 px e área visual circular menor. Cabe o cabeçalho e a primeira linha dentro de 812 px contados desde o topo da seção. Fundo claro e preço vermelho.

##### Expansão Desktop observada (1024px+ / 1440px)

Três colunas de cerca de 331 px em 1152 px úteis. A seção usa posição sticky no desktop e posição relativa na variante estreita. A altura desktop medida coincidiu com a viewport. CSS da página em 810 e 1200 px; limiar exato da troca não isolado.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Preço próximo do nome, mesma composição foto–texto em cada item e CTA para o cardápio completo.
- **Adaptáveis** — Paleta, fontes, tamanho visual das fotos e estilo dos selos.

##### Animações & Interações observadas

- Posição sticky confirmada no DOM no desktop. Efeito próprio do hover nos pratos [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar os selos em poucos itens. Evitar que texto longo desalinhe as linhas e desloque o preço para longe do nome.

#### L4-SPEC-01 — Carta por taça ao lado de mesa privativa

- **Categoria destino** — `special-modules.md`
- **ID sugerido** — `L4-SPEC-01`
- **Nome do padrão** — Carta por taça ao lado de mesa privativa
- **Fonte** — [Ruota](https://ruota-template.framer.website/)
- **Nichos indicados** — cantinas, bares de vinho e restaurantes

##### Requisitos de Mídia e Copy

Três rótulos com estilo, origem e preço. Uma foto horizontal para a mesa e cerca de 20–25 palavras por apresentação.

##### Ordem obrigatória do DOM

1. Painel de vinhos com identificador, título, descrição e lista de três linhas.
2. Painel de mesa com foto, título, descrição e link de consulta.

##### Comportamento Mobile-First observado (375px)

Painéis empilhados de 409 px com margens de 20 px, raio de 32 px e alturas de 534 e 503 px. Foto de 369 × 220 px (1,68:1). Cada painel cabe isoladamente em 812 px. Carta sobre fundo vermelho com separadores claros.

##### Expansão Desktop observada (1024px+ / 1440px)

Painéis de 630 e 598 px, cerca de 51/49 da largura combinada, com 752 px de altura e raio de 40 px. Foto da mesa de 518 × 340 px (1,52:1). A carta mantém preço à direita.

##### Invariantes vs. Adaptáveis

- **Invariantes** — A carta e o convite têm ações e informações próprias. Preservar estilo, origem e preço na mesma linha.
- **Adaptáveis** — Paleta, fonte, seleção de vinhos e fotografia.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Usar uma foto da mesa ou sala que pode ser reservada. Manter o preço alinhado mesmo quando o nome do vinho aumentar.

#### L4-SPEC-02 — Linha do tempo de degustação com estimativa de mesa

- **Categoria destino** — `special-modules.md`
- **ID sugerido** — `L4-SPEC-02`
- **Nome do padrão** — Linha do tempo de degustação com estimativa de mesa
- **Fonte** — [Braise](https://braise-dining.framer.website/)
- **Nichos indicados** — menus degustação, experiências guiadas e eventos gastronômicos

##### Requisitos de Mídia e Copy

Uma foto por etapa com recorte retrato, hora e nome do prato. Uma frase curta de ingredientes, harmonização opcional e valores discriminados.

##### Ordem obrigatória do DOM

1. Foto do prato ativo.
2. Título, introdução, hora, ordem e descrição do prato.
3. Controle de etapa com setas e slider.
4. Preço por pessoa, harmonização, quantidade, subtotal e link de reserva.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 409 px com margens de 20 px. Foto de 409 × 512 px (0,80:1). Setas de 44 × 44 px. Imagem e bloco de texto somam cerca de 906 px antes dos controles, ultrapassando uma dobra local de 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Área de 1239 px com foto de 631 px, texto de 526 px e vão de cerca de 82 px. Foto medida em 631 × 730 px. Trilho horizontal abaixo das duas colunas, seguido pela faixa com preços e reserva. Fundo quase preto e destaque âmbar.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Hora, nome e imagem compartilham o mesmo estado ativo. Opções de preço permanecem próximas do total.
- **Adaptáveis** — Número de etapas, cor do trilho, textos e fotografias.

##### Animações & Interações observadas

- Clique em Next course → a etapa ativa mudou. Na amostra posterior apareceu o 3º prato, às 19:50, com nova foto, título e ponto no trilho. Efeito dos ajustes sobre o total [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Oferecer controle por setas e teclado além do arraste. Separar valor por pessoa de total para a mesa.

#### L4-SPEC-03 — Explorador de plantas com abas de tipologia

- **Categoria destino** — `special-modules.md`
- **ID sugerido** — `L4-SPEC-03`
- **Nome do padrão** — Explorador de plantas com abas de tipologia
- **Fonte** — [Skyline Residences](https://skyline-estate.framer.website/)
- **Nichos indicados** — incorporadoras, imobiliárias e empreendimentos residenciais

##### Requisitos de Mídia e Copy

Planta legível por tipologia, foto interna e dados curtos de quartos, banheiros, área interna e terraço. Nome e resumo de uma linha por aba.

##### Ordem obrigatória do DOM

1. Título e introdução.
2. Abas com número, nome e resumo.
3. Painel ativo com identificação, andares, planta, foto, medidas e ações de consulta.

##### Comportamento Mobile-First observado (375px)

Quatro abas em 2 × 2, caixas de aproximadamente 197 × 97 px. Painel empilhado de 409 px. Planta de 377 × 270 px (1,40:1) e foto de 409 × 230 px (1,78:1). A aba e a planta podem aparecer na mesma dobra local; o painel inteiro excede 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Quatro abas de 299 px em linha. Painel de 1268 px com planta de 768 × 550 px e foto de 396 × 260 px. Relação aproximada de 66/34 entre planta e coluna de dados, pelo tamanho medido das mídias. Fundo preto e planta em superfície clara.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Vincular a mesma tipologia a nome, faixa de andares, foto, planta e métricas. Tornar a aba ativa identificável.
- **Adaptáveis** — Unidades de medida, tipografia e acabamento fotográfico.

##### Animações & Interações observadas

- Clique em Corner Residence → aba ativa, cabeçalho, faixa de andares e imagens mudaram para a segunda tipologia. Planta e foto foram conferidas no painel.

##### Regras Anti-Slop específicas daquela seção

- Exibir medidas como texto e manter a planta com contraste. Evitar que o estado ativo dependa apenas de cor.

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

#### L6-SPEC-01 — Seletor de procedimentos em três perguntas

- **Categoria destino** — `special-modules.md`
- **ID sugerido** — `L6-SPEC-01`
- **Nome do padrão** — Seletor de procedimentos em três perguntas
- **Fonte** — [Cassian](https://tidy-marketing-173692.framer.app/)
- **Nichos indicados** — clínicas e catálogos consultivos

##### Requisitos de Mídia e Copy

Dispensa foto. Pergunta curta por etapa e rótulos de até quatro palavras.

##### Ordem obrigatória do DOM

1. Identificador e número da etapa.
2. Resumo editável das escolhas anteriores quando preenchido.
3. Pergunta, botões e indicação de progresso.

##### Comportamento Mobile-First observado (375px)

Região útil de 409 × 428 px na primeira etapa. Duas trilhas de cerca de 148 e 229 px. Botões com 44 px de altura. A caixa de 572 px cabe em uma dobra local de 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Caixa de 1252 px e área interativa de 1124 px. Trilhas de aproximadamente 353 e 707 px, com 64 px entre elas. Pergunta e alternativas ficam na área maior.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Estado atual, título da pergunta e opção de voltar permanecem juntos.
- **Adaptáveis** — Rótulos, estilo dos botões e quantidade de opções por pergunta.

##### Animações & Interações observadas

- Clique em Face → mudou para etapa 2 de 3, mostrou a seleção anterior e apresentou três novas opções.

##### Regras Anti-Slop específicas daquela seção

- Usar as escolhas para orientar a navegação por conteúdo. Identificar com clareza a etapa e a forma de editar a resposta.

#### L6-SPEC-02 — Comparador de duas imagens com divisor operável

- **Categoria destino** — `special-modules.md`
- **ID sugerido** — `L6-SPEC-02`
- **Nome do padrão** — Comparador de duas imagens com divisor operável
- **Fonte** — [Cassian](https://tidy-marketing-173692.framer.app/)
- **Nichos indicados** — clínicas, fotografia e projetos de restauração

##### Requisitos de Mídia e Copy

Duas imagens registradas com perspectiva e iluminação equivalentes. Rótulos curtos, intervalo entre capturas e nota de contexto.

##### Ordem obrigatória do DOM

1. Comparador com duas camadas, rótulos e controle deslizante.
2. Bloco de resultados com título, caso, metadados e nota.
3. Link para coleção completa.

##### Comportamento Mobile-First observado (375px)

Pilha com comparador de 409 × 438 px e texto de 409 × 451 px. As duas caixas já somam 889 px antes dos respiros. Controle de 44 × 44 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Comparador ao lado do texto em faixa de 1348 px. Bloco editorial de 482 px. As imagens internas mediram 674 × 843 px em uma amostra; a moldura visível recorta as camadas.

##### Invariantes vs. Adaptáveis

- **Invariantes** — As duas imagens compartilham alinhamento e o controle informa sua posição.
- **Adaptáveis** — Tipografia, cor de borda e formato dos rótulos.

##### Animações & Interações observadas

- Seta direita no slider → valor acessível passou de 50 para 55. O caso fotografado no template é uma renderização identificada na página.

##### Regras Anti-Slop específicas daquela seção

- Manter os rótulos visíveis e evitar mudança de escala entre as duas imagens. Oferecer teclado além do ponteiro.
