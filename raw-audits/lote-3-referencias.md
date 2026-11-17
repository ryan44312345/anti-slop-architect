# Lote 3 — Referências web

## Páginas inspecionadas

| Site | URL inspecionada | Desktop | Mobile | Overflow horizontal |
| --- | --- | --- | --- | --- |
| Ruota | https://ruota-template.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Slice Town | https://slice-town-wbs.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Cafenza | https://cafenza.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Foodee | https://foodee.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |

Dimensões em `innerWidth × innerHeight`. Overflow compara `scrollWidth` com `clientWidth` da raiz. A inspeção usou Chrome virtual, leitura direta do DOM, capturas pontuais e rolagem amostrada até o rodapé. A variante estreita usou o fallback previamente aprovado de zoom a 300%. A área útil foi de 449 px. Os rótulos das fichas seguem o Lote 2. Não houve medição a 375 px nem emulação de toque. O encaixe em 812 px é uma estimativa a partir das caixas internas e considera o topo de cada seção, não o topo da página. A posição sticky e os estados de entrada podem alterar os limites momentâneos. Os links da tabela são as páginas abertas diretamente; `/#menu` no Slice Town foi acessado ao testar a âncora.

## Fichas por categoria

### `narrative-about.md`

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

##### Linha pronta para o `INDEX.md`

- **L3-NARR-01 | Painel de ofício com números em círculos** — Melhor para: cantinas artesanais, padarias e torrefações. Vibe: editorial e calorosa. (Fonte: Ruota) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Adaptável]

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

##### Linha pronta para o `INDEX.md`

- **L3-NARR-02 | Retratos da equipe com ficha de função** — Melhor para: restaurantes autorais, confeitaria e hospitalidade. Vibe: humana e editorial. (Fonte: Foodee) | Tags: [Mídia: Foto-Crítica] [Scroll: Sticky] [Fundo: Adaptável]

### `special-modules.md`

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

##### Linha pronta para o `INDEX.md`

- **L3-SPEC-01 | Cardápio diário em cartões sticky sobrepostos** — Melhor para: cantinas, menus do dia e restaurantes sazonais. Vibe: editorial e artesanal. (Fonte: Ruota) | Tags: [Mídia: Foto-Crítica] [Scroll: Sticky] [Fundo: Claro]

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

##### Linha pronta para o `INDEX.md`

- **L3-SPEC-02 | Lista de pizzas com preços alinhados por tamanho** — Melhor para: pizzarias, padarias e cardápios por porção. Vibe: retrô e direta. (Fonte: Slice Town) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Escuro]

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

##### Linha pronta para o `INDEX.md`

- **L3-SPEC-03 | Seleção de pratos com miniaturas circulares e preço em destaque** — Melhor para: restaurantes vegetarianos, bistrôs e menus de degustação. Vibe: informal e gastronômica. (Fonte: Foodee) | Tags: [Mídia: Foto-Crítica] [Scroll: Sticky] [Fundo: Claro]

### `conversion-closing.md`

#### L3-CONV-01 — Reserva com campos em pares e fundo fotográfico

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L3-CONV-01`
- **Nome do padrão** — Reserva com campos em pares e fundo fotográfico
- **Fonte** — [Slice Town](https://slice-town-wbs.framer.website/)
- **Nichos indicados** — pizzarias, bistrôs e restaurantes com serviço de mesa

##### Requisitos de Mídia e Copy

Uma textura ou fotos de fundo podem ser usadas se não competirem com os campos. Rótulos objetivos e uma única ação principal.

##### Ordem obrigatória do DOM

1. H2 de reserva.
2. Formulário com nome, telefone, email, número de pessoas, data e horário.
3. Pedidos especiais e botão de reserva.
4. Camada decorativa de fundo no DOM.

##### Comportamento Mobile-First observado (375px)

Formulário de 417 × 809 px, recuo de 16 px e raio de 10 px. Seis campos em uma coluna, textarea e botão. O cartão sozinho ocupa quase 812 px; somado ao título, não cabe integralmente na dobra local.

##### Expansão Desktop observada (1024px+ / 1440px)

Formulário de 690 × 640 px, raio de 16 px, campos em três pares. Observações ocupam a faixa inferior. Superfície creme contrastada com campos claros e contorno escuro. CSS de página em 810 e 1200 px; limiar do formulário não isolado.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Ordem do preenchimento e separação entre campos obrigatórios e observações.
- **Adaptáveis** — Paleta, fotografia, sombras e texto do botão.

##### Animações & Interações observadas

- Presença de campos nativos de data e hora confirmada. Animação de envio e confirmação da reserva [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Manter rótulos visíveis fora dos campos. Proteger o contraste do formulário independentemente do conteúdo do fundo.

##### Linha pronta para o `INDEX.md`

- **L3-CONV-01 | Reserva com campos em pares e fundo fotográfico** — Melhor para: pizzarias, bistrôs e restaurantes com serviço de mesa. Vibe: descontraída e gráfica. (Fonte: Slice Town) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Adaptável]

### `showcase-media.md`

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

##### Linha pronta para o `INDEX.md`

- **L3-SHOW-01 | Sequência de cenas com títulos sobre fotografia** — Melhor para: cafeterias, hotéis e espaços de convivência. Vibe: fotográfica e contemplativa. (Fonte: Cafenza) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Claro]

### `features-process.md`

#### L3-FEAT-01 — FAQ lateral com cartões expansíveis

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L3-FEAT-01`
- **Nome do padrão** — FAQ lateral com cartões expansíveis
- **Fonte** — [Cafenza](https://cafenza.framer.website/)
- **Nichos indicados** — cafeterias, espaços de trabalho e serviços com reserva

##### Requisitos de Mídia e Copy

Dispensa mídia. Cinco perguntas curtas e respostas de um parágrafo centradas em dúvidas operacionais.

##### Ordem obrigatória do DOM

1. Identificador e título.
2. Lista de perguntas.
3. Em cada cartão: rótulo, ícone de expansão e resposta quando aberto.

##### Comportamento Mobile-First observado (375px)

Uma coluna. Conteúdo de 409 px com recuo de 20 px, título de cerca de 368 px e cartões claros com borda fina. O contêiner mediu 699 px na amostra; com o respiro externo a seção mediu 899 px e ultrapassa uma dobra local de 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Cabeçalho de 524 px e trilha de perguntas de 646 px. Título verde à esquerda e cartões alinhados à direita. Faixas CSS da página em 810 e 1200 px; limiar exato do empilhamento não isolado.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Título antes da lista; pergunta e resposta permanecem dentro do mesmo cartão.
- **Adaptáveis** — Cores, fontes, forma do ícone e quantidade de perguntas.

##### Animações & Interações observadas

- Clique na pergunta sobre a origem dos grãos no desktop → cartão cresceu e o ícone mudou de + para ×. Texto completo e duração da transição [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar perguntas que removam incerteza real de atendimento. Garantir indicação clara de aberto e fechado.

##### Linha pronta para o `INDEX.md`

- **L3-FEAT-01 | FAQ lateral com cartões expansíveis** — Melhor para: cafeterias, espaços de trabalho e serviços com reserva. Vibe: calma e utilitária. (Fonte: Cafenza) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Claro]
