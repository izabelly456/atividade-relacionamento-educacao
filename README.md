🎓 Sistema de Gestão: Professores & AulasEste projeto é um exemplo prático de como organizar um banco de dados usando Python e SQLAlchemy. Imagine que é um mini-diário escolar onde você liga cada aula ao seu respectivo professor.


💡 1. O que este projeto faz?
Ele gerencia a relação entre Professores e suas Aulas.
É um sistema de "Um para Muitos":1 Professor pode dar Várias Aulas
1 Aula pertence a apenas 1 Professor.


🛠️ 2. Tecnologias Usadas Python 3: A linguagem base.SQLAlchemy: O "tradutor" que permite falar com o banco de dados usando código Python.SQLite: O banco de dados (um arquivo .db que nasce sozinho na pasta).


🚀 3. Como configurar (Passo a Passo)

1º Passo: Instalar o tradutor (SQLAlchemy)Abra o seu terminale digite:pip install sqlalchemy


2º Passo: Preparar o arquivo, Garanta que o código Python está salvo (ex: app.py).

3º Passo: Executar No terminal, digite:Bashpython app.py
📂


 4. Entendendo as Funções (O que dá para fazer?)

 adicionar_professor: Cria um novo professor no sistema.
 
 adicionar_aula: Cria uma aula e pede o ID do professor (o "dono" dela)

 listar_aulas:Mostra todas as aulas e quem é o professor de cada uma.
 
 atualizar_professor: Muda o nome de um professor já cadastrado.
 
 deletar_aula: Apaga uma aula específica do banco.
 
 ⚠️ 5. Como usar na prática?

 Para o código funcionar de verdade, você precisa chamar as funções no final do arquivo. Por exemplo:Python# No final do seu arquivo, adicione isso para testar:

adicionar_professor() # Digite o nome do prof
adicionar_aula()      # Digite o título e o ID (geralmente 1)
listar_aulas()        # Veja a mágica acontecer!


🗃️ 6. Onde ficam guardados os dados?

Assim que você rodar o código pela primeira vez, surgirá um arquivo chamado educacao.db. Não delete esse arquivo, pois é ali que moram todos os nomes e aulas que você cadastrar!