# heroes.md

#### L1-HERO-01 — Retrato integral com manifesto sobreposto

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L1-HERO-01`
- **Nome do padrão** — Retrato integral com manifesto sobreposto
- **Fonte** — [Spector](https://spector.framer.website/)
- **Nichos indicados** — estúdios de branding, agências criativas, produtoras de moda

**Evidência histórica** — Lote 1. Desktop 1348 × 936 px CSS; estreito 449 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Retrato único com área livre para sobrepor o manifesto. Usar título curto, localização e uma lista breve de disciplinas.

##### Ordem obrigatória do DOM

1. Identificação editorial, H1 e localização.
2. Ano e lista curta de disciplinas.
3. Manifesto em linhas e marca lateral opcional.
4. Camada de retrato e textura, posicionada atrás do conteúdo.

##### Comportamento em largura estreita

Blocos de conteúdo empilhados, margem lateral de 16 px e H1 de 48 px. O retrato cobre o palco com recorte fechado. A caixa superior vai de y=120 a y≈551, com a lista de disciplinas terminando perto de y=511. O manifesto continua no DOM. A caixa externa usa `100vh` com recorte. Em telas baixas, parte do conteúdo interno pode ultrapassar o palco. Em uma tela de 812 px, os blocos superiores medidos têm espaço geométrico para caber se mantiverem suas dimensões. A integração do manifesto completo nessa altura não foi confirmada.

##### Comportamento em desktop

A 1348 px, o palco mede 1348 × 936 px, com retrato sangrado e grade fina sobre fundo próximo de #050609. Dois agrupamentos superiores partem da margem esquerda de 24 px e da região central. O manifesto em vermelho e creme ocupa a base esquerda e a marca com código vertical ocupa a borda direita. O H1 usa Plus Jakarta Sans a 48 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Preservar identificação, disciplinas e manifesto sobre as camadas de retrato e textura.
- **Adaptáveis** — Fotografia, paleta e tipografia do projeto.

##### Animações & Interações observadas

- [NÃO OBSERVADO] para animação específica do retrato ou para hover na seção.

##### Regras Anti-Slop específicas daquela seção

- Escolher um único retrato com espaço para o título e recorte dirigido pelo rosto.
- Manter as disciplinas em um bloco de leitura distinto do manifesto e testar contraste por linha sobre a fotografia.
- Conferir o limite do recorte em telas estreitas antes de travar a altura em `100vh`.

##### Direção de arte e aplicação

[INFERIDO] **Sobreposição.** Manifesto e retrato competem pela mesma área; reserve espaço negativo no recorte.

#### L1-HERO-02 — Retrato com identidade em transformação

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L1-HERO-02`
- **Nome do padrão** — Retrato com identidade em transformação
- **Fonte** — [Alter](https://alter.framer.photos/)
- **Nichos indicados** — portfólios autorais, direção criativa, motion design

**Evidência histórica** — Lote 1. Desktop 1348 × 936 px CSS; estreito 449 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Retrato vertical reconhecível entre os estados e nome em duas camadas. Manter apresentação e estados curtos.

##### Ordem obrigatória do DOM

1. H1 semântico acessível.
2. Nome visual em duas camadas e retrato central.
3. Moldura de mira, estado do personagem e texto de apresentação.
4. Indicador de transformação e pista de rolagem onde houver espaço.

##### Comportamento em largura estreita

Palco sticky de largura total na variante estreita. O retrato medido tem 137 × 243 px, proporção aproximada de 9:16. Nome contornado e sobrenome laranja se sobrepõem à foto. A intro aparece dentro da moldura junto aos estados. O palco acompanha a altura da janela e o trecho usa `180vh`. Em uma tela de 812 px o palco inicial tenderia a ocupar a primeira dobra, enquanto a transformação completa teria um trecho de cerca de 1462 px. A relação de sobreposição nessa altura é uma estimativa.

##### Comportamento em desktop

A 1348 px, retrato de 474 × 842 px no eixo central. Nome contornado à esquerda e sobrenome maciço laranja à direita. Intro de 300 px de largura no canto inferior esquerdo e estado no inferior direito. A moldura traça só os cantos. O trecho de 2059 px corresponde a cerca de 2,2 alturas da janela. Fundo preto, retrato monocromático, Switzer na apresentação e detalhe monoespaçado nos dados.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Conservar H1 acessível, palco sticky, retrato no eixo e mudança de estado na rolagem.
- **Adaptáveis** — Foto, cor de destaque, tipografia e texto dos estados.

##### Animações & Interações observadas

- Rolagem → palco sticky → estado visível mudou de `CIVILIAN` para `TRANSFORMING`, com avanço da barra laranja e troca de letras na composição do nome. Duração e curva [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Reservar o laranja para o nome ativo e o progresso. A foto precisa permanecer reconhecível em ambos os estados.
- Posicionar os indicadores nos limites da moldura e manter apenas os dados que narram a transformação.
- Dar ao H1 um texto legível por tecnologia assistiva mesmo quando a identidade visual estiver repartida em camadas.

##### Direção de arte e aplicação

[INFERIDO] **Palco sequencial.** A transformação só ajuda se cada estado acrescentar informação; mantenha um retrato estático como alternativa.

#### L1-HERO-03 — Nome monumental com janela de projetos

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L1-HERO-03`
- **Nome do padrão** — Nome monumental com janela de projetos
- **Fonte** — [Billie](https://billie-duvalle.framer.website/)
- **Nichos indicados** — portfólios individuais, direção de arte, estúdios de embalagem

**Evidência histórica** — Lote 1. Desktop 1348 × 936 px CSS; estreito 449 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Nome como elemento tipográfico central, imagens de projetos para a janela e bio curta com especialidade e localização.

##### Ordem obrigatória do DOM

1. Identidade no cabeçalho e navegação da página.
2. Nome principal, com equivalente textual acessível se for desenhado como imagem.
3. Janela de imagens de projetos entre as linhas do nome na versão estreita.
4. Mini bio em caixa alta.

##### Comportamento em largura estreita

Nome dividido em duas linhas com mídia central. A janela medida em uma amostra tinha 240 × 130 px, cerca de 1,85:1. Em baixa altura, a bio sobrepôs parte da linha inferior. O palco externo usa `100vh` e começa cerca de 10 px abaixo do topo. O encaixe confortável do arranjo sobreposto em uma janela de 812 px ainda precisa de verificação.

##### Comportamento em desktop

A 1348 px, nome branco em uma linha sobre fundo quase preto, ocupando caixa de aproximadamente 924 × 137 px. Cabeçalho distribui assinatura, três links e ano em eixo horizontal. Bio central em três linhas perto da base. Na captura inicial, o nome domina o palco e a mídia de projeto não aparecia no centro.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Preservar nome central, janela entre as duas linhas na variante estreita e bio em área própria.
- **Adaptáveis** — Escolha das imagens, cor de fundo e fonte.

##### Animações & Interações observadas

- Quadros diferentes apareceram na janela de imagens em capturas distintas, e as dimensões internas variaram. O gatilho e o encadeamento completo ficaram [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Preservar a escala do nome e usar a mini bio para informar especialidade e localização.
- Manter as mídias da janela vinculadas ao portfólio real.
- Reservar zonas independentes para a bio e a linha inferior quando a viewport for baixa. Evitar controles promocionais que cubram a composição.

##### Direção de arte e aplicação

[INFERIDO] **Janela assimétrica.** Use o nome como âncora e a janela como amostra; nomes longos exigem testar a quebra.

#### L1-HERO-04 — Chamada de produto com montagem na rolagem

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L1-HERO-04`
- **Nome do padrão** — Chamada de produto com montagem na rolagem
- **Fonte** — [Ligatra](https://only-instance-526558.framer.app/)
- **Nichos indicados** — hamburguerias, marcas de alimentação, lançamentos de produto

**Evidência histórica** — Lote 1. Desktop 1348 × 936 px CSS; estreito 449 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Recortes de ingredientes em escala e iluminação coerentes. Nome do produto, título curto, uma frase de descrição e CTA.

##### Ordem obrigatória do DOM

1. Identificação do produto.
2. H1 e descrição de ingredientes.
3. CTA primário de pedido.
4. Seção visual separada com palco sticky e camadas fotográficas do produto.

##### Comportamento em largura estreita

Intro de 342 px, margem de 20 px e H1 Bowlby One de 60 px. A descrição ocupa duas linhas e o botão amarelo mede 127 × 52 px, terminando em y≈330. A montagem começa em y≈342. A caixa inicial do hambúrguer no DOM foi medida perto de y=486–640, com 125 × 154 px. A parte textual e o CTA caberiam na primeira dobra de 812 px pelas medidas. A mídia começaria nessa dobra, mas a posição exata depende do palco sticky e do estado da rolagem.

##### Comportamento em desktop

A 1348 px, intro com 466 px de altura e título de 144 px com gradiente de amarelo para laranja sobre #0b0806. CTA em cápsula de 132 × 52 px. Na sequência, a caixa do hambúrguer mede cerca de 447 × 551 px em uma das medições. A captura mostra os ingredientes separados em profundidade vertical abaixo do CTA.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter identificação, título, descrição e CTA antes do palco sticky com camadas ordenadas.
- **Adaptáveis** — Produto, fotos, cores e fontes.

##### Animações & Interações observadas

- Rolagem → palco da montagem → ingredientes aparecem em estados com espaçamentos verticais distintos. A distância de rolagem de cada camada e a curva ficaram [NÃO OBSERVADO].
- CTA de pedido identificado no DOM. Transição específica de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Colocar a ação de pedido antes do trecho sticky.
- Usar recortes fotográficos coerentes em luz, escala e eixo vertical para que os ingredientes leiam como o mesmo produto.
- Fazer a cor de destaque acompanhar a paleta da fotografia. Manter um único CTA principal na composição.

##### Direção de arte e aplicação

[INFERIDO] **Montagem sequencial.** Vale quando a decomposição explica o produto; preserve uma imagem montada para leitura direta.

#### L7-HERO-01 — Painel editorial com torre recortada atravessando a base

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L7-HERO-01`
- **Nome do padrão** — Painel editorial com torre recortada atravessando a base
- **Fonte** — [Caldren](https://caldren.framer.website/)
- **Nichos indicados** — incorporadoras e imóveis autorais

**Evidência histórica** — Lote 7. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1363 = 1363 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Render vertical recortado da torre e fundo atmosférico. Título de duas linhas largas ou três estreitas, apresentação de até duas frases e CTA curto.

##### Ordem obrigatória do DOM

1. Camada de céu.
2. Identificador institucional.
3. Painel com navegação quando aplicável, introdução e CTA, ações auxiliares e headline em sobreposição visual.
4. Camada da torre e anotação de imóvel na variante larga.

##### Comportamento em largura estreita

Fundo misto. Céu azul envolve painel branco de 417 × 588 px, com margem de 16 px. H1 de 377 × 133 px. A camada da torre começa por volta de y=449 e mede 449 × 400 px. Seção de 789 px, com a camada final projetada até cerca de y=849. O conteúdo do painel cabe pelo DOM, mas a composição inteira não termina dentro de 812 px na geometria medida.

##### Comportamento em desktop

Fundo misto com painel branco de 1235 × 853 px, margem de 64 px e céu azul a toda largura. H1 de 1235 × 201 px em caixa central, torre sobreposta e base fotográfica sangrada. Introdução e CTA à esquerda, anotação e conteúdo secundário à direita. Seção sticky de 1240 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter o título na área branca e a torre cruzando a base sem cobrir o CTA. Preservar uma ação primária legível independentemente da imagem.
- **Adaptáveis** — Cor do céu e do painel, fontes, torre, textos e ações auxiliares.

##### Animações & Interações observadas

- Posição sticky verificada no DOM. Transição precisa das camadas e abertura do showreel [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- A torre precisa ser um recorte com escala legível. Tratar a anotação como dado do imóvel e garantir contraste do título quando a mídia avançar.

##### Direção de arte e aplicação

[INFERIDO] **Sobreposição.** A torre atravessa a borda e conecta as superfícies; reserve um recorte com silhueta reconhecível.

#### L7-HERO-02 — Abertura B2B clara com carrossel de imagem lateral

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L7-HERO-02`
- **Nome do padrão** — Abertura B2B clara com carrossel de imagem lateral
- **Fonte** — [Koddam](https://koddam.framer.website/)
- **Nichos indicados** — consultorias B2B, serviços profissionais e imobiliárias

**Evidência histórica** — Lote 7. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Fotografias institucionais com assunto legível em recortes vertical e horizontal. Contexto de uma linha, título de cerca de 7–10 palavras, descrição de até duas frases e ações curtas.

##### Ordem obrigatória do DOM

1. Contexto ou prova verificável, H1 e descrição.
2. Ações primária e secundária.
3. Mídia com indicadores de navegação.

##### Comportamento em largura estreita

Fundo claro, tom próximo de #f6f6f4. Coluna de 419 px com margem de 15 px. H1 de 156 px de altura e CTAs de 40 px. A mídia passa para baixo, 419 × 240 px (1,75:1) com raio de 10 px. CTAs terminam em y≈500 e a foto em y≈790 contando o header. O conteúdo principal tem espaço em 812 px pela geometria medida.

##### Comportamento em desktop

Fundo claro do lado textual e fotografia sangrada até a borda direita. Caixa do texto de 594 × 434 px a partir de x=30. Foto de 620 × 842 px (0,74:1). O texto ocupa aproximadamente a metade esquerda e a mídia cerca de 46% da largura útil.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Texto e ações antecedem a mídia na leitura. A imagem sangra lateralmente na tela larga e se torna uma caixa abaixo do texto no estreito.
- **Adaptáveis** — Fotos, família serifada ou equivalente, cor e hierarquia visual dos CTAs.

##### Animações & Interações observadas

- Foram identificadas quatro mídias e quatro botões de paginação no DOM. Troca manual e autoplay [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar contexto que informe a especialidade. Só manter um selo de reputação quando houver prova verificável.

##### Direção de arte e aplicação

[INFERIDO] **Divisão com carrossel.** O texto fixa a proposta enquanto a mídia varia; foto única basta quando há apenas uma imagem relevante.

#### L7-HERO-03 — Busto escultórico com título dividido e atalhos de serviço

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L7-HERO-03`
- **Nome do padrão** — Busto escultórico com título dividido e atalhos de serviço
- **Fonte** — [Cassian](https://tidy-marketing-173692.framer.app/)
- **Nichos indicados** — clínicas estéticas, estúdios de imagem e marcas de design

**Evidência histórica** — Lote 7. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Busto monocromático recortado, com bordas livres para grafismos. Título curto que aceite divisão sintática, uma frase de apresentação e poucos atalhos.

##### Ordem obrigatória do DOM

1. Camadas decorativas.
2. Headline dividida visualmente.
3. Busto e atalhos de procedimentos, conforme variante.
4. Apresentação, CTA de consulta e dados de contexto.

##### Comportamento em largura estreita

Fundo escuro com linhas finas de contorno. Título em caixa de aproximadamente 350 × 183 px. Busto de 360 × 416 px começa em y≈312. Atalhos de 44 px quebram em duas linhas. CTA de consulta de 409 × 56 px começa em y≈963 e fica abaixo da dobra de 812 px. O palco inteiro mede cerca de 1139 px.

##### Comportamento em desktop

Fundo escuro sólido próximo de #0b0e13. Palco de 1348 × 1000 px, busto central em caixa de 788 × 904 px. Título separado entre os extremos superiores, CTA e introdução na base esquerda e metadados na direita. A imagem é central recortada, sem sangrar toda a largura.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Preservar leitura contínua do título para tecnologia assistiva. Manter o busto como eixo e o CTA em região própria.
- **Adaptáveis** — Paleta escura ou inversão com contraste validado, tipografia, grafismos e tipo de busto.

##### Animações & Interações observadas

- Atalhos de procedimentos identificados no DOM. Reação visual do busto e dos atalhos [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Evitar fragmentar o título sem alternativa semântica. Manter uma rota de consulta visível cedo quando a imagem empurrar a ação para abaixo da dobra.

##### Direção de arte e aplicação

[INFERIDO] **Título dividido.** Busto e texto compartilham o centro; o recorte deve deixar livres atalhos e palavras-chave.

#### L7-HERO-04 — Prato circular no centro da assinatura tipográfica

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L7-HERO-04`
- **Nome do padrão** — Prato circular no centro da assinatura tipográfica
- **Fonte** — [Ruota](https://ruota-template.framer.website/)
- **Nichos indicados** — cantinas, restaurantes autorais e marcas gastronômicas

**Evidência histórica** — Lote 7. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Foto de prato vista de cima, com prato circular integral e recorte limpo. Marca que aceite composição em dois segmentos, chamada de duas linhas e CTAs curtos.

##### Ordem obrigatória do DOM

1. Marca visual em dois segmentos com mídia circular entre eles.
2. Chamada editorial.
3. Ações de reserva e cardápio.

##### Comportamento em largura estreita

Fundo vermelho sólido com texto creme, sem foto sangrada. Hero de 449 × 445 px após header de 72 px. Eixo visual de 409 px com prato de 128 × 128 px. Chamada e botões empilhados de 54 px. A seção termina em y≈517 e cabe em 812 px.

##### Comportamento em desktop

Fundo vermelho sólido. Hero de 1348 × 646 px, com 1252 px úteis e margens de 48 px. Faixa da marca de 496 px de altura, foto circular central e palavras de apoio na base esquerda com CTAs lado a lado à direita. A medição em um estado mostrou caixa do prato de 538 × 538 px, sujeita à transformação.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter a foto entre os segmentos da marca e conservar a ordem mídia, chamada e ações.
- **Adaptáveis** — Cor de superfície, família tipográfica, prato e redação.

##### Animações & Interações observadas

- As caixas da marca e do prato variaram entre estados de captura. Gatilho e trajetória [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar prato com círculo e foco coerentes. Fornecer nome completo acessível para a marca dividida.

##### Direção de arte e aplicação

[INFERIDO] **Medalhão central.** O contorno do prato organiza a assinatura; fotos retangulares sem recorte comprometem a composição.
