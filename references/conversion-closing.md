# conversion-closing.md

#### L1-CONV-01 — Fechamento de contato com palco e email visível

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L1-CONV-01`
- **Nome do padrão** — Fechamento de contato com palco e email visível
- **Fonte** — [Alter](https://alter.framer.photos/)
- **Nichos indicados** — designers independentes, consultorias criativas, pequenos estúdios

##### Requisitos de Mídia e Copy

Pode funcionar com palco escuro, sem depender de foto. Usar convite curto, email e links sociais.

##### Ordem obrigatória do DOM

1. Título semântico de contato e link para a página de contato.
2. Estado de disponibilidade e convite curto.
3. Email clicável.
4. Links sociais.

##### Comportamento Mobile-First observado de fato (449 px)

Palco escuro de 449 × 640 px. A faixa de contato começa a cerca de 435 px do início da seção, ocupa 409 px e tem margem de 20 px. Email em Switzer a 22 px. Os quatro links sociais aparecem depois, em linha, com caixas de 44 px de altura e fonte monoespaçada de 11 px. A área do link de fundo mede a seção inteira no DOM.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, palco de 936 px de altura. O convite e o email estão próximos ao canto inferior esquerdo, com margem de 40 px e email de cerca de 35 px com sublinhado laranja. Redes no canto oposto. O conteúdo de contato continua legível mesmo quando a região central fotografada aparece vazia. O título semântico de contato tem caixa de 1 × 1 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter email em destaque, redes secundárias e acesso independente a cada link.
- **Adaptáveis** — Cor de fundo, fonte, sublinhado e destinos.

##### Animações & Interações observadas

- O email usa `mailto:` e há um link absoluto no palco para a página de contato. Animação do fundo e reação visual de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Dar ao email peso visual suficiente para funcionar como ação principal.
- Usar um endereço real no projeto final e manter as redes como ações secundárias.
- Garantir que o link amplo do palco preserve acesso por mouse e teclado aos links de email e redes.

#### L1-CONV-02 — Comparação de combos com ação por opção

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L1-CONV-02`
- **Nome do padrão** — Comparação de combos com ação por opção
- **Fonte** — [Ligatra](https://only-instance-526558.framer.app/)
- **Nichos indicados** — hamburguerias, delivery, cardápios com combos

##### Requisitos de Mídia e Copy

Recortes de produto em escala comparável. Usar etiqueta breve, nome, descrição, preço, CTA e inclusões.

##### Ordem obrigatória do DOM

1. Título de escolha.
2. Lista de combos. Cada item contém imagem, etiqueta curta, nome, descrição, preço, ação de pedido e lista de itens incluídos.

##### Comportamento Mobile-First observado de fato (449 px)

Três cartões em uma coluna de 409 px com margem de 20 px. Título Bowlby One de 34 px em duas linhas. Cada imagem mede 365 × 200 px, aproximadamente 1,83:1. O CTA mede cerca de 180 × 52 px. Os cartões usam planos largos em marrom muito escuro, com cantos arredondados e foto recortada do produto.

##### Expansão Desktop (1024px+) observada de fato

A 1348 px, três colunas iguais de cerca de 380 px dentro de uma faixa de 1180 px, com vãos de cerca de 20 px. Título de 52 px. Imagens de 324 × 230 px, cerca de 1,41:1. Chamadas amarelas de 188 × 52 px. Preços e botões alinhados entre as três opções na amostra desktop.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter mesma ordem interna e ação específica por opção, com preços comparáveis.
- **Adaptáveis** — Fotos, paleta, tipografia e estilo do botão.

##### Animações & Interações observadas

- Os três CTAs apontam para um endereço de demonstração no DOM. Fluxo de pedido e mudança visual específica ao hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar o mesmo tamanho aparente e o mesmo eixo para as fotos dos produtos.
- Aplicar a mesma ordem de informações em todos os cartões para facilitar a comparação de preço e composição.
- Usar rótulos curtos que indiquem uma diferença real e trocar o destino demonstrativo pelo pedido da opção correspondente.

#### L2-CONV-01 — Unidades com pedido e rota por loja

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L2-CONV-01`
- **Nome do padrão** — Unidades com pedido e rota por loja
- **Fonte** — [Ligatra](https://only-instance-526558.framer.app/)
- **Nichos indicados** — redes de restaurantes, cafeterias e lojas físicas

##### Requisitos de Mídia e Copy

Uma foto por unidade, endereço completo, horários em linhas separadas e dois rótulos curtos de ação.

##### Ordem obrigatória do DOM

1. Identificador da seção e H2.
2. Lista de unidades.
3. Em cada unidade: foto, nome, endereço, horários e ações de pedido e rota.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 409 px com margem de 20 px e raio de 22 px. Imagens de aproximadamente 409 × 200 px (2,05:1). Cartões de 412–449 px cabem isoladamente em 812 px. A lista completa excede a dobra.

##### Expansão Desktop observada (1024px+ / 1440px)

Três colunas de 380 px com vão de 20 px, superfície clara e cartões com raio de 28 px. Imagens de 380 × 240 px (1,58:1). A 1090 px já havia uma coluna, compatível com a faixa CSS de 1200 px.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Cada ação pertence à unidade no mesmo cartão. A foto precede os dados operacionais.
- **Adaptáveis** — Paleta, imagens e estilos de botão.

##### Animações & Interações observadas

- Links de pedido e rota identificados no DOM. Efeito visual de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Permitir alturas diferentes conforme os horários. Direcionar pedido e rota à unidade correta.

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

#### L5-CONV-01 — Comparação de dois pacotes por visita

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L5-CONV-01`
- **Nome do padrão** — Comparação de dois pacotes por visita
- **Fonte** — [Dental Point](https://dental-point-clinic.framer.website/)
- **Nichos indicados** — clínicas, estúdios e serviços com pacotes

##### Requisitos de Mídia e Copy

Nome e público de cada pacote, preço com unidade, cerca de quatro inclusões e um CTA por opção. Dispensa fotos.

##### Ordem obrigatória do DOM

1. Título e introdução.
2. Dois planos.
3. Em cada plano: nome, perfil indicado, preço e unidade, lista de itens e CTA.

##### Comportamento Mobile-First observado (375px)

Os planos se empilham em faixa de 417 px. O primeiro cartão mede 385 × 516 px, com área interna de 353 px e CTA de 48 px de altura. Um cartão cabe isoladamente em 812 px.

##### Expansão Desktop observada (1024px+ / 1440px)

Dois cartões de cerca de 618 × 622 px. Superfície creme no primeiro e preto no segundo. Conteúdo interno de 538 px e botões de largura própria.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Manter unidade do preço ao lado do valor e repetir a sequência de leitura nos dois planos.
- **Adaptáveis** — Cores, tipografia, ícones e destaque visual.

##### Animações & Interações observadas

- Links de agendamento identificados. Hover e conclusão do agendamento [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Explicitar o que está incluído e se o preço é por visita. Usar contraste para hierarquia, com leitura equivalente nos dois planos.

#### L5-CONV-02 — Três níveis de consultoria com plano central destacado

- **Categoria destino** — `conversion-closing.md`
- **ID sugerido** — `L5-CONV-02`
- **Nome do padrão** — Três níveis de consultoria com plano central destacado
- **Fonte** — [Koddam](https://koddam.framer.website/)
- **Nichos indicados** — consultorias, serviços recorrentes e SaaS

##### Requisitos de Mídia e Copy

Nome, público-alvo em uma frase, valor com recorrência, cerca de quatro inclusões e CTA por plano.

##### Ordem obrigatória do DOM

1. Identificador, título e introdução.
2. Grade de planos.
3. Em cada plano: nome, descrição, preço, inclusões e ação.

##### Comportamento Mobile-First observado (375px)

Uma coluna de 419 px, margem de 15 px. Cada cartão mede cerca de 467 px de altura e tem CTA de 379 × 40 px. Cabe o título e um plano em aproximadamente 812 px, conforme os espaçamentos medidos.

##### Expansão Desktop observada (1024px+ / 1440px)

Três cartões de 416 × 481 px com vão de 20 px. Cartão central verde-claro e dois brancos. CTAs pretos de 376 × 40 px alinhados na base.

##### Invariantes vs. Adaptáveis

- **Invariantes** — Mesma hierarquia de preço e inclusões nos três cartões. A comparação preserva a ordem dos planos.
- **Adaptáveis** — Cores, tipografia, recorrência e quantidade de benefícios.

##### Animações & Interações observadas

- Links Get Started presentes. Transição visual de hover [NÃO OBSERVADO].

##### Regras Anti-Slop específicas daquela seção

- Usar o destaque para justificar a escolha central com uma diferença concreta de escopo. Alinhar preço e botão mesmo quando o texto variar.

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
