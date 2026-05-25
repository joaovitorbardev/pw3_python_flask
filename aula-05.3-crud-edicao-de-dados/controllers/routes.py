# Importando o render_template
# Motor para renderizar as páginas
from flask import render_template, request, redirect, url_for

#importando um Model Game e o SQLAlchemy
from models.database import Game, db

# Criando a função para receber o Flask (app)


def init_app(app):
    # SIMULANDO UM BANCO DE DADOS
    listaGames = [{"titulo": "CS-GO", "ano": 2012, "categoria": "FPS Online"}]

    # A partir daqui virão as rotas

    # CRIANDO A ROTA PRINCIPAL DO SITE
    @app.route('/')
    # def serve para criar funções no Python
    def home():
        return render_template('index.html')

    # CRIANDO A ROTA DE GAMES
    @app.route('/games')
    def games():
        # Criando variáveis para passar as informações de um jogo
        titulo = "Silk Song"
        ano = 2025
        categoria = "Metroid Van"

        # Criando um objeto Python (dicionário) para representar as propriedades de um jogo
        game = {
            "Título": "Minecraft",
            "Ano": 2012,
            "Categoria": "Sandbox"
        }
        # Criando vetor (lista)
        jogadores = ['Eduardo', 'Ana', 'Guilherme', 'Vitor', 'Antônio']
        return render_template('games.html',
                               # Enviando as variáveis para página HTML
                               titulo=titulo,
                               ano=ano,
                               categoria=categoria,
                               jogadores=jogadores,
                               game=game)

    # CRIANDO A ROTA DE CONSOLES
    @app.route('/consoles')
    def consoles():
        # Criando vetor (lista)
        consoles = ['Xbox', 'Playstation 5',
                    'Super Nintendo', 'Gameboy', 'Atari']
        return render_template('consoles.html',
                               consoles=consoles)

    # ROTA DE CADASTRO DE JOGOS
    @app.route('/cadgames', methods=['GET', 'POST'])  
    def cadgames():
        # Verificando se o método da requisição é POST
        if request.method == 'POST':
            # Recebendo os dados do formulário e gravando na lista
            listaGames.append({'titulo' : request.form.get('titulo'), 'ano' : request.form.get('ano'), 'categoria' : request.form.get('categoria')})
            # o método append() adiciona valores a lista
            return redirect(url_for('cadgames'))    
        return render_template('cadgames.html',
                               listaGames = listaGames)
        
        #rota de estoque de jogos
    @app.route("/estoque-jogos", methods=['GET', 'POST'])
            # criando um parametro na rota (id) para excluir um registro 
    @app.route("/estoque-jogos/delete/<int:id>")
    def estoque_jogos(id=None):
        if id:
            game = Game.query.get(id)
            db.session.delete(game)
            db.session.commit()
            return redirect(url_for('estoque_jogos'))
        # Cadastrando um jogo
        if request.method == "POST":
            dados = request.form.to_dict()
            newGame = Game(
                titulo = dados['titulo'],
                ano = dados['ano'],
                categoria = dados['categoria'],
                plataforma = dados['plataforma'],
                preco = dados['preco'],
                quantidade = dados['quantidade'],
            )
            db.session.add(newGame)
            db.session.commit()
            return redirect(url_for('estoque_jogos'))
        games = Game.query.all()
        return render_template('estoque-jogos.html', games=games)
    
    @app.route('/editar-jogos/<int:id>', methods=['GET'])
    def editar_jogos(id):
        # buscando o jogo no banco pelo id
        game = Game.query.get(id)
        # verificando se a requisição é post
        if request.method = 'POST':
            dados_form = request.form.to_dict()
            game.titulo = dados_form['titulo']
            game.ano = dados_form['ano']
            game.categoria = dados_form['categoria']
            game.plataforma = dados_form['plataforma']
            game.preco = dados_form['preco']
            game.quantidade = dados_form['quantidade']
            #  confirmando as alterações no vanco
            db.session.commit()
            return redirect(url_for('estoque'))
        return render_template('editar-jogos.html', game=game) 
    
