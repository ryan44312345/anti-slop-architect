# features-process.md

#### L2-FEAT-01 — Palco sticky com quatro etapas de preparo

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L2-FEAT-01`
- **Nome do padrão** — Palco sticky com quatro etapas de preparo
- **Fonte** — [Ligatra](https://only-instance-526558.framer.app/)
- **Nichos indicados** — hamburguerias, torrefações e marcas artesanais

##### Requisitos de Mídia e Copy

Uma mídia por etapa, com recorte paisagem. Um verbo e uma frase de até 15 palavras por etapa.

##### Ordem obrigatória do DOM

1. Identificador e H2.
2. Palco com janela de mídia e quatro chips.
3. Lista com número, título e frase em cada etapa.

##### Comportamento Mobile-First observado (375px)

Coluna única com margem de 20 px. Janela de 409 × 230 px (16:9), raio de 20 px. Palco e primeira etapa somam cerca de 527 px e cabem em uma dobra local de 812 px. Só a lista completa ocupa 880 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Palco de 776 px e lista de 340 px, proporção aproximada 70/30, separados por 64 px. Janela de 776 × 520 px (1,49:1), raio de 32 px. Cada etapa reserva 540 px de percurso. A pilha já estava ativa a 1090 px, compatível com a faixa CSS que muda a 1200 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Palco antes das etapas, um chip e uma mídia por etapa.
- **Adaptáveis** — Paleta, fonte, raios e linguagem fotográfica.

##### Animações & Interações observadas

- O palco tem posição sticky no DOM. A reação específica da mídia ao clicar nos chips ficou [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Justificar o trecho de rolagem com mudanças reais de preparo. Manter verbo, mídia e etapa atual sincronizados.

#### L2-FEAT-02 — Cinco verbos do ofício em colunas editoriais

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L2-FEAT-02`
- **Nome do padrão** — Cinco verbos do ofício em colunas editoriais
- **Fonte** — [FineDine Home](https://finedine-template.framer.website/)
- **Nichos indicados** — restaurantes autorais, cafés especiais e ateliês

##### Requisitos de Mídia e Copy

Cinco fotos documentais de etapas distintas. Um verbo, uma leitura ou tradução curta e cerca de 15–25 palavras por painel.

##### Ordem obrigatória do DOM

1. Título e subtítulo.
2. Lista de painéis.
3. Em cada painel: inscrição, fotografia, H3, leitura do termo e descrição.
4. Link de aprofundamento.

##### Comportamento Mobile-First observado (375px)

Uma coluna em faixa de 409 px com margem de 20 px. Fotos de 365 × 300 px (1,22:1), com 22 px de recuo interno. Painéis de 749–770 px cabem isoladamente em 812 px. Fundo escuro com separadores discretos.

##### Expansão Desktop observada (1024px+ / 1440px)

Cinco colunas de aproximadamente 250 px em 1252 px. Imagens de 206 × 300 px (0,69:1), separadores verticais e inscrição âmbar sobre fundo escuro. CSS contém faixas em 810 e 1200 px. O limiar específico da grade de cinco colunas não foi isolado.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Uma foto por verbo e a mesma sequência de inscrição, foto e explicação.
- **Adaptáveis** — Idioma, cor, fontes e assunto fotográfico.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Usar inscrição em outro idioma quando tiver função informativa. Planejar foco fotográfico que aceite cortes vertical e horizontal.

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

#### L5-FEAT-01 — Etapas de atendimento com fotografia da jornada

- **Categoria destino** — `features-process.md`
- **ID sugerido** — `L5-FEAT-01`
- **Nome do padrão** — Etapas de atendimento com fotografia da jornada
- **Fonte** — [Dental Point](https://dental-point-clinic.framer.website/)
- **Nichos indicados** — clínicas, estúdios e serviços agendados

##### Requisitos de Mídia e Copy

Três fotos que representem momentos distintos do atendimento. Um título e uma frase operacional por etapa.

##### Ordem obrigatória do DOM

1. Identificador e título da seção.
2. Três etapas numeradas.
3. Em cada etapa: número, título, texto curto e imagem.

##### Comportamento Mobile-First observado (375px)

Trilho estreito com cartão ativo perto de 417 × 624 px e imagem de 417 × 334 px (1,25:1). Bordas suavizadas na foto. O cabeçalho de 190 px mais o cartão e o vão ultrapassam a dobra de 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Três blocos sucessivos. Cada linha de 1284 × 680 px tem grupos de 308, 462 e 514 px, cerca de 24/36/40. A fotografia é vertical (514 × 680 px), com número isolado e título e texto no bloco central.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Número, descrição e foto identificam a mesma etapa. Manter a leitura em sequência.
- **Adaptáveis** — Direção fotográfica, tipo de numeração e paleta.

##### Animações & Interações observadas

- O trilho mostrou uma etapa em destaque e bordas das vizinhas na largura estreita. Gatilho exato da troca [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar o texto para explicar o que a pessoa faz ou encontra. Evitar repetir a mesma descrição entre etapas.

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
