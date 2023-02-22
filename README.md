# Hand-A-Game
Disciplina: Engenharia de Software II
Prof. Dr. Ricardo Argenton Ramos

## Resumo de Funcionalidades
Uma plataforma que busca gerenciar empréstimo de jogos entre pessoas, sendo esses
jogos físicos ou digitais de diversas plataformas.
Depois de criar uma conta, um usuário pode cadastrar jogos que está disposto a emprestar
na plataforma e outros podem buscar por esses jogos dentro da mesma.
Uma vez encontrado um jogo que deseja-se pegar emprestado, a plataforma envia uma
notificação para o dono do jogo. Se ele aceitar a solicitação de empréstimo, as informações
de contato dos usuários (dono e beneficiário) serão trocadas para que possam se
comunicar.
Adicionalmente, é possível editar jogos já cadastrados, visualizar histórico de empréstimos
e fazer busca com filtros por jogos.
## Diagrama de Caso de Uso
[alt text](https://github.com/amaropedro/hand-a-game/blob/main/Diagrama.png?raw=true)
## REQUISITOS/FUNCIONALIDADES:
- Cadastro
- Login
- Solicitar jogo emprestado
- Adicionar jogo virtual/físico
- Atualizar jogo virtual/físico
- Remover jogo virtual/físico
- Visualizar histórico de empréstimos
- Reportar atraso no prazo de um empréstimo

### Fluxo: Fazer login
1. O usuário (U1) acessa a plataforma
2. U1 preenche os campos ‘usuário’ e ‘senha’
3. U1 clica em ‘login’
4. A tela de perfil aparece
#### Fluxo alternativo: Usuário ou senha não constam.
3.1. Um popup com a mensagem ‘usuário ou senha não constam’ aparece
3.2. O usuário clica em ‘criar uma conta’
Segue para o fluxo CRIAR UMA CONTA
### Fluxo: Criar uma conta
1. O usuário (U1) acessa a plataforma
2. U1 clica em ‘criar uma conta’
3. A tela de cadastro aparece
4. U1 preenche os campos (USERNAME, SENHA, CONFIRMAR SENHA, EMAIL,
CIDADE E CONTATO)
5. U1 clica em ‘fazer cadastro’
6. Um popup com a mensagem ‘CADASTRO REALIZADO COM SUCESSO’ aparece
7. A tela de perfil aparece
#### Fluxo alternativo: Campos incorretos
    5.1. Um popup com a mensagem ‘CAMPOS INCORRETOS OU NÃO
PREENCHIDOS’ aparece.
    5.2. U1 clica em ‘ok’
    5.3. U1 corrige os campos
    Contínua em 5 no fluxo principal
#### Fluxo alternativo: Campos não preenchidos
    5.1. Um popup com a mensagem ‘CAMPOS INCORRETOS OU NÃO
PREENCHIDOS’ aparece.
    5.2. U1 clica em ‘ok’
    5.3. U1 preenche os campos que haviam faltado
    Contínua em 5 no fluxo principal
#### Fluxo alternativo: Username já cadastrado
    5.1. Um popup com a mensagem ‘USERNAME JÁ ESTÁ CADASTRADO A
PLATAFORMA’ aparece.
    5.2. U1 clica em ‘ok’
    5.3. U1 escolhe um outro username
    Continua em 5 no fluxo principal
### Fluxo: Cadastrar um jogo à plataforma
    Pré-requisito: o Usuário (U1) já está logado na plataforma.
1. U1 clica em ‘meus jogos’
2. A tela meus jogos aparece
3. U1 clica no botão em formato de ‘+’ (cadastrar um jogo)
4. Um popup de cadastro aparece
5. U1 preenche os atributos do jogo (TITULO, FOTO DA CAPA, GÊNEROS, FÍSICO E
TEMPO MÁXIMO DE EMPRÉSTIMO)
6. U1 escolhe dentre as plataformas listadas para o atributo PLATAFORMA. Sendo
elas: Steam, Epic Games, Nintendo, Xbox, Playstation, Outro.
7. U1 clica em confirmar
8. Um popup com a mensagem ‘JOGO CADASTRADO COM SUCESSO’ aparece
#### Fluxo alternativo: Campos não preenchidos
    7.1. Um popup com a mensagem ‘CAMPOS INCORRETOS OU NÃO
PREENCHIDOS’ aparece.
    7.2. U1 clica em ‘ok’
    7.3. U1 preenche os campos que haviam faltado
    Contínua em 7 no fluxo principal
### Fluxo: Remover um jogo da plataforma
    Pré-requisitos: o Usuário (U1) já está logado na plataforma, U1 tem um jogo
cadastrado na plataforma.
1. U1 clica em ‘meus jogos’
2. A tela meus jogos aparece
3. U1 clica no jogo que deseja remover da plataforma
4. O popup com as características do jogo aparece
5. U1 clica em ‘remover jogo’
6. Um popup de confirmação aparece
7. U1 clica em ‘remover’
8. Um popup com a mensagem ‘JOGO REMOVIDO COM SUCESSO’ aparece
9. A tela de meus jogos volta a aparecer
#### Fluxo alternativo: Erro, jogo está emprestado
    7.1. Um popup com a mensagem ‘ERRO, JOGO ESTÁ ATUALMENTE
EMPRESTADO. ESPERE O TEMPO DE EMPRÉSTIMO ACABAR.’
    7.2. U1 clica em ‘ok’
    7.3. O popup com as características do jogo volta a aparecer
    Fim do fluxo alternativo
### Fluxo: Recebendo e visualizando notificações
    Pré-requisitos: o Usuário (U1) já está logado na plataforma.
1. O sistema (S) emite uma notificação para U1
2. Em qualquer tela da plataforma, um pontinho vermelho com o número de
notificações será exibido acima do botão ‘notificações’
3. U1 clica em ‘notificações’
4. A tela de notificações aparece, listando as atuais notificações.
### Fluxo: Editar jogo
    Pré-requisitos: o Usuário (U1) já está logado na plataforma, U1 tem um jogo
cadastrado na plataforma.
1. U1 clica em ‘meus jogos’
2. A tela meus jogos aparece
3. U1 clica no jogo que deseja editar
4. O popup com as características do jogo aparece
5. U1 clica em ‘editar’
6. U1 edita os campos que deseja
7. U1 clica em ‘salvar alterações’
8. O popup com as características do jogo volta a aparecer
#### Fluxo alternativo: Erro, jogo está emprestado
    7.1. Um popup com a mensagem ‘ERRO, JOGO ESTÁ ATUALMENTE
EMPRESTADO. ESPERE O TEMPO DE EMPRÉSTIMO ACABAR.’
    7.2. U1 clica em ‘ok’
    7.3. O popup com as características do jogo volta a aparecer
    Fim do fluxo alternativo
### Fluxo: Pegar um jogo emprestado
    pré-requisito: o Usuário (U1) já está logado na plataforma, um outro usuário (U2)
cadastrou um jogo à plataforma.
1. U1 clica em ‘emprestados’
2. U1 clica no botão em formato de ‘+’ (pegar um jogo emprestado)
3. A tela de pesquisa aparece
4. U1 pesquisa pelo nome do jogo que deseja
5. Uma resposta com os jogos disponíveis aparece
6. U1 seleciona um filtro da plataforma desejada (Steam, Epic Games, Nintendo, Xbox,
Playstation, Qualquer [Default])
7. Uma nova resposta aparece, correspondente ao filtro
8. U1 seleciona um filtro de tempo máximo de empréstimo desejado (1 mês, 2 meses,
3 meses, 4 meses, 5 meses ou mais, Qualquer [Default])
9. Uma nova resposta aparece, correspondente ao filtro
10. U1 seleciona o jogo que gostaria de pedir emprestado
11. Um popup de confirmação aparece
12. O sistema (S) manda a solicitação do beneficia (U1) para o dono do jogo (U2) como
uma notificação
13. U2 clica em notificações
14. A tela de notificações aparece
15. U2 vai ao campo onde a solicitação de empréstimo de U1 aparece e clica em
‘emprestar jogo’
16. U1 recebe uma notificação informando que ele tem acesso ao jogo, juntamente com
o contato de U2 para obter as credenciais ou marcar para buscar o jogo físico.
#### Fluxo alternativo: U2 não aceita a solicitação
    15.1. U2 vai ao campo onde a solicitação de empréstimo de U1 aparece e clica no
botão em formato de ‘x’ (excluir solicitação)
Fim do fluxo alternativo.
#### Fluxo alternativo: Adicionar jogo físico aos filtros
    9.1 U1 vai ao filtro físico e seleciona a opção SIM dentre (SIM, NÃO,
QUALQUER [Default])
    9.2 Uma nova resposta aparece, agora apenas com jogos disponíveis na
cidade de U1.
    Contínua em 10 no fluxo principal
### Fluxo: Visualizar histórico de empréstimos
    Pré-requisitos: o Usuário (U1) já está logado na plataforma, U1 tem um jogo
cadastrado na plataforma.
1. U1 clica em ‘meus jogos’
2. A tela meus jogos aparece
3. U1 clica no jogo que deseja visualizar
4. O popup com as características do jogo aparece
5. U1 vê o histórico de empréstimos desse jogo na tabela de histórico de empréstimos
### Fluxo: Reportar Atraso
1. O Sistema (S) detecta um atraso na devolução de um jogo
2. S notifica o dono do jogo (U1) e aquele que pegou-o emprestado (U2)
#### Fluxo alternativo: Jogo não-físico -> adicionar tolerância.
    2.1. O dono do jogo (U1) abre o app
    2.2. U1 clica em notificações
    2.3. A tela de notificações aparece
    2.4. U1 clicar na notificação de atraso
    2.5. U1 clica em adicionar tolerância
    2.6. U1 seleciona o tempo de tolerância (1 dia, 1 semana, 1 mês, 2 meses ou
mais) e confirma
#### Fluxo alternativo: Jogo não-físico -> solicitar tolerância.
    2.1. O Usuário que pegou o jogo emprestado (U2) abre o app
    2.2. U2 clica em notificações
    2.3. U2 clica na notificação de atraso
    2.4. U2 clica em solicitar tolerância
    2.5. U2 seleciona o tempo de tolerância (1 dia, 1 semana, 1 mês, 2 meses ou
mais) e confirma
    2.6. U1 recebe uma notificação sobre a solicitação de tolerância
    2.7. U1 clica em notificações
    2.8. A tela de notificações aparece
    2.9. U1 clica na notificação de tolerância
    2.10. U1 clica em adicionar tolerância
    2.11. S adiciona a tolerância de tempo ao tempo máximo de devolução do
jogo, nesse empréstimo
#### Fluxo alternativo: U2 não concede a tolerância
    2.10.1. U1 clica no botão em formato de ‘x’ (excluir solicitação)
    2.10.2. S não atribui uma tolerância