# Lote 6 — Referências web

## Páginas inspecionadas

| Site | URL inspecionada | Desktop | Mobile | Overflow horizontal |
| --- | --- | --- | --- | --- |
| Cassian | https://tidy-marketing-173692.framer.app/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Elysévia | https://xn--elysvia-eya.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Silenus | https://silenus.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| HomeSalon TNC | https://homesalon-tnc.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Chapter Barbershop | https://chapterbarbershop.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |

Dimensões em `innerWidth × innerHeight`. Overflow compara `scrollWidth` e `clientWidth` da raiz. Inspeção em navegador virtual com capturas pontuais, leitura do DOM e rolagem amostrada até o rodapé. A variante estreita usou o fallback aprovado de zoom a 300%, com 449 px de área útil. Os rótulos das fichas seguem o formato do acervo. Os 375 px e o toque não foram testados. A dobra de 812 px foi estimada a partir da geometria de cada seção. Os limiares exatos dos módulos não foram isolados. As cinco URLs abriram diretamente.

## Fichas por categoria

### `special-modules.md`

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

##### Linha pronta para o `INDEX.md`

- **L6-SPEC-01 | Seletor de procedimentos em três perguntas** — Melhor para: clínicas e catálogos consultivos. Vibe: clínica e guiada. (Fonte: Cassian) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Claro]

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

##### Linha pronta para o `INDEX.md`

- **L6-SPEC-02 | Comparador de duas imagens com divisor operável** — Melhor para: clínicas, fotografia e projetos de restauração. Vibe: documental e precisa. (Fonte: Cassian) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Claro]

### `navigation-chrome.md`

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

##### Linha pronta para o `INDEX.md`

- **L6-NAV-01 | Diretório de opções por preocupação em grade alternada** — Melhor para: clínicas, consultorias e serviços especializados. Vibe: acolhedora e gráfica. (Fonte: Elysévia) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Escuro]

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

##### Linha pronta para o `INDEX.md`

- **L6-NAV-02 | Diretório de unidades filtrado por cidade** — Melhor para: barbearias, franquias e redes de atendimento. Vibe: urbana e funcional. (Fonte: Chapter Barbershop) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Escuro]

### `features-process.md`

#### L6-FEAT-01 — Percurso de consulta com imagem e nota de acolhimento

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L6-FEAT-01`
- **Nome do padrão** — Percurso de consulta com imagem e nota de acolhimento
- **Fonte** — [Elysévia](https://xn--elysvia-eya.framer.website/)
- **Nichos indicados** — clínicas e serviços consultivos

##### Requisitos de Mídia e Copy

Uma foto com ponto focal central, uma nota de contexto e três etapas com texto de uma frase.

##### Ordem obrigatória do DOM

1. Grupo visual com imagem e nota.
2. Identificador, título e introdução.
3. Três etapas com número, nome e descrição.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 417 px. Foto de 417 × 380 px (1,10:1). O bloco textual mede 1032 px com etapas e ultrapassa 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Área de 1280 px com foto de 608 × 760 px e coluna textual de 560 px, cerca de 52/48 sem o vão. Etapas verticais no lado do texto.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter nota associada à foto e etapas numeradas após a introdução.
- **Adaptáveis** — Foto, paleta e forma dos números.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Cada etapa deve informar uma decisão ou conversa específica. Evitar texto repetitivo entre avaliação e acompanhamento.

##### Linha pronta para o `INDEX.md`

- **L6-FEAT-01 | Percurso de consulta com imagem e nota de acolhimento** — Melhor para: clínicas e serviços consultivos. Vibe: serena e editorial. (Fonte: Elysévia) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Claro]

#### L6-FEAT-02 — Como funciona em três cenas de atendimento domiciliar

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L6-FEAT-02`
- **Nome do padrão** — Como funciona em três cenas de atendimento domiciliar
- **Fonte** — [HomeSalon TNC](https://homesalon-tnc.framer.website/)
- **Nichos indicados** — serviços em domicílio, salões móveis e atendimento sob agendamento

##### Requisitos de Mídia e Copy

Três etapas com nome orientado à ação e uma linha explicativa. Imagens de apoio podem mostrar ambiente ou equipamento.

##### Ordem obrigatória do DOM

1. Título da seção.
2. Grupo de etapas.
3. Em cada etapa: número, ação e resumo.

##### Comportamento Mobile-First observado (375px)

Faixa de 417 px. Bloco de processo de 1054 px e corpo examinado de cerca de 250 px. Título e textos têm altura para caber isoladamente em 812 px, mas o trecho da página inclui espaço adicional de composição.

##### Expansão Desktop observada (1024px+ / 1440px)

Bloco de 1316 px em uma seção de rolagem prolongada. A área vinculada à rolagem mediu cerca de 4961 px. Imagens estreitas de 191 × 481 px complementam as etapas na variante larga.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Ordem da seleção, agendamento e atendimento. A descrição identifica o que acontece em cada etapa.
- **Adaptáveis** — Foto, formato dos números e cores.

##### Animações & Interações observadas

- Gatilho e efeito visual exato da sequência [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Dar uma tarefa distinta a cada etapa. Preservar acesso ao conteúdo essencial mesmo quando a apresentação tiver rolagem extensa.

##### Linha pronta para o `INDEX.md`

- **L6-FEAT-02 | Como funciona em três cenas de atendimento domiciliar** — Melhor para: serviços em domicílio, salões móveis e atendimento sob agendamento. Vibe: direta e gráfica. (Fonte: HomeSalon TNC) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Escuro]

### `showcase-media.md`

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

##### Linha pronta para o `INDEX.md`

- **L6-SHOW-01 | Catálogo de cortes com sequência fotográfica** — Melhor para: barbearias, salões e estúdios de beleza. Vibe: escura e de ofício. (Fonte: Silenus) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Escuro]

### `social-proof.md`

#### L6-PROOF-01 — Depoimentos em coluna ao lado de uma foto de execução

- **Categoria destino** — `social-proof.md`
- **ID sugerido** — `L6-PROOF-01`
- **Nome do padrão** — Depoimentos em coluna ao lado de uma foto de execução
- **Fonte** — [Silenus](https://silenus.framer.website/)
- **Nichos indicados** — barbearias, salões e serviços artesanais

##### Requisitos de Mídia e Copy

Uma foto de execução, três depoimentos curtos e avatares opcionais. Nome e avaliação em cada registro.

##### Ordem obrigatória do DOM

1. Identificador, título e introdução.
2. Foto de execução.
3. Três cartões com citação, identificação e avaliação.

##### Comportamento Mobile-First observado (375px)

Pilha em faixa de 409 px. Imagem interna de 491 × 480 px antes do recorte visual. Cabeçalho de 169 px e corpo de 1102 px, além de respiros. O conjunto excede 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Faixa de 1268 px com fotografia à esquerda e três cartões contornados à direita. Imagem interna de 609 × 680 px em uma amostra, com recorte para a área visual. Avatares de 48 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Três vozes distintas, cada citação com autoria e avaliação correspondente.
- **Adaptáveis** — Imagem, cor de borda, tipografia e estilo de avatar.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Usar a foto como contexto do serviço. Manter os relatos verificáveis e fáceis de distinguir.

##### Linha pronta para o `INDEX.md`

- **L6-PROOF-01 | Depoimentos em coluna ao lado de uma foto de execução** — Melhor para: barbearias, salões e serviços artesanais. Vibe: documental e acolhedora. (Fonte: Silenus) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Escuro]

#### L6-PROOF-02 — Garantia de retorno com três condições explícitas

- **Categoria destino** — `social-proof.md`
- **ID sugerido** — `L6-PROOF-02`
- **Nome do padrão** — Garantia de retorno com três condições explícitas
- **Fonte** — [Chapter Barbershop](https://chapterbarbershop.framer.website/)
- **Nichos indicados** — barbearias, salões e serviços presenciais

##### Requisitos de Mídia e Copy

Uma afirmação curta com prazo, uma explicação de até duas frases e três condições de uma linha.

##### Ordem obrigatória do DOM

1. Título e explicação da garantia.
2. Faixa de termos em destaque.
3. Três condições com título e explicação.

##### Comportamento Mobile-First observado (375px)

Título e explicação em área de 401 px. Faixa de 132 px e condições em bloco de 265 px. Seção de 709 px, dentro de uma dobra local de 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Abertura de 1320 px, título de 640 px e faixa intermediária. Três condições em linha com cerca de 379 × 77 px cada. Fundo escuro e texto de alto contraste.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Prazo, alcance e custo ficam explícitos também fora da faixa de destaque.
- **Adaptáveis** — Tipografia, cores e redação conforme a garantia real.

##### Animações & Interações observadas

- Movimento da faixa e interação [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar condições testáveis com prazo e custo explícitos. Evitar depender de texto repetido para explicar como solicitar o retorno.

##### Linha pronta para o `INDEX.md`

- **L6-PROOF-02 | Garantia de retorno com três condições explícitas** — Melhor para: barbearias, salões e serviços presenciais. Vibe: objetiva e enfática. (Fonte: Chapter Barbershop) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Escuro]

### `conversion-closing.md`

#### L6-CONV-01 — Agendamento domiciliar com endereço na sequência de reserva

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L6-CONV-01`
- **Nome do padrão** — Agendamento domiciliar com endereço na sequência de reserva
- **Fonte** — [HomeSalon TNC](https://homesalon-tnc.framer.website/)
- **Nichos indicados** — salões móveis, técnicos e serviços domiciliares

##### Requisitos de Mídia e Copy

Rótulos claros para serviço, data, hora, local e contato. Uma introdução curta e um botão de confirmação.

##### Ordem obrigatória do DOM

1. Título e introdução.
2. Seletor, data, hora e localização.
3. Nome, email, telefone e mensagem.
4. Botão de confirmação.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 417 px; campos internos de cerca de 405 px. Botão de 417 × 49 px. Bloco de aproximadamente 831 px, excedendo 812 px. Campos divididos por linhas finas.

##### Expansão Desktop observada (1024px+ / 1440px)

Seletor e campos iniciais em pares de cerca de 399 px. Telefone e mensagem em largura total. Botão de 860 × 73 px. Fundo preto e rótulos claros.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Localização faz parte da reserva e permanece junto da data e da hora.
- **Adaptáveis** — Estilo dos campos, ícones, textos e ordem de opções do seletor.

##### Animações & Interações observadas

- Seletor e campos nativos identificados. Envio e confirmação [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- As opções do seletor precisam corresponder ao rótulo. A amostra usava cidades em um campo de tipo de serviço e texto provisório na introdução.

##### Linha pronta para o `INDEX.md`

- **L6-CONV-01 | Agendamento domiciliar com endereço na sequência de reserva** — Melhor para: salões móveis, técnicos e serviços domiciliares. Vibe: minimalista e operacional. (Fonte: HomeSalon TNC) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Escuro]
