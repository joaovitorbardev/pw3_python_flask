# importando o flask na aplicação 

from flask import Flask, render_template

from controllers import routes

#carregando o flask em um variável

app = Flask(__name__, template_folder='views')

routes.init_app(app)

#__name__ é uma variavel pytron que tem o nome da aplicação atual ou do módulo atual

#iniciando o servidor web

if __name__ == '__main__':
    app.run()

#run inicia o servidor
#verificando se o app.py for o arquivo principal, ele inicia o servidor
