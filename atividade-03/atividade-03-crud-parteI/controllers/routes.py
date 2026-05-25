
from flask import render_template, request, redirect, url_for
from models.database import Game, Console, db

def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        return render_template('games.html')

    @app.route('/consoles')
    def consoles():
        return render_template('consoles.html')

    @app.route('/estoque-jogos', methods=['GET', 'POST'])
    def estoque_jogos():

        if request.method == 'POST':
            dados = request.form.to_dict()

            novo_game = Game(
                dados['titulo'],
                dados['ano'],
                dados['categoria'],
                dados['plataforma'],
                dados['preco'],
                dados['quantidade']
            )

            db.session.add(novo_game)
            db.session.commit()

            return redirect(url_for('estoque_jogos'))

        games = Game.query.all()
        return render_template('estoque-jogos.html', games=games)

    @app.route('/editar-jogo/<int:id>', methods=['GET', 'POST'])
    def editar_jogo(id):

        game = Game.query.get(id)

        if request.method == 'POST':
            game.titulo = request.form['titulo']
            game.ano = request.form['ano']
            game.categoria = request.form['categoria']
            game.plataforma = request.form['plataforma']
            game.preco = request.form['preco']
            game.quantidade = request.form['quantidade']

            db.session.commit()

            return redirect(url_for('estoque_jogos'))

        return render_template('editar-jogo.html', game=game)

    @app.route('/excluir-jogo/<int:id>')
    def excluir_jogo(id):

        game = Game.query.get(id)

        db.session.delete(game)
        db.session.commit()

        return redirect(url_for('estoque_jogos'))

    @app.route('/estoque-consoles', methods=['GET', 'POST'])
    def estoque_consoles():

        if request.method == 'POST':
            dados = request.form.to_dict()

            novo_console = Console(
                dados['nome'],
                dados['fabricante'],
                dados['ano'],
                dados['preco'],
                dados['quantidade']
            )

            db.session.add(novo_console)
            db.session.commit()

            return redirect(url_for('estoque_consoles'))

        consoles = Console.query.all()
        return render_template('estoque-consoles.html', consoles=consoles)

    @app.route('/editar-console/<int:id>', methods=['GET', 'POST'])
    def editar_console(id):

        console = Console.query.get(id)

        if request.method == 'POST':
            console.nome = request.form['nome']
            console.fabricante = request.form['fabricante']
            console.ano = request.form['ano']
            console.preco = request.form['preco']
            console.quantidade = request.form['quantidade']

            db.session.commit()

            return redirect(url_for('estoque_consoles'))

        return render_template('editar-console.html', console=console)

    @app.route('/excluir-console/<int:id>')
    def excluir_console(id):

        console = Console.query.get(id)

        db.session.delete(console)
        db.session.commit()

        return redirect(url_for('estoque_consoles'))
