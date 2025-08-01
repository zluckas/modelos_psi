from flask import Flask, render_template, redirect, url_for, request, flash
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = 'secret_key123'

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
database = 'banco.db'

class User(UserMixin):
    def __init__(self, id, nome, senha):
        self.id = id
        self.nome = nome
        self.senha = senha

    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    return user_id

def conectar():
    conn = sqlite3.connect(database)
    return conn

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        hash_senha = generate_password_hash(senha)
        return redirect(url_for('login'))
    return render_template('cadastro.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        
        flash('Usuário ou senha inválidos.', category='error')
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout realizado com sucesso.')
    return redirect(url_for('login'))

'''@app.route('/protected')
@login_required
def protected():
    return f'Olá, {current_user.nome}!''' #area protejida (usar apenas se pedir)

if __name__ == '__main__':
    app.run(debug=True)