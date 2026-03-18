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

@app.route ('/games')

def games():
    titulo= "silksong"
    ano = 2025
    categoria = "metroid van"
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

#__name__ é uma variavel pytron que tem o nome da aplicação atual ou do módulo atual

#iniciando o servidor web

if __name__ == '__main__':
    app.run()

#run inicia o servidor
#verificando se o app.py for o arquivo principal, ele inicia o servidor
