from flask import Flask,redirect,render_template,request
import json

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://DESKTOP-3NB93KR/cadastro?driver=ODBC+Driver+17+for+SQL+Server'
app.secret_key = 'joao07'


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cadastrar')
def cadastrar():
    return render_template('cadastrar.html')


@app.route('/index')
def login():
    return redirect('/')

@app.route('/principal')
def principal():
    return render_template('principal.html')


@app.route('/cadastrarUsuario',methods=['POST'])
def cadastrarUsuario():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    email = request.form.get('email')
    anoNasc = request.form.get('anoNasc')
    sexo = request.form.get('genero')

    usuarios = dict()
    usuarios['nome'] = nome
    usuarios['senha'] = senha
    usuarios['email'] = email
    usuarios['anoNasc'] = anoNasc

    print(nome,senha,email,anoNasc,sexo)

    with open('usuarios.json', 'a') as usuariosTemp:
        json.dump(usuarios,usuariosTemp,indent=10)
        usuariosTemp.write(' ') 
        usuariosTemp.write('\n') 
    return redirect('/')





if __name__ == '__main__':
    app.run(debug=True)
