# Visão do produto

## Problema que queremos resolver

Os supervisores precisam saber quem trabalha e quem folga, registrar faltas e outras exceções, encontrar cobertura de FT e consultar o mesmo estado da operação em celulares diferentes.

## Forma de uso desejada — confirmada

A rotina normal é calculada pelo aplicativo. O supervisor informa as exceções manualmente. Se não houver lançamento de falta, o funcionário é considerado presente pela regra do produto. A interface e o momento em que esse estado passa a valer serão definidos antes da implementação.

Quando uma FT precisar de cobertura, a consulta deve ajudar a localizar funcionários de folga e considerar o histórico proporcional de aceites e recusas na ordem de prioridade.

## Usuários

O uso por vários supervisores em celulares diferentes foi confirmado. A existência de acesso individual para funcionários, administradores separados e permissões por posto ainda será discutida.

## Capacidades desejadas

| Capacidade | Situação |
| --- | --- |
| Escala alternada de trabalho e folga | Confirmada |
| Turnos diurnos e noturnos com horários diferentes | Confirmada |
| Lançamento manual de faltas e exceções | Confirmado |
| Presença considerada por padrão sem falta lançada | Confirmada; detalhes operacionais em aberto |
| Consulta de funcionários de folga | Confirmada |
| Histórico e percentual de aceite de FT | Confirmados; política completa em aberto |
| Atualização compartilhada entre celulares pela internet | Confirmada |
| Relatórios, trilha de alterações e níveis de permissão | Propostos; detalhes a definir |
| Convites automáticos e notificações aos funcionários | Em aberto |

## Limites da preparação atual

O objetivo desta etapa é organizar os requisitos e depois definir aparência, navegação e funcionamento. A escolha entre aplicativo nativo, aplicativo web instalável ou outra plataforma permanece aberta.

Integrações com folha de pagamento, sistemas de ponto, biometria, localização e serviços de mensagens ainda não fazem parte de um escopo aprovado. O controle de presença por exceções não deve ser descrito como uma confirmação individual de batida de ponto.

## O que precisamos conhecer sobre a operação

- Quantidade de funcionários, supervisores e postos.
- Funções e requisitos para cobrir cada posto.
- Volume de faltas e FTs por mês.
- Como os convites são feitos e como a resposta chega ao supervisor.
- Quem pode corrigir registros e como são resolvidas divergências.
- Quais celulares e condições de internet serão usados.
