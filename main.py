from flask import Flask,redirect,render_template,request,flash
import json
import os.path

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

    
        
    if os.path.isfile('usuarios.json') and os.path.getsize('usuarios.json') > 0:
        with open('usuarios.json') as usuarioTemp:
            usuariospy = json.load(usuarioTemp)
    else:
        usuariospy = []
    
    usuariospy.append(usuarios)

    with open('usuarios.json', 'w') as gravarTemp:
        json.dump(usuariospy,gravarTemp,indent=4)

    

    flash(f'{nome} cadastrado(a) com sucesso ! ')
    return render_template('cadastrar.html')


@app.route('/login', methods=['POST'])
def loginAdm():

    nome = request.form.get('nome')
    senha = request.form.get('senha')

    if nome == 'adm' and senha == '000':
        return render_template('adm.html')
    else:
        flash('nome ou senha inválido')
        return redirect('/')





if __name__ == '__main__':
    app.run(debug=True)
