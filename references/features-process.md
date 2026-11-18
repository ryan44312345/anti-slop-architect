# features-process.md

#### L2-FEAT-01 — Palco sticky com quatro etapas de preparo

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L2-FEAT-01`
- **Nome do padrão** — Palco sticky com quatro etapas de preparo
- **Fonte** — [Ligatra](https://only-instance-526558.framer.app/)
- **Nichos indicados** — hamburguerias, torrefações e marcas artesanais

**Evidência histórica** — Lote 2. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Uma mídia por etapa, com recorte paisagem. Um verbo e uma frase de até 15 palavras por etapa.

##### Ordem obrigatória do DOM

1. Identificador e H2.
2. Palco com janela de mídia e quatro chips.
3. Lista com número, título e frase em cada etapa.

##### Comportamento em largura estreita

Coluna única com margem de 20 px. Janela de 409 × 230 px (16:9), raio de 20 px. Palco e primeira etapa somam cerca de 527 px e cabem em uma dobra local de 812 px. Só a lista completa ocupa 880 px.

##### Comportamento em desktop

Palco de 776 px e lista de 340 px, proporção aproximada 70/30, separados por 64 px. Janela de 776 × 520 px (1,49:1), raio de 32 px. Cada etapa reserva 540 px de percurso. A pilha já estava ativa a 1090 px, compatível com a faixa CSS que muda a 1200 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Palco antes das etapas, um chip e uma mídia por etapa.
- **Adaptáveis** — Paleta, fonte, raios e linguagem fotográfica.

##### Animações & Interações observadas

- O palco tem posição sticky no DOM. A reação específica da mídia ao clicar nos chips ficou [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Justificar o trecho de rolagem com mudanças reais de preparo. Manter verbo, mídia e etapa atual sincronizados.

##### Direção de arte e aplicação

[INFERIDO] **Palco sticky.** Sincronize imagem e etapa quando a troca explicar a transformação; ofereça sequência estática em telas baixas.

#### L2-FEAT-02 — Cinco verbos do ofício em colunas editoriais

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L2-FEAT-02`
- **Nome do padrão** — Cinco verbos do ofício em colunas editoriais
- **Fonte** — [FineDine Home](https://finedine-template.framer.website/)
- **Nichos indicados** — restaurantes autorais, cafés especiais e ateliês

**Evidência histórica** — Lote 2. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Cinco fotos documentais de etapas distintas. Um verbo, uma leitura ou tradução curta e cerca de 15–25 palavras por painel.

##### Ordem obrigatória do DOM

1. Título e subtítulo.
2. Lista de painéis.
3. Em cada painel: inscrição, fotografia, H3, leitura do termo e descrição.
4. Link de aprofundamento.

##### Comportamento em largura estreita

Uma coluna em faixa de 409 px com margem de 20 px. Fotos de 365 × 300 px (1,22:1), com 22 px de recuo interno. Painéis de 749–770 px cabem isoladamente em 812 px. Fundo escuro com separadores discretos.

##### Comportamento em desktop

Cinco colunas de aproximadamente 250 px em 1252 px. Imagens de 206 × 300 px (0,69:1), separadores verticais e inscrição âmbar sobre fundo escuro. CSS contém faixas em 810 e 1200 px. O limiar específico da grade de cinco colunas não foi isolado.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Uma foto por verbo e a mesma sequência de inscrição, foto e explicação.
- **Adaptáveis** — Idioma, cor, fontes e assunto fotográfico.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Usar inscrição em outro idioma quando tiver função informativa. Planejar foco fotográfico que aceite cortes vertical e horizontal.

##### Direção de arte e aplicação

[INFERIDO] **Colunas editoriais.** Os verbos devem distinguir competências; preserve a leitura seguindo a ordem do documento.

#### L3-FEAT-01 — FAQ lateral com cartões expansíveis

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L3-FEAT-01`
- **Nome do padrão** — FAQ lateral com cartões expansíveis
- **Fonte** — [Cafenza](https://cafenza.framer.website/)
- **Nichos indicados** — cafeterias, espaços de trabalho e serviços com reserva

**Evidência histórica** — Lote 3. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Dispensa mídia. Cinco perguntas curtas e respostas de um parágrafo centradas em dúvidas operacionais.

##### Ordem obrigatória do DOM

1. Identificador e título.
2. Lista de perguntas.
3. Em cada cartão: rótulo, ícone de expansão e resposta quando aberto.

##### Comportamento em largura estreita

Uma coluna. Conteúdo de 409 px com recuo de 20 px, título de cerca de 368 px e cartões claros com borda fina. O contêiner mediu 699 px na amostra; com o respiro externo a seção mediu 899 px e ultrapassa uma dobra local de 812 px.

##### Comportamento em desktop

Cabeçalho de 524 px e trilha de perguntas de 646 px. Título verde à esquerda e cartões alinhados à direita. Faixas CSS da página em 810 e 1200 px; limiar exato do empilhamento não isolado.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Título antes da lista; pergunta e resposta permanecem dentro do mesmo cartão.
- **Adaptáveis** — Cores, fontes, forma do ícone e quantidade de perguntas.

##### Animações & Interações observadas

- Clique na pergunta sobre a origem dos grãos no desktop → cartão cresceu e o ícone mudou de + para ×. Texto completo e duração da transição [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar perguntas que removam incerteza real de atendimento. Garantir indicação clara de aberto e fechado.

##### Direção de arte e aplicação

[INFERIDO] **FAQ dividido.** Coloque a entrada editorial ao lado de perguntas autônomas; respostas curtas são adequadas ao acordeão.

#### L4-FEAT-01 — Serviços residenciais em linhas numeradas com fotografia

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L4-FEAT-01`
- **Nome do padrão** — Serviços residenciais em linhas numeradas com fotografia
- **Fonte** — [Skyline Residences](https://skyline-estate.framer.website/)
- **Nichos indicados** — condomínios, hotéis e empreendimentos de alto padrão

**Evidência histórica** — Lote 4. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Cinco fotos de ações reais. Título de até cinco palavras e uma frase que diga o que está incluído.

##### Ordem obrigatória do DOM

1. Título da seção e introdução.
2. Sequência de cinco serviços.
3. Em cada serviço: nome, número, descrição e foto associada.

##### Comportamento em largura estreita

Cinco módulos empilhados em faixa de 409 px. Foto de 385 × 207 px (1,86:1) e raio de 2 px. A lista inteira mede cerca de 2158 px. Um módulo médio cabe em 812 px.

##### Comportamento em desktop

Faixa de 1268 px. A lista mede cerca de 2061 px, com fotos de 572 × 282 px (2,03:1) e raio de 2 px. O conjunto continua distribuído em linhas sucessivas.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Um serviço, uma imagem e uma descrição por linha. Manter numeração coerente com a sequência.
- **Adaptáveis** — Cores, fotografia, tipografia e quantidade de serviços.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Usar fotos que ilustrem a entrega do serviço. Dizer o que a equipe efetivamente faz em vez de empilhar adjetivos.

##### Direção de arte e aplicação

[INFERIDO] **Linhas numeradas.** A numeração orienta a varredura; mantenha descrições comparáveis e fotos ligadas à linha certa.

#### L4-FEAT-02 — Lista de serviços com painel expandido

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L4-FEAT-02`
- **Nome do padrão** — Lista de serviços com painel expandido
- **Fonte** — [Veyora](https://veyora.framer.ai/)
- **Nichos indicados** — imobiliárias, administradoras e consultorias

**Evidência histórica** — Lote 4. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Uma foto por serviço, título curto e cerca de 15–25 palavras de descrição. Um link apenas quando houver destino próprio.

##### Ordem obrigatória do DOM

1. Identificador e título da seção.
2. Três cabeçalhos de serviço.
3. No item aberto, texto e mídia associados ao próprio cabeçalho.

##### Comportamento em largura estreita

Área de 417 px e margens de 16 px. O primeiro serviço estava expandido e sua imagem media 417 × 240 px (1,74:1), raio de 8 px. O grupo de itens mediu 898 px, acima de uma dobra local de 812 px.

##### Comportamento em desktop

Largura útil de 1284 px. Cabeçalhos de serviço de cerca de 800 px e imagem de 360 × 232 px (1,55:1), raio de 8 px. O painel aberto distribui texto e foto lado a lado em fundo escuro.

##### Invariantes vs. Adaptáveis

- **Invariantes** — A descrição e a mídia pertencem ao serviço correspondente e seguem o cabeçalho no DOM.
- **Adaptáveis** — Paleta, tipografia, enquadramento e texto do serviço.

##### Animações & Interações observadas

- Estado inicial expandido confirmado. Mudança de painel após clicar no segundo cabeçalho [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Manter os nomes dos serviços visíveis nos estados fechados. Evitar fotos equivalentes para operações com resultados diferentes.

##### Direção de arte e aplicação

[INFERIDO] **Lista com expansão.** A expansão reduz densidade quando os serviços têm detalhes de tamanhos diferentes; mantenha títulos autoexplicativos.

#### L4-FEAT-03 — Jornada em quatro etapas ao lado de imagem arquitetônica

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L4-FEAT-03`
- **Nome do padrão** — Jornada em quatro etapas ao lado de imagem arquitetônica
- **Fonte** — [Veyora](https://veyora.framer.ai/)
- **Nichos indicados** — imobiliárias, escritórios de arquitetura e serviços consultivos

**Evidência histórica** — Lote 4. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Uma foto de arquitetura e quatro etapas, com ícone, número, título curto e descrição de até 15–20 palavras.

##### Ordem obrigatória do DOM

1. Identificador e título.
2. Área de conteúdo com quatro cartões numerados e fotografia associada.
3. Cada cartão agrupa ícone, número, título e descrição.

##### Comportamento em largura estreita

Conteúdo em coluna de 417 px, margem de 16 px e imagem de 417 × 280 px (1,49:1), raio de 8 px. A região de conteúdo mede cerca de 1464 px, exigindo rolagem para a sequência completa.

##### Comportamento em desktop

Área de 1284 × 576 px. Foto de 634 × 576 px à esquerda e grade 2 × 2 de cartões à direita, em proporção próxima de 50/50. Painéis brancos sobre fundo cinza-claro, com ícone e número nos cantos superiores.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Preservar sequência de 01 a 04 e leitura individual de cada etapa.
- **Adaptáveis** — Foto, estilo dos ícones, fontes e cor das superfícies.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Manter número e ícone secundários em relação à ação da etapa. Usar verbos que descrevam o que a pessoa pode fazer em cada momento.

##### Direção de arte e aplicação

[INFERIDO] **Sequência com imagem lateral.** A foto situa o serviço; mantenha as etapas legíveis como sequência mesmo sem a mídia.

#### L5-FEAT-01 — Etapas de atendimento com fotografia da jornada

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L5-FEAT-01`
- **Nome do padrão** — Etapas de atendimento com fotografia da jornada
- **Fonte** — [Dental Point](https://dental-point-clinic.framer.website/)
- **Nichos indicados** — clínicas, estúdios e serviços agendados

**Evidência histórica** — Lote 5. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Três fotos que representem momentos distintos do atendimento. Um título e uma frase operacional por etapa.

##### Ordem obrigatória do DOM

1. Identificador e título da seção.
2. Três etapas numeradas.
3. Em cada etapa: número, título, texto curto e imagem.

##### Comportamento em largura estreita

Trilho estreito com cartão ativo perto de 417 × 624 px e imagem de 417 × 334 px (1,25:1). Bordas suavizadas na foto. O cabeçalho de 190 px mais o cartão e o vão ultrapassam a dobra de 812 px.

##### Comportamento em desktop

Três blocos sucessivos. Cada linha de 1284 × 680 px tem grupos de 308, 462 e 514 px, cerca de 24/36/40. A fotografia é vertical (514 × 680 px), com número isolado e título e texto no bloco central.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Número, descrição e foto identificam a mesma etapa. Manter a leitura em sequência.
- **Adaptáveis** — Direção fotográfica, tipo de numeração e paleta.

##### Animações & Interações observadas

- O trilho mostrou uma etapa em destaque e bordas das vizinhas na largura estreita. Gatilho exato da troca [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar o texto para explicar o que a pessoa faz ou encontra. Evitar repetir a mesma descrição entre etapas.

##### Direção de arte e aplicação

[INFERIDO] **Jornada com foto.** A foto deve esclarecer o atendimento; use enquadramento documental compatível com o momento descrito.

#### L6-FEAT-01 — Percurso de consulta com imagem e nota de acolhimento

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L6-FEAT-01`
- **Nome do padrão** — Percurso de consulta com imagem e nota de acolhimento
- **Fonte** — [Elysévia](https://xn--elysvia-eya.framer.website/)
- **Nichos indicados** — clínicas e serviços consultivos

**Evidência histórica** — Lote 6. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Uma foto com ponto focal central, uma nota de contexto e três etapas com texto de uma frase.

##### Ordem obrigatória do DOM

1. Grupo visual com imagem e nota.
2. Identificador, título e introdução.
3. Três etapas com número, nome e descrição.

##### Comportamento em largura estreita

Uma coluna de 417 px. Foto de 417 × 380 px (1,10:1). O bloco textual mede 1032 px com etapas e ultrapassa 812 px.

##### Comportamento em desktop

Área de 1280 px com foto de 608 × 760 px e coluna textual de 560 px, cerca de 52/48 sem o vão. Etapas verticais no lado do texto.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter nota associada à foto e etapas numeradas após a introdução.
- **Adaptáveis** — Foto, paleta e forma dos números.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Cada etapa deve informar uma decisão ou conversa específica. Evitar texto repetitivo entre avaliação e acompanhamento.

##### Direção de arte e aplicação

[INFERIDO] **Sequência com nota.** Use a nota para reduzir incerteza antes da consulta; mantenha-a junto da etapa a que se refere.

#### L6-FEAT-02 — Como funciona em três cenas de atendimento domiciliar

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L6-FEAT-02`
- **Nome do padrão** — Como funciona em três cenas de atendimento domiciliar
- **Fonte** — [HomeSalon TNC](https://homesalon-tnc.framer.website/)
- **Nichos indicados** — serviços em domicílio, salões móveis e atendimento sob agendamento

**Evidência histórica** — Lote 6. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Três etapas com nome orientado à ação e uma linha explicativa. Imagens de apoio podem mostrar ambiente ou equipamento.

##### Ordem obrigatória do DOM

1. Título da seção.
2. Grupo de etapas.
3. Em cada etapa: número, ação e resumo.

##### Comportamento em largura estreita

Faixa de 417 px. Bloco de processo de 1054 px e corpo examinado de cerca de 250 px. Título e textos têm altura para caber isoladamente em 812 px, mas o trecho da página inclui espaço adicional de composição.

##### Comportamento em desktop

Bloco de 1316 px em uma seção de rolagem prolongada. A área vinculada à rolagem mediu cerca de 4961 px. Imagens estreitas de 191 × 481 px complementam as etapas na variante larga.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Ordem da seleção, agendamento e atendimento. A descrição identifica o que acontece em cada etapa.
- **Adaptáveis** — Foto, formato dos números e cores.

##### Animações & Interações observadas

- Gatilho e efeito visual exato da sequência [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Dar uma tarefa distinta a cada etapa. Preservar acesso ao conteúdo essencial mesmo quando a apresentação tiver rolagem extensa.

##### Direção de arte e aplicação

[INFERIDO] **Cenas sequenciais.** Reserve uma cena por fase quando ela mudar o entendimento; a ordem deve se manter em coluna.
