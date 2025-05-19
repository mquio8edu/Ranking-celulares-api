from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
import os

app = Flask(__name__)

@app.route('/')
def home():
    return 'API de ranking de celulares está no ar!'

@app.route('/ranking/celulares-ate-1000')
def ranking():
    url = "https://www.canaltech.com.br/smartphone/melhores-celulares-ate-1000-reais/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    headers = soup.find_all(['h2', 'h3'])
    celulares = []

    for h in headers:
        texto = h.get_text().lower()
        if any(p in texto for p in ['1º', '2º', '3º', 'primeiro', 'segundo', 'terceiro']):
            partes = h.get_text().split('–')
            if len(partes) < 2:
                partes = h.get_text().split('-')
            if len(partes) >= 2:
                modelo = partes[1].strip()
                celulares.append(modelo)

    return jsonify({
        "fonte": "Canaltech",
        "ranking": celulares[:3]
    })

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
