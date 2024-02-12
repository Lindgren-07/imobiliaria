from flask import Flask,redirect,render_template,request,flash
import json
import os.path
from sqlalchemy import Column,String,Integer,Date,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

try:
    engine = create_engine('postgresql://postgres:jlindgren@localhost:5432/imobiliaria')
except:
    print('error')
else:
    print('funcionou')

Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Cliente(Base):
    __tablename__ = 'cliente'
    id_cliente = Column(Integer,primary_key=True)
    nome_cliente = Column(String,nullable=False)
    senha_cliente = Column(String,nullable=False)
    email_cliente = Column(String,nullable=False)
    anoNasc_cliente = Column(Date, nullable=False)



app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:jlindgren@localhost:5432/imobiliaria'
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

@app.route('/adm')
def adm():
   usuarios = session.query(Cliente).all()
   return render_template('adm.html',usuarios=usuarios)


@app.route('/cadastrarUsuario',methods=['POST'])
def cadastrarUsuario():
    nome = request.form.get('nome')
    senha = request.form.get('senha')
    email = request.form.get('email')
    anoNasc = request.form.get('anoNasc')
    

    novo_cliente = Cliente(nome_cliente=nome,senha_cliente=senha,email_cliente=email,anoNasc_cliente=anoNasc)
    session.add(novo_cliente)
    session.commit()

    

    flash(f'{nome} cadastrado(a) com sucesso ! ')
    return render_template('cadastrar.html')


@app.route('/login', methods=['POST'])
def loginAdm():

    clientes = session.query(Cliente).all()

    email = request.form.get('email')
    senha = request.form.get('senha')

    if email == 'adm@adm' and senha == '000':
        return redirect('/adm')
    for cliente in clientes:
        if cliente.email_cliente == email and cliente.senha_cliente == senha:
            return redirect('/principal')  
    else:
        flash('nome ou senha inválido')
        return redirect('/')
    

        

   


@app.route('/excluirUsuario', methods=['POST'])
def excluirUsuario():
    id = request.form.get('idUsuario')
    nome = request.form.get('nome')
    session.query(Cliente).filter(Cliente.id_cliente==id).delete()
    session.commit()

    flash(f'Cliente {nome} excluido com sucesso')
    return redirect('/adm')




if __name__ == '__main__':
    Base.metadata.create_all(bind=engine)
    app.run(debug=True)
    
