# Importa a classe Flask da biblioteca flask
# Sem essa linha, o Python não sabe o que é "Flask"
from flask import Flask, render_template

# Cria a instância da aplicação Flask
# __name__ é uma variável especial do Python que contém o nome do módulo atual
# O Flask usa isso para saber onde procurar os templates e arquivos estáticos
app = Flask(__name__)


# O decorador @app.route define qual URL aciona esta função
# '/' é a rota raiz — o endereço principal do site (ex: http://localhost:5000/)
@app.route('/')
def inicio():
    # Esta função retorna o que o navegador vai receber como resposta
    # Por enquanto, retornamos uma string HTML simples
    return render_template('index.html')

@app.route('/dream')
def realizar_dream():
    return '<h1>Sonho</h1>'

@app.route('/varias-linhas')
def varias_linhas():
    return '''
    <h1>Várias linhas</h1>
    <p>Este é um exmeplo de resposta com várias linhas de HTML.</p>
    <ul>
        <li>Item 1</li>
        <li>Item 2</li>
        <li>Item 3</li>
    <ul>
    '''

@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

@app.route('/sobre/fatec')
def sobre_fatec():
    # Rota /sobre: http://localhost:5000/sobre
    return '''
        <h1>Página sobre a Fatec</h1>
        <p>Desenvolvida na <b>Fatec</b></p>
    '''

@app.route('/cor/<cor1>')
def exibir_cor(cor1):
    return f'<h1 style="color:{cor1}"> A cor escolhida foi: {cor1}</h1>'

@app.route('/bootstrap')
def ver_algo():
    return render_template('bootstrap.html')

# Bloco de execução: só roda quando o arquivo é executado diretamente
if __name__ == '__main__':
    # debug=True ativa o recarregamento automático ao salvar o arquivo
    # NUNCA use debug=True em produção (servidor público)
    app.run(debug=True)