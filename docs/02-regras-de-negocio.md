# Regras de negócio

Este documento separa o que foi confirmado das sugestões que ainda precisam de decisão. Não fixa tecnologia nem implementa as regras.

## 1. Escala de trabalho e folga

**Confirmado:** na rotina descrita, o funcionário trabalha em um dia e folga no seguinte. O aplicativo deve calcular as datas futuras para cada funcionário.

**Necessidade a detalhar:** cadastrar uma data de referência individual, junto ao turno, para saber em qual lado da alternância cada pessoa está. A conta deve continuar entre meses e anos; a paridade do dia do mês, sozinha, não resolve a escala.

### Horários informados

| Período | Entrada | Saída | Observação |
| --- | --- | --- | --- |
| Diurno | 06h | 18h | Informado pelo responsável |
| Diurno | 07h | 19h | Informado pelo responsável |
| Noturno | 18h | 06h do dia seguinte | Informado pelo responsável |
| Noturno | 19h | 07h do dia seguinte | Informado pelo responsável |
| Noturno | 18h | 08h do dia seguinte | Informado pelo responsável; soma 14 horas e requer confirmação |

A associação de horários a postos e as mudanças de horário por funcionário serão detalhadas depois.

## 2. Exceções manuais

**Confirmado:** faltas, férias e outras alterações serão lançadas manualmente. Não é necessário registrar individualmente o comparecimento de todos os funcionários no funcionamento normal.

**Proposto:** distinguir falta, férias, licença, folga autorizada e troca de turno, para que situações diferentes não sejam contadas como a mesma ocorrência. Categorias e efeitos exatos permanecem em aberto.

**Em aberto:** decidir se cada exceção mantém a alternância original ou altera a referência de escala. A sugestão inicial é que uma exceção pontual não reinicie automaticamente o ciclo.

## 3. Presença por padrão

**Confirmado:** sem lançamento de falta, o aplicativo deve considerar que o funcionário compareceu.

**Proposto:** representar isso como presença presumida, distinguindo-a de uma confirmação manual. Antes do turno, mostrar previsão; durante o turno, mostrar andamento; depois do encerramento, aplicar a regra padrão se não houver exceção.

**Em aberto:** momento do fechamento, nomes dos estados na interface, correções retroativas e reflexo nos relatórios. A proposta de fechamento após o fim do turno ainda não foi aprovada como regra definitiva.

Um dia de folga não deve gerar uma falta. Férias e outros afastamentos precisam ser tratados conforme sua categoria, sem presumir que são ausências injustificadas.

## 4. Datas de turnos noturnos

**Proposto:** identificar o turno pela data de início e manter entrada e saída completas, inclusive quando atravessam a meia-noite.

**Em aberto:** convenção de exibição e consulta. A tela de funcionários de folga e a seleção para FT precisam considerar que alguém pode estar saindo de um turno na manhã da data consultada.

## 5. Consulta e cobertura de FT

**Confirmado:** mostrar quem está de folga para ajudar os supervisores a encontrar pessoas que possam fazer FT.

**Proposto:** consultar a disponibilidade para a data e o intervalo exatos da FT, considerando férias, afastamentos, outros turnos e requisitos do posto. As regras de elegibilidade e de intervalos de descanso ainda serão definidas.

**Em aberto:** como registrar convite, aceite, recusa, ausência de resposta, desistência, cancelamento e comparecimento. Não foi definido se o funcionário responderá dentro do aplicativo ou se o supervisor lançará o resultado.

O efeito de uma FT na escala normal também deve ser decidido explicitamente; não reiniciar o ciclo sem uma regra aprovada.

## 6. Estatística e prioridade de FT

**Confirmado:** o percentual deve variar proporcionalmente aos aceites e recusas. Quem aceita todos os convites respondidos tem 100% nesse histórico. A intenção é usar esse indicador para ajudar a ordenar a prioridade de convite entre os disponíveis.

### Exemplos aritméticos

Nos exemplos abaixo, cada convite tem uma resposta definitiva: aceite ou recusa.

| Aceites | Recusas | Total de respostas | Percentual de aceite |
| ---: | ---: | ---: | ---: |
| 1 | 0 | 1 | 100% |
| 1 | 1 | 2 | 50% |
| 5 | 1 | 6 | 83,33% |
| 0 | 1 | 1 | 0% |

Nessas condições, percentual = aceites / (aceites + recusas) × 100. Quando o total for zero, a proposta é mostrar "sem histórico"; não há taxa observada a calcular.

**Em aberto:** tratamento de não respondidos e cancelados, histórico de funcionários novos, desempates, período do histórico, quantidade mínima de convites e eventual separação por turno ou posto.

**Proposto:** registrar comparecimento às FTs aceitas em indicador separado. Uma recusa de convite e uma falta após aceitar são eventos diferentes. Também é recomendável exibir a quantidade de respostas junto da porcentagem, por exemplo "83,33% — 5 de 6".

O percentual é um histórico observado, não uma garantia de resposta futura.

## 7. Compartilhamento entre celulares

**Confirmado:** o aplicativo depende de internet e compartilha informações entre supervisores. Uma falta registrada em um celular deve aparecer nos demais.

**Proposto:** manter uma base central, mostrar confirmação de salvamento e registrar autor e horário das alterações. A tecnologia dessa base ainda será escolhida.

**Em aberto:** o que acontece sem conexão, como tratar alterações simultâneas e quais usuários podem corrigir registros. Não se deve apresentar uma mudança como sincronizada antes de sua confirmação.
