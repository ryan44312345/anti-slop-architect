# navigation-chrome.md

#### L2-NAV-01 — Diretório de unidades com mapa expansível

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L2-NAV-01`
- **Nome do padrão** — Diretório de unidades com mapa expansível
- **Fonte** — [FineDine Home](https://finedine-template.framer.website/)
- **Nichos indicados** — restaurantes com filiais, hotéis e espaços de atendimento

**Evidência histórica** — Lote 2. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Um mapa por unidade, texto de rota e dados operacionais. Nome, endereço e horário visíveis mesmo com o painel fechado.

##### Ordem obrigatória do DOM

1. Identificador, H2 e explicação.
2. Lista de unidades com botão contendo nome, endereço, horário e ícone.
3. Painel com mapa, dados de transporte e acesso, telefone, email e ações de rota e reserva.

##### Comportamento em largura estreita

Lista de 409 px com margens de 20 px. Cabeçalho de aproximadamente 175 px. No painel aberto o mapa de 165 × 400 px ficou ao lado dos dados, que quebraram em várias linhas. Cabe um cabeçalho fechado em 812 px. O encaixe do painel aberto depende das quebras e do conteúdo.

##### Comportamento em desktop

Faixa de 1252 px. Cabeçalho de cerca de 109 px, com nome, endereço e horários em grupos horizontais. Mapa aberto de 586 × 400 px ao lado dos detalhes. Divisórias finas em fundo escuro. CSS inclui 810 e 1200 px, com limiar do componente sem isolamento.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Dados operacionais no estado fechado. Mapa e ações vinculados à unidade correspondente.
- **Adaptáveis** — Arte do mapa, paleta, separadores e textos dos botões.

##### Animações & Interações observadas

- Clique em Park Slope → o traço vertical do ícone girou em direção à posição horizontal. Exibição final dos detalhes da unidade [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Dimensionar a área de texto para preservar telefone e email. Acompanhar o mapa com instruções textuais.

##### Direção de arte e aplicação

[INFERIDO] **Diretório de unidades.** Abra mapa sob demanda quando houver escolha de filial; mantenha endereço legível antes de abrir.

#### L4-NAV-01 — Endereço com horários e sinal de abertura

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L4-NAV-01`
- **Nome do padrão** — Endereço com horários e sinal de abertura
- **Fonte** — [Ruota](https://ruota-template.framer.website/)
- **Nichos indicados** — restaurantes, cafés e lojas de bairro

**Evidência histórica** — Lote 4. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Endereço em destaque, uma linha por faixa de horário, telefone e email. Um estado curto para o dia atual.

##### Ordem obrigatória do DOM

1. Identificador e endereço.
2. Colunas de horários e contato, com indicação breve de funcionamento.
3. Indicador circular do dia e estado de abertura.

##### Comportamento em largura estreita

Detalhes de 409 px em coluna e círculo de 290 × 290 px abaixo. O bloco de detalhes mede 669 px e cabe isoladamente em 812 px; a composição inteira mede 1079 px. Superfície creme e dados em vermelho.

##### Comportamento em desktop

Detalhes de 824 px com horários e contato lado a lado. Círculo vermelho de 380 × 380 px à direita. Seção de 763 px. Endereço domina a primeira linha do bloco principal.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Priorizar endereço e horários completos. O estado atual complementa a semana inteira.
- **Adaptáveis** — Cores, tipografia e geometria do indicador.

##### Animações & Interações observadas

- Estado fechado e próxima abertura foram exibidos. Atualização na mudança de horário [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Manter o estado atual em texto. Dar contraste suficiente às linhas de horário e confirmar o fuso da unidade antes de implementar o cálculo.

##### Direção de arte e aplicação

[INFERIDO] **Informação de visita.** Horário e status respondem perguntas diferentes; exiba o fuso e trate dias especiais na implementação.

#### L6-NAV-01 — Diretório de opções por preocupação em grade alternada

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L6-NAV-01`
- **Nome do padrão** — Diretório de opções por preocupação em grade alternada
- **Fonte** — [Elysévia](https://xn--elysvia-eya.framer.website/)
- **Nichos indicados** — clínicas, consultorias e serviços especializados

**Evidência histórica** — Lote 6. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Dispensa foto. Seis temas curtos e uma frase de cerca de 10–16 palavras por item.

##### Ordem obrigatória do DOM

1. Identificador e título.
2. Introdução breve e acesso ao índice completo.
3. Grade de links com número, tema, descrição e indicador.

##### Comportamento em largura estreita

Painel de 417 px, área de cartões de 381 px e uma coluna. Cada cartão mede cerca de 229 px de altura. Cabe o cabeçalho de 302 px e o primeiro cartão em 812 px; a grade completa exige rolagem.

##### Comportamento em desktop

Painel de 1216 px, cabeçalho de 1120 px dividido entre título e introdução. Grade 3 × 2, com cartões de 363 × 257 px, alternando claro e escuro.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Cada tema funciona como rota própria. Cabeçalho precede os links.
- **Adaptáveis** — Cores, numeração, quantidade de temas e tipografia.

##### Animações & Interações observadas

- Links de tema e índice registrados no DOM. Efeito visual próprio de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Nomear o problema na linguagem do cliente. Evitar converter cada cartão em promessa de resultado.

##### Direção de arte e aplicação

[INFERIDO] **Diretório de serviços.** Rótulos devem corresponder às preocupações do público; preserve a ordem de leitura ao alternar blocos.

#### L6-NAV-02 — Diretório de unidades filtrado por cidade

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L6-NAV-02`
- **Nome do padrão** — Diretório de unidades filtrado por cidade
- **Fonte** — [Chapter Barbershop](https://chapterbarbershop.framer.website/)
- **Nichos indicados** — barbearias, franquias e redes de atendimento

**Evidência histórica** — Lote 6. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Uma foto por unidade, nome e bairro curtos, endereço e horários em linhas legíveis.

##### Ordem obrigatória do DOM

1. Identificador e título.
2. Filtros de cidade incluindo todas.
3. Cartões de unidade com foto, nome, bairro, endereço, horário e ação.

##### Comportamento em largura estreita

Faixa de 401 px e margem de 24 px. Filtros quebram em duas linhas, com área de 88 px. Cartões de 401 × 483 px com foto de 401 × 260 px (1,54:1). Um cartão cabe em 812 px.

##### Comportamento em desktop

Faixa de 1252 px. Filtros lado a lado com cerca de 39 px de altura. Duas colunas quando o conjunto completo está ativo. Cartão de 616 × 517 px e foto de 616 × 260 px (2,37:1).

##### Invariantes vs. Adaptáveis

- **Invariantes** — Cidade ativa controla quais unidades aparecem. Horários e ação permanecem vinculados ao cartão.
- **Adaptáveis** — Paleta, nomes das cidades e direção fotográfica.

##### Animações & Interações observadas

- Clique em Chicago → a lista ficou restrita à unidade Chapter Four, no bairro West Loop.

##### Regras Anti-Slop específicas daquela seção

- Manter o estado ativo identificável e fornecer opção de listar todas. Cada ação precisa apontar para a unidade exibida.

##### Direção de arte e aplicação

[INFERIDO] **Diretório filtrável.** Filtro vale quando reduz uma lista longa; preserve resultado vazio e opção de voltar a todas as cidades.

#### L7-NAV-01 — Footer institucional com escritórios e assinatura monumental

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L7-NAV-01`
- **Nome do padrão** — Footer institucional com escritórios e assinatura monumental
- **Fonte** — [Caldren](https://caldren.framer.website/)
- **Nichos indicados** — imobiliárias, incorporadoras e grupos com vários escritórios

**Evidência histórica** — Lote 7. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1363 = 1363 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Monograma, assinatura larga, promessa curta de newsletter e três grupos de navegação. Uma linha por escritório quando houver espaço.

##### Ordem obrigatória do DOM

1. Monograma, chamada e inscrição por email.
2. Grupos Explore, Company e Offices.
3. Assinatura tipográfica.
4. Copyright e links sociais e legais.

##### Comportamento em largura estreita

Caixa externa de 662 px de altura e miolo de 409 px com margem de 20 px. Topo empilhado, email e ação permanecem lado a lado. A assinatura mede 397 × 56 px. A faixa final empilha copyright e links. O bloco cabe em 812 px pelas medidas do DOM; a captura do extremo inferior mostrou principalmente o fundo.

##### Comportamento em desktop

Área interna de 1235 px com marca e inscrição à esquerda e três grupos em 477 px à direita. Assinatura de 1232 × 173 px abaixo. Linha legal horizontal. Fundo com gradiente azul para bege.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Agrupar destinos institucionais e escritórios e manter a leitura legal independente da imagem da assinatura.
- **Adaptáveis** — Gradiente, fontes, monograma, contatos e número de grupos.

##### Animações & Interações observadas

- Campo e botão de inscrição identificados. Envio e efeitos [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Preservar contraste nas duas extremidades do gradiente. Não usar assinatura gigante para substituir links, endereços ou copyright.

##### Direção de arte e aplicação

[INFERIDO] **Footer institucional.** A assinatura pode marcar o fechamento sem competir com escritórios e contatos.

#### L7-NAV-02 — Header corporativo com links centrais e menu móvel empilhado

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L7-NAV-02`
- **Nome do padrão** — Header corporativo com links centrais e menu móvel empilhado
- **Fonte** — [Koddam](https://koddam.framer.website/)
- **Nichos indicados** — consultorias, serviços B2B e sites institucionais

**Evidência histórica** — Lote 7. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Marca legível em formato compacto, cinco links curtos na referência e um CTA de contato.

##### Ordem obrigatória do DOM

1. Marca.
2. Grupo de destinos com página ativa.
3. CTA de contato no desktop.
4. Na variante estreita, marca e acionador seguidos pelo painel com links e CTA.

##### Comportamento em largura estreita

Barra branca de 60 px, miolo de 419 px com recuo de 15 px. Fechada mostra apenas marca e ícone. Aberta exibe links em coluna na ordem Home, About, Services, Resources, Pricing, depois Contact Us. A indicação verde da página ativa permanece. O painel branco cobre parte do hero.

##### Comportamento em desktop

Barra branca de 80 px, miolo de 1288 px e margem de 30 px. Marca à esquerda, cinco links no centro e CTA em cápsula preta à direita. Página ativa em cápsula verde-clara.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter o estado ativo, sequência de links e acesso ao CTA dentro do painel estreito.
- **Adaptáveis** — Cor do estado ativo, fonte, ícone e texto dos links.

##### Animações & Interações observadas

- Clique no hambúrguer → painel branco abriu e apareceu a lista vertical. Segundo clique → painel recolheu. Curva da transição [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Garantir alcance ao último link quando a altura for baixa. Nomear e expor o estado do acionador para leitores de tela.

##### Direção de arte e aplicação

[INFERIDO] **Header horizontal.** Centro para poucas rotas e uma ação destacada; rótulos longos exigem antecipar a quebra.

#### L7-NAV-03 — Header clínico mínimo com diálogo de catálogo

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L7-NAV-03`
- **Nome do padrão** — Header clínico mínimo com diálogo de catálogo
- **Fonte** — [Cassian](https://tidy-marketing-173692.framer.app/)
- **Nichos indicados** — clínicas com catálogo de serviços e marcas editoriais

**Evidência histórica** — Lote 7. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Marca textual, destinos curtos e CTA de uma palavra ou expressão curta. Categorias e metadados só quando ajudarem a buscar um serviço.

##### Ordem obrigatória do DOM

1. Marca.
2. Links centrais na variante larga.
3. CTA Book.
4. Na variante estreita, acionador.
5. Diálogo com categorias e itens, acesso ao seletor, links de páginas, CTA final e endereço.

##### Comportamento em largura estreita

Barra transparente fixa, caixa de 104 px e linha útil de 72 px. Marca à esquerda, CTA claro e controle de 41 × 32 px à direita. Aberto, o diálogo escuro rolável precede os links institucionais com grupos Face, Breast, Body e Non-surgical, depois acesso ao seletor, páginas, CTA e endereço.

##### Comportamento em desktop

Barra fixa de 76 px com marca e CTA nos extremos e seis links centrais. Sobre o hero a superfície é escura/transparente. Em outra posição foi observado fundo claro e CTA azul, com contraste reduzido no texto central.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter marca e CTA acessíveis antes de abrir o menu. O diálogo oferece saída explícita e navegação organizada.
- **Adaptáveis** — Tipografia, polaridade da superfície, número de grupos e estilos de metadados.

##### Animações & Interações observadas

- Clique em Open menu → diálogo apareceu, controle passou a expanded e foco entrou no primeiro procedimento. Clique em Close menu → diálogo fechou. Retorno de foco e Escape [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Aplicar foco visível e contraste em todas as superfícies. Reservar a lista agrupada de procedimentos a catálogos que precisem desse nível de navegação.

##### Direção de arte e aplicação

[INFERIDO] **Header com diálogo.** Útil quando o catálogo exige agrupamento; trate foco inicial, Escape e retorno ao botão.

#### L7-NAV-04 — Footer de restaurante com newsletter e dois grupos de links

- **Categoria destino** — `navigation-chrome.md`
- **ID sugerido** — `L7-NAV-04`
- **Nome do padrão** — Footer de restaurante com newsletter e dois grupos de links
- **Fonte** — [Ruota](https://ruota-template.framer.website/)
- **Nichos indicados** — restaurantes, cantinas, cafés e bares

##### Requisitos de Mídia e Copy

Título curto, uma frase sobre conteúdo e frequência, campo de e-mail, ação de inscrição, dois grupos de destinos e uma linha de assinatura. A marca pode ser tipográfica. A composição dispensa fotografia.

##### Ordem obrigatória do DOM

1. `footer` com painel, miolo e bloco superior.
2. Newsletter com título e introdução, seguida de formulário com e-mail e botão de envio.
3. Área dos links. A ordem de origem alterna menu, Instagram, reserva, TikTok, eventos privados e mapa. Visualmente, são duas colunas, com ações do restaurante à esquerda.
4. Bloco inferior com divisor, assinatura e copyright com endereço.

##### Comportamento em largura estreita

[MEDIDO] No viewport de 454 × 312 px CSS por zoom, a raiz mediu 449 px úteis sem overflow (449 = 449). O painel mede 429 × 649 px, com 10 px de recuo lateral, 30 px de raio nos cantos superiores e miolo de 389 px. O formulário empilha os controles em 128 px de altura. [OBSERVADO] A newsletter fica acima de duas colunas de links e a assinatura fica acima do copyright.

[MEDIDO] A 545 × 374 px CSS, com 539 px úteis, o painel mede 519 × 649 px e o miolo 479 px. A estrutura superior permanece em coluna. [NÃO OBSERVADO] 375 × 812 px, limiar exato e troca de layout por altura.

##### Comportamento em desktop

[MEDIDO] A 1363 × 936 px CSS, com 1348 px úteis, o painel mede 1300 × 507 px, com raio superior de 40 px. O miolo de 1204 px distribui 720 px para a newsletter e 420 px para links, separados por 64 px. Formulário em linha de 620 × 58 px. [OBSERVADO] Na base, a marca e o copyright ocupam extremidades opostas do divisor.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Publicação primeiro, destinos em grupos distintos e assinatura abaixo de um separador.
- **Adaptáveis** — Paleta, famílias tipográficas, número de redes e frequência real da newsletter.

##### Animações & Interações observadas

- [OBSERVADO] Campo de texto e botão de inscrição presentes. Os destinos de redes e mapa do modelo apontam a páginas genéricas.
- [NÃO OBSERVADO] Envio, confirmação, validação, hover e transições específicas.

##### Regras Anti-Slop específicas daquela seção

- Dê título e frequência verificáveis à newsletter e configure destinos reais para redes, mapa e reservas.
- Use rótulo persistente no campo e status acessível para erro e sucesso. Em telas pequenas, mantenha os controles em fluxo e deixe as colunas dos links quebrarem quando os rótulos ocuparem o espaço disponível.
- Garanta contraste do texto sobre a superfície saturada. Use uma única família de destaque para título e assinatura se a marca permitir.

##### Direção de arte e aplicação

[OBSERVADO] Um painel vermelho (#D8381E) sobre fundo creme inverte as cores da página. O título serifado domina o primeiro olhar, enquanto os links em corpo menor e o divisor demarcam a parte utilitária.

[INFERIDO] A diferença de escala separa convite e navegação sem criar dois cartões concorrentes. O alto contraste e a ordem visual são transferíveis para outras paletas. Prefira um rodapé de contato quando não houver newsletter ativa ou links suficientes para dois grupos.
