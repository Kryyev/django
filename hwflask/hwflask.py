from flask import Flask
import requests

app = Flask(__name__)

response = requests.get('https://bitpay.com/api/rates')
data = response.json()

# print(data[0]['code'])


@app.route('/rates/currency=usd')
def rates():
    result = ''
    for item in data:
        result = result + f"<li>{item['name']} {item['code']} {item['rate']}</li>"
    return f'<ul>{result}</ul>'


rates()


if __name__ == '__main__':
    app.run(debug=True, port=5010)


# response = requests.get('https://bitpay.com/api/rates', params=payload)
#         data = response.json()

