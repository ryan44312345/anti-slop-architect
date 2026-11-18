# social-proof.md

#### L2-PROOF-01 — Nota agregada com trilha de depoimentos

- **Categoria destino** — `social-proof.md`
- **ID sugerido** — `L2-PROOF-01`
- **Nome do padrão** — Nota agregada com trilha de depoimentos
- **Fonte** — [Ligatra](https://only-instance-526558.framer.app/)
- **Nichos indicados** — restaurantes, serviços locais e franquias

**Evidência histórica** — Lote 2. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Nota e volume em duas linhas. Citações de cerca de 10–20 palavras com nome e fonte.

##### Ordem obrigatória do DOM

1. Nota e volume de avaliações.
2. Controles anterior e próximo.
3. Trilha horizontal com estrelas, citação, nome e fonte em cada cartão.

##### Comportamento em largura estreita

Controles de 48 px abaixo do título. Cartão de 300 × 320 px, raio de 22 px, recuo inicial de 20 px e vão de 14 px. Parte do próximo cartão fica visível. A caixa da seção mediu 692 px e cabe em 812 px a partir de seu topo.

##### Comportamento em desktop

Título e setas na mesma linha. Cartões de 380 × 360 px, raios de 28 px, recuo inicial de 84 px e vãos de 20 px. Três cartões mais parte do quarto. A trilha permanece horizontal nas amostras intermediárias.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Resumo precede relatos. Manter navegação acessível e pista visual do próximo cartão.
- **Adaptáveis** — Cor das estrelas, fundo, fonte e tamanho dos cartões.

##### Animações & Interações observadas

- Clique em Next no desktop → a trilha avançou cerca de 399 px, um cartão mais o vão. Efeito específico de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar nota e volume com origem verificável. Manter os controles fora da caixa de citação.

##### Direção de arte e aplicação

[INFERIDO] **Trilha navegável.** A nota agrega e as citações explicam; mantenha fonte e contexto da nota junto ao número.

#### L5-PROOF-01 — Indicadores de impacto com gráfico de quatro períodos

- **Categoria destino** — `social-proof.md`
- **ID sugerido** — `L5-PROOF-01`
- **Nome do padrão** — Indicadores de impacto com gráfico de quatro períodos
- **Fonte** — [Koddam](https://koddam.framer.website/)
- **Nichos indicados** — consultorias, serviços B2B e empresas de tecnologia

**Evidência histórica** — Lote 5. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Três valores com unidade, rótulo e frase. Quatro barras com percentual e período. Dispensa fotos.

##### Ordem obrigatória do DOM

1. Identificador da seção.
2. Três indicadores com valor, rótulo e explicação.
3. Gráfico com quatro valores e respectivos períodos.

##### Comportamento em largura estreita

Faixa de 419 px com margem de 15 px. Indicadores empilhados em área de 593 px. Gráfico abaixo com 300 px e quatro barras de cerca de 97 px. O conjunto ultrapassa 812 px.

##### Comportamento em desktop

Faixa de 1288 px e altura de seção de 746 px. Identificador e três indicadores em linha com divisórias. Gráfico de 1006 × 300 px, deslocado para alinhar com os indicadores. Uma barra verde-clara contrasta com as demais brancas sobre verde escuro.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Cada barra mantém valor e período. A escala visual deve representar os números proporcionalmente.
- **Adaptáveis** — Paleta, fontes, períodos e métricas.

##### Animações & Interações observadas

- Barra destacada visualmente. Gatilho de destaque e resposta ao hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Identificar a grandeza, período e fonte do gráfico. Usar números verificáveis ao adaptar o módulo.

##### Direção de arte e aplicação

[INFERIDO] **Indicadores com gráfico.** Só use gráfico quando houver séries comparáveis; informe unidade, período e fonte.

#### L6-PROOF-01 — Depoimentos em coluna ao lado de uma foto de execução

- **Categoria destino** — `social-proof.md`
- **ID sugerido** — `L6-PROOF-01`
- **Nome do padrão** — Depoimentos em coluna ao lado de uma foto de execução
- **Fonte** — [Silenus](https://silenus.framer.website/)
- **Nichos indicados** — barbearias, salões e serviços artesanais

**Evidência histórica** — Lote 6. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Uma foto de execução, três depoimentos curtos e avatares opcionais. Nome e avaliação em cada registro.

##### Ordem obrigatória do DOM

1. Identificador, título e introdução.
2. Foto de execução.
3. Três cartões com citação, identificação e avaliação.

##### Comportamento em largura estreita

Pilha em faixa de 409 px. Imagem interna de 491 × 480 px antes do recorte visual. Cabeçalho de 169 px e corpo de 1102 px, além de respiros. O conjunto excede 812 px.

##### Comportamento em desktop

Faixa de 1268 px com fotografia à esquerda e três cartões contornados à direita. Imagem interna de 609 × 680 px em uma amostra, com recorte para a área visual. Avatares de 48 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Três vozes distintas, cada citação com autoria e avaliação correspondente.
- **Adaptáveis** — Imagem, cor de borda, tipografia e estilo de avatar.

##### Animações & Interações observadas

- [NÃO OBSERVADO]

##### Regras Anti-Slop específicas daquela seção

- Usar a foto como contexto do serviço. Manter os relatos verificáveis e fáceis de distinguir.

##### Direção de arte e aplicação

[INFERIDO] **Depoimentos com foto lateral.** A foto contextualiza o trabalho; cada relato precisa de autoria e identificação independentes da imagem.

#### L6-PROOF-02 — Garantia de retorno com três condições explícitas

- **Categoria destino** — `social-proof.md`
- **ID sugerido** — `L6-PROOF-02`
- **Nome do padrão** — Garantia de retorno com três condições explícitas
- **Fonte** — [Chapter Barbershop](https://chapterbarbershop.framer.website/)
- **Nichos indicados** — barbearias, salões e serviços presenciais

**Evidência histórica** — Lote 6. Desktop 1363 × 936 px CSS; estreito 454 × 312 px CSS por zoom (449 px úteis). Comparação histórica de overflow: Desktop 1348 = 1348 · Mobile 449 = 449. As descrições abaixo vêm desse registro. Encaixe a 812 px, quando mencionado, é [INFERIDO]. 375 × 812 px, toque e breakpoint exato são [NÃO OBSERVADO] salvo evidência explícita.

##### Requisitos de Mídia e Copy

Uma afirmação curta com prazo, uma explicação de até duas frases e três condições de uma linha.

##### Ordem obrigatória do DOM

1. Título e explicação da garantia.
2. Faixa de termos em destaque.
3. Três condições com título e explicação.

##### Comportamento em largura estreita

Título e explicação em área de 401 px. Faixa de 132 px e condições em bloco de 265 px. Seção de 709 px, dentro de uma dobra local de 812 px.

##### Comportamento em desktop

Abertura de 1320 px, título de 640 px e faixa intermediária. Três condições em linha com cerca de 379 × 77 px cada. Fundo escuro e texto de alto contraste.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Prazo, alcance e custo ficam explícitos também fora da faixa de destaque.
- **Adaptáveis** — Tipografia, cores e redação conforme a garantia real.

##### Animações & Interações observadas

- Movimento da faixa e interação [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar condições testáveis com prazo e custo explícitos. Evitar depender de texto repetido para explicar como solicitar o retorno.

##### Direção de arte e aplicação

[INFERIDO] **Garantia por condições.** Use somente quando a política puder ser cumprida; mantenha as exceções perto da promessa.
