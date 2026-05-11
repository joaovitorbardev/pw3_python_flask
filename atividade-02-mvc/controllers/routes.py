from flask import render_template, request, redirect, url_for

def init_app(app):

    @app.route ('/')
    # o @ pe para criar funções no pytron

    #declarar variavel nome = o que ela recebe
    #o underline mostra que é uma variavel de ambiente

    def home():
        return render_template('index.html')

    @app.route ('/dano')

    def games():
        return render_template('dano.html')

    @app.route ('/suportes')

    def suportes():
        return render_template('suportes.html')

    @app.route ('/tanques')

    def tanques():
        return render_template('tanques.html')

    @app.route ('/registro')

    def registro():
        return render_template('registro.html')
