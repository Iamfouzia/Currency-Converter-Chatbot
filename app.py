from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        data = request.get_json()
        source_currency = data['queryResult']['parameters']['unit-currency']['currency']
        amount = data['queryResult']['parameters']['unit-currency']['amount']
        target_currency = data['queryResult']['parameters']['currency-name']

        print(source_currency)
        print(amount)
        print(target_currency)

        url = f"https://api.exchangerate-api.com/v4/latest/{source_currency}"
        response = requests.get(url)
        exchange_data = response.json()
        rate = exchange_data['rates'][target_currency]
        result = amount * rate

        reply = f"{amount} {source_currency} = {result:.2f} {target_currency}"
        return jsonify({"fulfillmentText": reply})
    return "<h1>Hello</h1>"

if __name__ == "__main__":
    app.run(debug=True)