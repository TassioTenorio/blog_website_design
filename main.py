from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormLogin, FormCriarConta
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

lista_usuarios = ['Tassio', 'Nayara', 'Maria Eduarda', 'Thais']

app.config['SECRET_KEY'] = '85a46798861d1268220391d130135da0'
app.config['SQLALCHEMY_DATABASE_URI'] =  'sqlite:///comunidade.db'

database = SQLAlchemy(app)

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


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()

    if form_login.validate_on_submit() and 'botao_submit_login' in request.form:
        flash(f'Login feito com sucesso no email: {form_login.email.data}', 'alert-success')
        # redirecionar para a homepage
        return redirect(url_for('home'))

    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada para o e-mail: {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', login=login, form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(debug=True)

