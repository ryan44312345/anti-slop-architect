# Lote 7 — Referências web

## Páginas inspecionadas

| Site | URL inspecionada | Desktop | Mobile | Overflow horizontal |
| --- | --- | --- | --- | --- |
| Caldren | https://caldren.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1363 = 1363 · Mobile 449 = 449 |
| Koddam | https://koddam.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Cassian | https://tidy-marketing-173692.framer.app/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Ruota | https://ruota-template.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |

Dimensões em `innerWidth × innerHeight`. Overflow compara `scrollWidth` e `clientWidth` na raiz no estado inicial. A variante estreita foi observada com zoom a 300%, 449 px úteis, sem emulação de toque. Os títulos das fichas seguem o formato do acervo. O encaixe em 812 px é uma estimativa pelo DOM, sem usar a altura do zoom como dobra. Os limiares específicos não foram isolados. Os Lotes 2 a 6 foram conferidos para evitar repetição. Cassian oferece um hero clínico escuro e Ruota usa fundo vermelho saturado. A tag Adaptável representa possibilidade de adaptação, sem alterar o fundo observado.

## Fichas por categoria

### `heroes.md`

#### L7-HERO-01 — Painel editorial com torre recortada atravessando a base

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L7-HERO-01`
- **Nome do padrão** — Painel editorial com torre recortada atravessando a base
- **Fonte** — [Caldren](https://caldren.framer.website/)
- **Nichos indicados** — incorporadoras e imóveis autorais

##### Requisitos de Mídia e Copy

Render vertical recortado da torre e fundo atmosférico. Título de duas linhas largas ou três estreitas, apresentação de até duas frases e CTA curto.

##### Ordem obrigatória do DOM

1. Camada de céu.
2. Identificador institucional.
3. Painel com navegação quando aplicável, introdução e CTA, ações auxiliares e headline em sobreposição visual.
4. Camada da torre e anotação de imóvel na variante larga.

##### Comportamento Mobile-First observado (375px)

Fundo misto. Céu azul envolve painel branco de 417 × 588 px, com margem de 16 px. H1 de 377 × 133 px. A camada da torre começa por volta de y=449 e mede 449 × 400 px. Seção de 789 px, com a camada final projetada até cerca de y=849. O conteúdo do painel cabe pelo DOM, mas a composição inteira não termina dentro de 812 px na geometria medida.

##### Expansão Desktop observada (1024px+ / 1440px)

Fundo misto com painel branco de 1235 × 853 px, margem de 64 px e céu azul a toda largura. H1 de 1235 × 201 px em caixa central, torre sobreposta e base fotográfica sangrada. Introdução e CTA à esquerda, anotação e conteúdo secundário à direita. Seção sticky de 1240 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter o título na área branca e a torre cruzando a base sem cobrir o CTA. Preservar uma ação primária legível independentemente da imagem.
- **Adaptáveis** — Cor do céu e do painel, fontes, torre, textos e ações auxiliares.

##### Animações & Interações observadas

- Posição sticky verificada no DOM. Transição precisa das camadas e abertura do showreel [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- A torre precisa ser um recorte com escala legível. Tratar a anotação como dado do imóvel e garantir contraste do título quando a mídia avançar.

##### Linha pronta para o `INDEX.md`

- **L7-HERO-01 | Painel editorial com torre recortada atravessando a base** — Melhor para: incorporadoras e imóveis autorais. Vibe: imobiliária e cinematográfica. (Fonte: Caldren) | Tags: [Mídia: Foto-Crítica] [Scroll: Sticky] [Fundo: Adaptável]

#### L7-HERO-02 — Abertura B2B clara com carrossel de imagem lateral

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L7-HERO-02`
- **Nome do padrão** — Abertura B2B clara com carrossel de imagem lateral
- **Fonte** — [Koddam](https://koddam.framer.website/)
- **Nichos indicados** — consultorias B2B, serviços profissionais e imobiliárias

##### Requisitos de Mídia e Copy

Fotografias institucionais com assunto legível em recortes vertical e horizontal. Contexto de uma linha, título de cerca de 7–10 palavras, descrição de até duas frases e ações curtas.

##### Ordem obrigatória do DOM

1. Contexto ou prova verificável, H1 e descrição.
2. Ações primária e secundária.
3. Mídia com indicadores de navegação.

##### Comportamento Mobile-First observado (375px)

Fundo claro, tom próximo de #f6f6f4. Coluna de 419 px com margem de 15 px. H1 de 156 px de altura e CTAs de 40 px. A mídia passa para baixo, 419 × 240 px (1,75:1) com raio de 10 px. CTAs terminam em y≈500 e a foto em y≈790 contando o header. O conteúdo principal tem espaço em 812 px pela geometria medida.

##### Expansão Desktop observada (1024px+ / 1440px)

Fundo claro do lado textual e fotografia sangrada até a borda direita. Caixa do texto de 594 × 434 px a partir de x=30. Foto de 620 × 842 px (0,74:1). O texto ocupa aproximadamente a metade esquerda e a mídia cerca de 46% da largura útil.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Texto e ações antecedem a mídia na leitura. A imagem sangra lateralmente na tela larga e se torna uma caixa abaixo do texto no estreito.
- **Adaptáveis** — Fotos, família serifada ou equivalente, cor e hierarquia visual dos CTAs.

##### Animações & Interações observadas

- Foram identificadas quatro mídias e quatro botões de paginação no DOM. Troca manual e autoplay [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar contexto que informe a especialidade. Só manter um selo de reputação quando houver prova verificável.

##### Linha pronta para o `INDEX.md`

- **L7-HERO-02 | Abertura B2B clara com carrossel de imagem lateral** — Melhor para: consultorias B2B, serviços profissionais e imobiliárias. Vibe: corporativa e editorial. (Fonte: Koddam) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Claro]

#### L7-HERO-03 — Busto escultórico com título dividido e atalhos de serviço

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L7-HERO-03`
- **Nome do padrão** — Busto escultórico com título dividido e atalhos de serviço
- **Fonte** — [Cassian](https://tidy-marketing-173692.framer.app/)
- **Nichos indicados** — clínicas estéticas, estúdios de imagem e marcas de design

##### Requisitos de Mídia e Copy

Busto monocromático recortado, com bordas livres para grafismos. Título curto que aceite divisão sintática, uma frase de apresentação e poucos atalhos.

##### Ordem obrigatória do DOM

1. Camadas decorativas.
2. Headline dividida visualmente.
3. Busto e atalhos de procedimentos, conforme variante.
4. Apresentação, CTA de consulta e dados de contexto.

##### Comportamento Mobile-First observado (375px)

Fundo escuro com linhas finas de contorno. Título em caixa de aproximadamente 350 × 183 px. Busto de 360 × 416 px começa em y≈312. Atalhos de 44 px quebram em duas linhas. CTA de consulta de 409 × 56 px começa em y≈963 e fica abaixo da dobra de 812 px. O palco inteiro mede cerca de 1139 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Fundo escuro sólido próximo de #0b0e13. Palco de 1348 × 1000 px, busto central em caixa de 788 × 904 px. Título separado entre os extremos superiores, CTA e introdução na base esquerda e metadados na direita. A imagem é central recortada, sem sangrar toda a largura.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Preservar leitura contínua do título para tecnologia assistiva. Manter o busto como eixo e o CTA em região própria.
- **Adaptáveis** — Paleta escura ou inversão com contraste validado, tipografia, grafismos e tipo de busto.

##### Animações & Interações observadas

- Atalhos de procedimentos identificados no DOM. Reação visual do busto e dos atalhos [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Evitar fragmentar o título sem alternativa semântica. Manter uma rota de consulta visível cedo quando a imagem empurrar a ação para abaixo da dobra.

##### Linha pronta para o `INDEX.md`

- **L7-HERO-03 | Busto escultórico com título dividido e atalhos de serviço** — Melhor para: clínicas estéticas, estúdios de imagem e marcas de design. Vibe: clínica, escultórica e contrastante. (Fonte: Cassian) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Escuro]

#### L7-HERO-04 — Prato circular no centro da assinatura tipográfica

- **Categoria destino** — `heroes.md`
- **ID sugerido** — `L7-HERO-04`
- **Nome do padrão** — Prato circular no centro da assinatura tipográfica
- **Fonte** — [Ruota](https://ruota-template.framer.website/)
- **Nichos indicados** — cantinas, restaurantes autorais e marcas gastronômicas

##### Requisitos de Mídia e Copy

Foto de prato vista de cima, com prato circular integral e recorte limpo. Marca que aceite composição em dois segmentos, chamada de duas linhas e CTAs curtos.

##### Ordem obrigatória do DOM

1. Marca visual em dois segmentos com mídia circular entre eles.
2. Chamada editorial.
3. Ações de reserva e cardápio.

##### Comportamento Mobile-First observado (375px)

Fundo vermelho sólido com texto creme, sem foto sangrada. Hero de 449 × 445 px após header de 72 px. Eixo visual de 409 px com prato de 128 × 128 px. Chamada e botões empilhados de 54 px. A seção termina em y≈517 e cabe em 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Fundo vermelho sólido. Hero de 1348 × 646 px, com 1252 px úteis e margens de 48 px. Faixa da marca de 496 px de altura, foto circular central e palavras de apoio na base esquerda com CTAs lado a lado à direita. A medição em um estado mostrou caixa do prato de 538 × 538 px, sujeita à transformação.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter a foto entre os segmentos da marca e conservar a ordem mídia, chamada e ações.
- **Adaptáveis** — Cor de superfície, família tipográfica, prato e redação.

##### Animações & Interações observadas

- As caixas da marca e do prato variaram entre estados de captura. Gatilho e trajetória [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar prato com círculo e foco coerentes. Fornecer nome completo acessível para a marca dividida.

##### Linha pronta para o `INDEX.md`

- **L7-HERO-04 | Prato circular no centro da assinatura tipográfica** — Melhor para: cantinas, restaurantes autorais e marcas gastronômicas. Vibe: editorial e vermelha saturada. (Fonte: Ruota) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Adaptável]

### `navigation-chrome.md`

#### L7-NAV-01 — Footer institucional com escritórios e assinatura monumental

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L7-NAV-01`
- **Nome do padrão** — Footer institucional com escritórios e assinatura monumental
- **Fonte** — [Caldren](https://caldren.framer.website/)
- **Nichos indicados** — imobiliárias, incorporadoras e grupos com vários escritórios

##### Requisitos de Mídia e Copy

Monograma, assinatura larga, promessa curta de newsletter e três grupos de navegação. Uma linha por escritório quando houver espaço.

##### Ordem obrigatória do DOM

1. Monograma, chamada e inscrição por email.
2. Grupos Explore, Company e Offices.
3. Assinatura tipográfica.
4. Copyright e links sociais e legais.

##### Comportamento Mobile-First observado (375px)

Caixa externa de 662 px de altura e miolo de 409 px com margem de 20 px. Topo empilhado, email e ação permanecem lado a lado. A assinatura mede 397 × 56 px. A faixa final empilha copyright e links. O bloco cabe em 812 px pelas medidas do DOM; a captura do extremo inferior mostrou principalmente o fundo.

##### Expansão Desktop observada (1024px+ / 1440px)

Área interna de 1235 px com marca e inscrição à esquerda e três grupos em 477 px à direita. Assinatura de 1232 × 173 px abaixo. Linha legal horizontal. Fundo com gradiente azul para bege.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Agrupar destinos institucionais e escritórios e manter a leitura legal independente da imagem da assinatura.
- **Adaptáveis** — Gradiente, fontes, monograma, contatos e número de grupos.

##### Animações & Interações observadas

- Campo e botão de inscrição identificados. Envio e efeitos [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Preservar contraste nas duas extremidades do gradiente. Não usar assinatura gigante para substituir links, endereços ou copyright.

##### Linha pronta para o `INDEX.md`

- **L7-NAV-01 | Footer institucional com escritórios e assinatura monumental** — Melhor para: imobiliárias, incorporadoras e grupos com vários escritórios. Vibe: institucional e atmosférica. (Fonte: Caldren) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Adaptável]

#### L7-NAV-02 — Header corporativo com links centrais e menu móvel empilhado

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L7-NAV-02`
- **Nome do padrão** — Header corporativo com links centrais e menu móvel empilhado
- **Fonte** — [Koddam](https://koddam.framer.website/)
- **Nichos indicados** — consultorias, serviços B2B e sites institucionais

##### Requisitos de Mídia e Copy

Marca legível em formato compacto, cinco links curtos na referência e um CTA de contato.

##### Ordem obrigatória do DOM

1. Marca.
2. Grupo de destinos com página ativa.
3. CTA de contato no desktop.
4. Na variante estreita, marca e acionador seguidos pelo painel com links e CTA.

##### Comportamento Mobile-First observado (375px)

Barra branca de 60 px, miolo de 419 px com recuo de 15 px. Fechada mostra apenas marca e ícone. Aberta exibe links em coluna na ordem Home, About, Services, Resources, Pricing, depois Contact Us. A indicação verde da página ativa permanece. O painel branco cobre parte do hero.

##### Expansão Desktop observada (1024px+ / 1440px)

Barra branca de 80 px, miolo de 1288 px e margem de 30 px. Marca à esquerda, cinco links no centro e CTA em cápsula preta à direita. Página ativa em cápsula verde-clara.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter o estado ativo, sequência de links e acesso ao CTA dentro do painel estreito.
- **Adaptáveis** — Cor do estado ativo, fonte, ícone e texto dos links.

##### Animações & Interações observadas

- Clique no hambúrguer → painel branco abriu e apareceu a lista vertical. Segundo clique → painel recolheu. Curva da transição [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Garantir alcance ao último link quando a altura for baixa. Nomear e expor o estado do acionador para leitores de tela.

##### Linha pronta para o `INDEX.md`

- **L7-NAV-02 | Header corporativo com links centrais e menu móvel empilhado** — Melhor para: consultorias, serviços B2B e sites institucionais. Vibe: clara e funcional. (Fonte: Koddam) | Tags: [Mídia: Tipográfico] [Scroll: Sticky] [Fundo: Claro]

#### L7-NAV-03 — Header clínico mínimo com diálogo de catálogo

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L7-NAV-03`
- **Nome do padrão** — Header clínico mínimo com diálogo de catálogo
- **Fonte** — [Cassian](https://tidy-marketing-173692.framer.app/)
- **Nichos indicados** — clínicas com catálogo de serviços e marcas editoriais

##### Requisitos de Mídia e Copy

Marca textual, destinos curtos e CTA de uma palavra ou expressão curta. Categorias e metadados só quando ajudarem a buscar um serviço.

##### Ordem obrigatória do DOM

1. Marca.
2. Links centrais na variante larga.
3. CTA Book.
4. Na variante estreita, acionador.
5. Diálogo com categorias e itens, acesso ao seletor, links de páginas, CTA final e endereço.

##### Comportamento Mobile-First observado (375px)

Barra transparente fixa, caixa de 104 px e linha útil de 72 px. Marca à esquerda, CTA claro e controle de 41 × 32 px à direita. Aberto, o diálogo escuro rolável precede os links institucionais com grupos Face, Breast, Body e Non-surgical, depois acesso ao seletor, páginas, CTA e endereço.

##### Expansão Desktop observada (1024px+ / 1440px)

Barra fixa de 76 px com marca e CTA nos extremos e seis links centrais. Sobre o hero a superfície é escura/transparente. Em outra posição foi observado fundo claro e CTA azul, com contraste reduzido no texto central.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter marca e CTA acessíveis antes de abrir o menu. O diálogo oferece saída explícita e navegação organizada.
- **Adaptáveis** — Tipografia, polaridade da superfície, número de grupos e estilos de metadados.

##### Animações & Interações observadas

- Clique em Open menu → diálogo apareceu, controle passou a expanded e foco entrou no primeiro procedimento. Clique em Close menu → diálogo fechou. Retorno de foco e Escape [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Aplicar foco visível e contraste em todas as superfícies. Reservar a lista agrupada de procedimentos a catálogos que precisem desse nível de navegação.

##### Linha pronta para o `INDEX.md`

- **L7-NAV-03 | Header clínico mínimo com diálogo de catálogo** — Melhor para: clínicas com catálogo de serviços e marcas editoriais. Vibe: clínica e discreta. (Fonte: Cassian) | Tags: [Mídia: Tipográfico] [Scroll: Sticky] [Fundo: Adaptável]

#### L7-NAV-04 — Footer de restaurante com newsletter e dois grupos de links

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L7-NAV-04`
- **Nome do padrão** — Footer de restaurante com newsletter e dois grupos de links
- **Fonte** — [Ruota](https://ruota-template.framer.website/)
- **Nichos indicados** — restaurantes, cantinas, cafés e bares

##### Requisitos de Mídia e Copy

Título, explicação, email e ação de inscrição;Grupo de links de serviço e grupo de redes e mapa;Separador, assinatura da marca e copyright com endereço

##### Ordem obrigatória do DOM

1. Painel vermelho de 429 × 649 px, recuo de 10 px, cantos superiores de 30 px e miolo de 389 px. Campo e botão de 58 px empilhados. Links em duas colunas, marca e copyright em coluna. Rodapé de 729 px, dentro de 812 px..

##### Comportamento Mobile-First observado (375px)

Painel de 1300 × 507 px com miolo de 1204 px. Newsletter de 720 px à esquerda e dois grupos em 420 px à direita. Formulário em linha e assinatura abaixo de um divisor, com copyright do lado oposto.

##### Expansão Desktop observada (1024px+ / 1440px)

Newsletter precede atalhos e o divisor separa a assinatura final. Preservar acesso às ações de reserva e localização.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Paleta, tipografia, cantos, destinos e frequência do email.
- **Adaptáveis** — Campo e botão de inscrição presentes. Envio e confirmação [NÃO OBSERVADO].

##### Animações & Interações observadas

- Explicar o que será enviado. Evitar duplicar o mapa ou esconder a ação de reserva entre redes sociais.

##### Regras Anti-Slop específicas daquela seção

- undefined

##### Linha pronta para o `INDEX.md`

- **L7-NAV-04 | Footer de restaurante com newsletter e dois grupos de links** — Melhor para: restaurantes, cantinas, cafés e bares. Vibe: editorial e calorosa. (Fonte: Ruota) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Título curto e uma frase que indique conteúdo e frequência do email. Dois grupos de três links e uma linha final com marca e endereço.]
