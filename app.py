from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    amount = float(request.form['amount'])
    from_currency = request.form['from_currency']
    to_currency = request.form['to_currency']

    url = f'https://economia.awesomeapi.com.br/last/{from_currency}-{to_currency}'

    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        if f'{from_currency}{to_currency}' in data:
            exchange_rate = float(data[f'{from_currency}{to_currency}']['bid'])
            converted_amount = amount * exchange_rate
            result = f'{amount} {from_currency} = {converted_amount:.2f} {to_currency}'
        else:
            result = 'Moeda de destino inválida.'
    else:
        result = 'Erro ao obter taxas de câmbio.'

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
