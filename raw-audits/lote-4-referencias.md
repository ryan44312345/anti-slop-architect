# Lote 4 — Referências web

## Páginas inspecionadas

| Site | URL inspecionada | Desktop | Mobile | Overflow horizontal |
| --- | --- | --- | --- | --- |
| Ruota | https://ruota-template.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Braise | https://braise-dining.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Skyline Residences | https://skyline-estate.framer.website/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |
| Veyora | https://veyora.framer.ai/ | 1363 × 936 px CSS | 454 × 312 px CSS | Desktop 1348 = 1348 · Mobile 449 = 449 |

Dimensões em `innerWidth × innerHeight`. Overflow compara `scrollWidth` e `clientWidth` na raiz. Inspeção no navegador virtual com leitura do DOM, rolagem amostrada até o rodapé e capturas pontuais. A variante estreita usou o fallback aprovado de zoom a 300%, com 449 px de área útil. O rótulo das fichas segue o modelo dos lotes anteriores. Os 375 px e o toque não foram testados. As estimativas de dobra usam 812 px a partir do topo da própria seção. Os limiares exatos dos componentes não foram isolados neste lote. As larguras de mídia são das caixas medidas e as proporções entre colunas excluem o vão quando indicado. No Ruota foram escolhidos dois padrões diferentes dos já registrados no Lote 3.

## Fichas por categoria

### `special-modules.md`

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

##### Linha pronta para o `INDEX.md`

- **L4-SPEC-01 | Carta por taça ao lado de mesa privativa** — Melhor para: cantinas, bares de vinho e restaurantes. Vibe: editorial e calorosa. (Fonte: Ruota) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Claro]

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

##### Linha pronta para o `INDEX.md`

- **L4-SPEC-02 | Linha do tempo de degustação com estimativa de mesa** — Melhor para: menus degustação, experiências guiadas e eventos gastronômicos. Vibe: sensorial e precisa. (Fonte: Braise) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Escuro]

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

##### Linha pronta para o `INDEX.md`

- **L4-SPEC-03 | Explorador de plantas com abas de tipologia** — Melhor para: incorporadoras, imobiliárias e empreendimentos residenciais. Vibe: arquitetônica e informativa. (Fonte: Skyline Residences) | Tags: [Mídia: Foto-Crítica] [Scroll: Estático] [Fundo: Escuro]

### `navigation-chrome.md`

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

##### Linha pronta para o `INDEX.md`

- **L4-NAV-01 | Endereço com horários e sinal de abertura** — Melhor para: restaurantes, cafés e lojas de bairro. Vibe: tipográfica e direta. (Fonte: Ruota) | Tags: [Mídia: Tipográfico] [Scroll: Estático] [Fundo: Claro]

### `conversion-closing.md`

#### L4-CONV-01 — Sala privativa com palco fotográfico e ficha de capacidade

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L4-CONV-01`
- **Nome do padrão** — Sala privativa com palco fotográfico e ficha de capacidade
- **Fonte** — [Braise](https://braise-dining.framer.website/)
- **Nichos indicados** — eventos privados, restaurantes e espaços de locação

##### Requisitos de Mídia e Copy

Uma cena horizontal da sala com zona livre para o texto. Título curto, descrição de uma frase e três pares de parâmetro e valor.

##### Ordem obrigatória do DOM

1. Título e descrição.
2. Lista de capacidade da sala, capacidade total e valor mínimo.
3. Link de consulta.
4. Camadas de imagem do palco.

##### Comportamento Mobile-First observado (375px)

Palco sticky de largura total com texto em caixa de cerca de 359 px e parâmetros em linhas. Imagens seguem a altura do palco. O bloco interno mediu cerca de 391 px, mas o encaixe confortável em 812 px depende do estado e da altura do palco.

##### Expansão Desktop observada (1024px+ / 1440px)

Trecho de 1732 px com palco sticky observado a 1348 × 515 px. Texto sobreposto em bloco de 712 px. Três métricas em grupos de cerca de 236 px. Camadas fotográficas ocupam toda a largura.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Retirar capacidade e valor do plano decorativo e manter a consulta depois dos três dados.
- **Adaptáveis** — Fotografia, tipografia, contraste e critérios da reserva.

##### Animações & Interações observadas

- Posição sticky verificada no DOM. Gatilho e efeito específico das camadas [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Garantir contraste mesmo sobre a área mais clara da sala. Informar qual capacidade se refere a cada modalidade de evento.

##### Linha pronta para o `INDEX.md`

- **L4-CONV-01 | Sala privativa com palco fotográfico e ficha de capacidade** — Melhor para: eventos privados, restaurantes e espaços de locação. Vibe: imersiva e reservada. (Fonte: Braise) | Tags: [Mídia: Foto-Crítica] [Scroll: Sticky] [Fundo: Escuro]

### `features-process.md`

#### L4-FEAT-01 — Serviços residenciais em linhas numeradas com fotografia

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L4-FEAT-01`
- **Nome do padrão** — Serviços residenciais em linhas numeradas com fotografia
- **Fonte** — [Skyline Residences](https://skyline-estate.framer.website/)
- **Nichos indicados** — condomínios, hotéis e empreendimentos de alto padrão

##### Requisitos de Mídia e Copy

Cinco fotos de ações reais. Título de até cinco palavras e uma frase que diga o que está incluído.

##### Ordem obrigatória do DOM

1. Título da seção e introdução.
2. Sequência de cinco serviços.
3. Em cada serviço: nome, número, descrição e foto associada.

##### Comportamento Mobile-First observado (375px)

Cinco módulos empilhados em faixa de 409 px. Foto de 385 × 207 px (1,86:1) e raio de 2 px. A lista inteira mede cerca de 2158 px. Um módulo médio cabe em 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Faixa de 1268 px. A lista mede cerca de 2061 px, com fotos de 572 × 282 px (2,03:1) e raio de 2 px. O conjunto continua distribuído em linhas sucessivas.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Um serviço, uma imagem e uma descrição por linha. Manter numeração coerente com a sequência.
- **Adaptáveis** — Cores, fotografia, tipografia e quantidade de serviços.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Usar fotos que ilustrem a entrega do serviço. Dizer o que a equipe efetivamente faz em vez de empilhar adjetivos.

##### Linha pronta para o `INDEX.md`

- **L4-FEAT-01 | Serviços residenciais em linhas numeradas com fotografia** — Melhor para: condomínios, hotéis e empreendimentos de alto padrão. Vibe: discreta e funcional. (Fonte: Skyline Residences) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Escuro]

#### L4-FEAT-02 — Lista de serviços com painel expandido

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L4-FEAT-02`
- **Nome do padrão** — Lista de serviços com painel expandido
- **Fonte** — [Veyora](https://veyora.framer.ai/)
- **Nichos indicados** — imobiliárias, administradoras e consultorias

##### Requisitos de Mídia e Copy

Uma foto por serviço, título curto e cerca de 15–25 palavras de descrição. Um link apenas quando houver destino próprio.

##### Ordem obrigatória do DOM

1. Identificador e título da seção.
2. Três cabeçalhos de serviço.
3. No item aberto, texto e mídia associados ao próprio cabeçalho.

##### Comportamento Mobile-First observado (375px)

Área de 417 px e margens de 16 px. O primeiro serviço estava expandido e sua imagem media 417 × 240 px (1,74:1), raio de 8 px. O grupo de itens mediu 898 px, acima de uma dobra local de 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Largura útil de 1284 px. Cabeçalhos de serviço de cerca de 800 px e imagem de 360 × 232 px (1,55:1), raio de 8 px. O painel aberto distribui texto e foto lado a lado em fundo escuro.

##### Invariantes vs. Adaptáveis

- **Invariantes** — A descrição e a mídia pertencem ao serviço correspondente e seguem o cabeçalho no DOM.
- **Adaptáveis** — Paleta, tipografia, enquadramento e texto do serviço.

##### Animações & Interações observadas

- Estado inicial expandido confirmado. Mudança de painel após clicar no segundo cabeçalho [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Manter os nomes dos serviços visíveis nos estados fechados. Evitar fotos equivalentes para operações com resultados diferentes.

##### Linha pronta para o `INDEX.md`

- **L4-FEAT-02 | Lista de serviços com painel expandido** — Melhor para: imobiliárias, administradoras e consultorias. Vibe: sóbria e orientada à ação. (Fonte: Veyora) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Escuro]

#### L4-FEAT-03 — Jornada em quatro etapas ao lado de imagem arquitetônica

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L4-FEAT-03`
- **Nome do padrão** — Jornada em quatro etapas ao lado de imagem arquitetônica
- **Fonte** — [Veyora](https://veyora.framer.ai/)
- **Nichos indicados** — imobiliárias, escritórios de arquitetura e serviços consultivos

##### Requisitos de Mídia e Copy

Uma foto de arquitetura e quatro etapas, com ícone, número, título curto e descrição de até 15–20 palavras.

##### Ordem obrigatória do DOM

1. Identificador e título.
2. Área de conteúdo com quatro cartões numerados e fotografia associada.
3. Cada cartão agrupa ícone, número, título e descrição.

##### Comportamento Mobile-First observado (375px)

Conteúdo em coluna de 417 px, margem de 16 px e imagem de 417 × 280 px (1,49:1), raio de 8 px. A região de conteúdo mede cerca de 1464 px, exigindo rolagem para a sequência completa.

##### Expansão Desktop observada (1024px+ / 1440px)

Área de 1284 × 576 px. Foto de 634 × 576 px à esquerda e grade 2 × 2 de cartões à direita, em proporção próxima de 50/50. Painéis brancos sobre fundo cinza-claro, com ícone e número nos cantos superiores.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Preservar sequência de 01 a 04 e leitura individual de cada etapa.
- **Adaptáveis** — Foto, estilo dos ícones, fontes e cor das superfícies.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Manter número e ícone secundários em relação à ação da etapa. Usar verbos que descrevam o que a pessoa pode fazer em cada momento.

##### Linha pronta para o `INDEX.md`

- **L4-FEAT-03 | Jornada em quatro etapas ao lado de imagem arquitetônica** — Melhor para: imobiliárias, escritórios de arquitetura e serviços consultivos. Vibe: clara e ordenada. (Fonte: Veyora) | Tags: [Mídia: Foto-Adaptável] [Scroll: Estático] [Fundo: Claro]
