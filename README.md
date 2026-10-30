# MC SEGURANÇAS

Planejamento do aplicativo para organizar escalas, faltas e folgas trabalhadas (FTs) da MC Seguranças.

**Fase atual: definição do produto e do visual.** Esta preparação contém documentação e organização do projeto. O desenvolvimento do aplicativo começará quando o responsável orientar o início da implementação.

## Objetivo

Permitir que supervisores consultem a escala 12x36, registrem exceções e encontrem funcionários de folga para cobrir FTs, usando informações compartilhadas entre celulares pela internet.

## Diretrizes confirmadas

- Calcular automaticamente trabalho e folga na escala de um dia de trabalho seguido de um dia de folga.
- Registrar faltas, férias e outras alterações manualmente.
- Considerar presença por padrão quando não houver uma falta registrada; o momento e a apresentação desse status ainda serão definidos.
- Mostrar os funcionários de folga na data consultada.
- Registrar o histórico de aceites e recusas de FT e calcular percentuais proporcionais para ajudar a ordenar a prioridade de convite.
- Compartilhar as atualizações entre os celulares dos supervisores pela internet.
- Definir o visual e os fluxos antes de programar o aplicativo.

## Documentação

| Documento | Conteúdo |
| --- | --- |
| [Visão do produto](docs/01-visao-do-produto.md) | Objetivo, usuários e limites desta etapa |
| [Regras de negócio](docs/02-regras-de-negocio.md) | Escala, exceções, presença, FT e sincronização |
| [Briefing de design](docs/03-briefing-de-design.md) | Decisões visuais e fluxos que vamos definir |
| [Decisões em aberto](docs/04-decisoes-em-aberto.md) | Perguntas que ainda precisam ser resolvidas |
| [Próximas etapas](docs/05-proximas-etapas.md) | Ordem proposta para avançar até a implementação |
| [Transição do repositório](docs/06-transicao-do-repositorio.md) | Registro do reaproveitamento e da cópia anterior |

## Como ler as definições

**Confirmado** identifica uma orientação expressa do responsável. **Proposto** identifica uma sugestão para discussão. **Em aberto** identifica uma decisão ainda não tomada. Uma sugestão registrada não significa aprovação.

## Repositório

Este espaço foi reaproveitado para o MC SEGURANÇAS por orientação do responsável. A branch principal é `main`, na conta `zakbodie`, e contém a preparação documental do novo projeto.

O nome desejado no GitHub é `mc-segurancas`. A renomeação do endereço é uma configuração administrativa pendente; o título e a finalidade do projeto já são MC SEGURANÇAS. A visibilidade atual do repositório é pública.

A versão anterior foi preservada na branch `backup/sistema-ascensao-20261030-4e006a8`. Esse material é histórico e não define o aplicativo MC SEGURANÇAS.

Plataforma, linguagem, framework, banco de dados, hospedagem, identidade visual, licença e modelo comercial permanecem em aberto. Valores discutidos durante a análise comercial são estimativas, não um preço contratado.

Usar exemplos fictícios nesta fase. Dados reais de funcionários, senhas, credenciais e documentos internos não devem entrar no histórico do repositório.

Preparação inicial: 30/10/2026.
