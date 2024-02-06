from flask import Flask,redirect,render_template,request

app = Flask(__name__)

app.secret_key = 'joao07'


@app.route('/')
def home():
    return render_template('index.html')







if __name__ == '__main__':
    app.run(debug=True)
