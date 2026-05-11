    # importanto o render_templates
    # motor para renderizar as páginas
from flask import render_template, request, redirect, url_for

    # criando a função para receber o flask
def init_app(app):

    listGames = [{"titulo": "cs-go","ano": 2012, "categoria": "fps online"}]

    @app.route ('/')
        # o @ pe para criar funções no pytron

        #declarar variavel nome = o que ela recebe
        #o underline mostra que é uma variavel de ambiente

    def home():
            return render_template('index.html')

    @app.route ('/games')

    def games():
            titulo= "silksong"
            ano = 2025
            categoria = "metroid van"

            # criando um objeto python (dicionario) para representar as propriedades de um jogo
            game = {
                "titulo": "Minecraft",
                "ano": 2012,
                "categoria": "Sandbox"
            }

            jogadores = ['eduardo', 'vitor', 'ana']
            return render_template('games.html', 
                                titulo= titulo,
                                ano = ano,
                                categoria = categoria,
                                jogadores = jogadores)

    @app.route ('/consoles')

    def consoles():
            consoles = ['switch', 'ps1', 'ps2', 'ps3', 'ps4']
            return render_template('consoles.html',
                                consoles = consoles)    
    
    # rota de casdastro de jogos
    
    @app.route('/cadgames', method =['GET', 'POST'])
    def cadgames():
           
        #    verificando se o metodo da requisição é post
           if request.method == 'POST':
                  
                #   RECEBENDO OS DADOS DO FORMULARIO
                listGames.append({'titulo': request.form.get('titulo'), 'ano': request.form.get('ano'), 'categoria': request.form.get('categoria')})

                return redirect(url_for('cadgames'))
           return render_template('cadgames.html', listaGames=listGames)
    