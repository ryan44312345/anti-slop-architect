# navigation-chrome.md

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

#### L4-NAV-01 — Endereço com horários e sinal de abertura

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L4-NAV-01`
- **Nome do padrão** — Endereço com horários e sinal de abertura
- **Fonte** — [Ruota](https://ruota-template.framer.website/)
- **Nichos indicados** — restaurantes, cafés e lojas de bairro

##### Requisitos de Mídia e Copy

Endereço em destaque, uma linha por faixa de horário, telefone e email. Um estado curto para o dia atual.

##### Ordem obrigatória do DOM

1. Identificador e endereço.
2. Colunas de horários e contato, com indicação breve de funcionamento.
3. Indicador circular do dia e estado de abertura.

##### Comportamento Mobile-First observado (375px)

Detalhes de 409 px em coluna e círculo de 290 × 290 px abaixo. O bloco de detalhes mede 669 px e cabe isoladamente em 812 px; a composição inteira mede 1079 px. Superfície creme e dados em vermelho.

##### Expansão Desktop observada (1024px+ / 1440px)

Detalhes de 824 px com horários e contato lado a lado. Círculo vermelho de 380 × 380 px à direita. Seção de 763 px. Endereço domina a primeira linha do bloco principal.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Priorizar endereço e horários completos. O estado atual complementa a semana inteira.
- **Adaptáveis** — Cores, tipografia e geometria do indicador.

##### Animações & Interações observadas

- Estado fechado e próxima abertura foram exibidos. Atualização na mudança de horário [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Manter o estado atual em texto. Dar contraste suficiente às linhas de horário e confirmar o fuso da unidade antes de implementar o cálculo.

#### L6-NAV-01 — Diretório de opções por preocupação em grade alternada

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L6-NAV-01`
- **Nome do padrão** — Diretório de opções por preocupação em grade alternada
- **Fonte** — [Elysévia](https://xn--elysvia-eya.framer.website/)
- **Nichos indicados** — clínicas, consultorias e serviços especializados

##### Requisitos de Mídia e Copy

Dispensa foto. Seis temas curtos e uma frase de cerca de 10–16 palavras por item.

##### Ordem obrigatória do DOM

1. Identificador e título.
2. Introdução breve e acesso ao índice completo.
3. Grade de links com número, tema, descrição e indicador.

##### Comportamento Mobile-First observado (375px)

Painel de 417 px, área de cartões de 381 px e uma coluna. Cada cartão mede cerca de 229 px de altura. Cabe o cabeçalho de 302 px e o primeiro cartão em 812 px; a grade completa exige rolagem.

##### Expansão Desktop observada (1024px+ / 1440px)

Painel de 1216 px, cabeçalho de 1120 px dividido entre título e introdução. Grade 3 × 2, com cartões de 363 × 257 px, alternando claro e escuro.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Cada tema funciona como rota própria. Cabeçalho precede os links.
- **Adaptáveis** — Cores, numeração, quantidade de temas e tipografia.

##### Animações & Interações observadas

- Links de tema e índice registrados no DOM. Efeito visual próprio de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Nomear o problema na linguagem do cliente. Evitar converter cada cartão em promessa de resultado.

#### L6-NAV-02 — Diretório de unidades filtrado por cidade

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L6-NAV-02`
- **Nome do padrão** — Diretório de unidades filtrado por cidade
- **Fonte** — [Chapter Barbershop](https://chapterbarbershop.framer.website/)
- **Nichos indicados** — barbearias, franquias e redes de atendimento

##### Requisitos de Mídia e Copy

Uma foto por unidade, nome e bairro curtos, endereço e horários em linhas legíveis.

##### Ordem obrigatória do DOM

1. Identificador e título.
2. Filtros de cidade incluindo todas.
3. Cartões de unidade com foto, nome, bairro, endereço, horário e ação.

##### Comportamento Mobile-First observado (375px)

Faixa de 401 px e margem de 24 px. Filtros quebram em duas linhas, com área de 88 px. Cartões de 401 × 483 px com foto de 401 × 260 px (1,54:1). Um cartão cabe em 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Faixa de 1252 px. Filtros lado a lado com cerca de 39 px de altura. Duas colunas quando o conjunto completo está ativo. Cartão de 616 × 517 px e foto de 616 × 260 px (2,37:1).

##### Invariantes vs. Adaptáveis

- **Invariantes** — Cidade ativa controla quais unidades aparecem. Horários e ação permanecem vinculados ao cartão.
- **Adaptáveis** — Paleta, nomes das cidades e direção fotográfica.

##### Animações & Interações observadas

- Clique em Chicago → a lista ficou restrita à unidade Chapter Four, no bairro West Loop.

##### Regras Anti-Slop específicas daquela seção

- Manter o estado ativo identificável e fornecer opção de listar todas. Cada ação precisa apontar para a unidade exibida.

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
