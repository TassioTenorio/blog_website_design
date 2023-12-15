from flask import Flask, render_template, url_for

app = Flask(__name__)

lista_usuarios = ['Tassio', 'Nayara', 'Maria Eduarda', 'Thais']

# decorators
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/lista_usuarios')
def usuarios():
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login')
def login():
    return render_template('login.html', login=login)


if __name__ == '__main__':
    app.run(debug=True)

