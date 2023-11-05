from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculadora_imc():
    resultado = None

    if request.method == 'POST':
        peso = float(request.form['peso'])
        altura = float(request.form['altura'])

        # Cálculo do IMC: IMC = peso / (altura * altura)
        imc = peso / (altura ** 2)

        classificacao = ''
        classe = ''

        if imc < 18.5:
            classificacao = 'Abaixo do Peso'
            classe = 'abaixo-peso'
        elif imc < 24.9:
            classificacao = 'Peso Ideal'
            classe = 'peso-ideal'
        elif imc < 29.9:
            classificacao = 'Sobrepeso'
            classe = 'sobrepeso'
        elif imc < 34.9:
            classificacao = 'Obesidade Grau 1'
            classe = 'obesidade-1'
        elif imc < 39.9:
            classificacao = 'Obesidade Grau 2'
            classe = 'obesidade-2'
        else:
            classificacao = 'Obesidade Grau 3'
            classe = 'obesidade-3'

        resultado = {
            'imc': f'{imc:.2f}',
            'classificacao': classificacao,
            'classe': classe
        }

    return render_template('calculadora_imc.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
