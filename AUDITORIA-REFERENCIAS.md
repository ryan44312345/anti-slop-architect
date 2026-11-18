# Auditoria do acervo

Base examinada: commit `47c4f4b92e0b2b09bccc5b5ce10602a292548fb0`. A auditoria documental abrange o guia de seleção, os oito arquivos de categoria e os sete lotes históricos. As 59 fichas têm IDs únicos e correspondência no índice.

| Categoria | Fichas |
| --- | ---: |
| Hero | 8 |
| Narrativa | 5 |
| Processo e recursos | 9 |
| Mídia | 6 |
| Prova social | 4 |
| Conversão | 8 |
| Navegação | 8 |
| Módulos especiais | 11 |

| Gravidade | Achado | Tratamento |
| --- | --- | --- |
| Alta | Campos deslocados, `undefined` e tag de fundo inválida em L7-NAV-04 | Reconstrução com DOM, medição e inspeção visual da fonte |
| Alta | 51 fichas rotulavam a variante estreita como 375 px e o desktop como 1440 px | Viewports históricos explícitos por ficha. Altura de 812 px tratada como inferência |
| Média | A tag de scroll inclui tanto cabeçalhos persistentes quanto palcos de conteúdo | A classificação por composição distingue os dois usos. Convém separar esses conceitos em futura revisão do guia |
| Média | O índice descrevia o tom, mas ajudava pouco a decidir entre estruturas parecidas | Composição, condição de seleção e tipo de navegação registrados |
| Média | Dependência de mídia e diversidade desiguais entre categorias | Decisões por ficha e lacunas registradas abaixo |

## Sobreposições e diversidade

- **L1-HERO-01 e L7-HERO-03.** Os dois exigem recorte forte e texto sobre ou junto à mídia. O primeiro organiza um manifesto e disciplinas. O segundo usa o busto para organizar título e atalhos. Ambos têm uso, mas oferecem pouca variedade quando o projeto não tem retrato preparado.
- **L4-FEAT-03, L5-FEAT-01, L6-FEAT-01 e L6-FEAT-02.** Dividem a jornada em passos. A foto arquitetônica situa um serviço, a documentação clínica explica o atendimento, a nota orienta o paciente e a sequência domiciliar explica a logística. Uma nova ficha de processo deveria mudar a forma de decidir ou explorar, por exemplo, um processo ramificado com saídas distintas.
- **L5-CONV-01 e L5-CONV-02.** Compartilham comparação por planos. Mantenha ambas para distinguir escolha entre dois formatos e recomendação dentro de três níveis. Um próximo padrão de conversão pode priorizar formulário curto de qualificação sem planos.
- **L1-SHOW-01 e L1-SHOW-02.** Mosaico denso para leitura simultânea e pares alternados para leitura pausada. As duas geometrias atendem portfólios com materiais diferentes. Todas as seis fichas de vitrine têm tag Foto-Crítica, o que limita projetos com pouco material visual.
- **Navegação.** Oito fichas incluem dois headers, dois footers, três diretórios e um bloco de visita. Um menu interno orientado a páginas extensas ou documentação ampliaria o repertório. A newsletter do Ruota e o fechamento por escritórios do Caldren exigem conteúdos distintos.
- **Prova social.** Quatro padrões com fundo escuro cobrem nota e relatos, gráfico, relato com foto e garantia. Uma ficha de prova clara sem fotos, por exemplo, citação demonstrável associada a um caso, ampliaria a escolha.
- **Aberturas.** Cinco de oito têm tag Escuro, dois Adaptável e um Claro. Seis exigem mídia crítica. Uma abertura clara conduzida apenas pela tipografia e outra conduzida por busca ou escolha do usuário são lacunas distintas.
- **Distribuição geral.** As tags registram 30 Escuro, 19 Claro e 10 Adaptável. Adaptável descreve portabilidade e não equivale a fundo misto observado. Há 18 Tipográfico, 14 Foto-Adaptável e 27 Foto-Crítica. Os módulos especiais concentram cardápios, imóveis e seleção/comparação. Projetos editoriais e catálogos independentes de fotografia ainda têm pouca cobertura.

## Evidências e limites

- **Reinspeção ao vivo.** L7-NAV-04 em 1363 × 936, 545 × 374 e 454 × 312 px CSS. A largura útil foi de 1348, 539 e 449 px. O navegador foi operado em ambiente virtual. A newsletter não foi enviada e os destinos externos genéricos não foram acionados.
- **Revisão documental.** As demais 58 fichas têm observações históricas preservadas e análise de aplicação marcada como inferência. As medidas continuam nas condições originais. A revisão não constitui nova verificação visual, de teclado ou de estados interativos dessas 58 fichas.
- **Validação.** `python3 scripts/validate_references.py` checa IDs históricos, destinos, títulos, fontes, campos e vocabulário das tags. URLs passaram em checagem de sintaxe. A disponibilidade ao vivo foi confirmada para Ruota. `git diff --check` passou e os arquivos históricos e o guia permaneceram idênticos.
- **Pesquisa complementar.** As lacunas acima são prioridades de pesquisa. Nenhum padrão novo foi catalogado neste conjunto de alterações.

## Recomendações para revisão futura do guia

1. Separar header persistente de scrollytelling e tornar sticky uma escolha condicionada à função da seção.
2. Pedir duas alternativas de composição quando vários candidatos tenham o mesmo arranjo ou dependência de mídia.
3. Na seleção, usar objetivo, tipo de conteúdo e risco de adaptação antes da descrição de tom.
4. Retestar a implementação em viewport real estreito, teclado e movimento reduzido, com evidência própria do projeto. Usar as larguras de auditoria apenas para estimar proporções.
5. Manter liberdade para paletas planas, tipografia sóbria e grades convencionais quando servirem ao conteúdo.
