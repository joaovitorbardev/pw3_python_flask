# importando o flask na aplicação 

from flask import Flask, render_template

#carregando o flask em um variável

app = Flask(__name__, template_folder='views')

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

#__name__ é uma variavel pytron que tem o nome da aplicação atual ou do módulo atual

#iniciando o servidor web

if __name__ == '__main__':
    app.run()

#run inicia o servidor
#verificando se o app.py for o arquivo principal, ele inicia o servidor
