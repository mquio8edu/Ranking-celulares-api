from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from collections import defaultdict
import os

app = Flask(__name__)

def get_top_celulares_canaltech():
    url = "https://www.canaltech.com.br/smartphone/melhores-celulares-ate-1000-reais/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    # Procura os títulos dos rankings
    headers = soup.find_all(['h2', 'h3'])
    
    ranking = []
    for header in headers:
        text = header.get_text().strip()
        if any(pos in text.lower() for pos in ['1º', '2º', '3º', 'primeiro', 'segundo', 'terceiro']):
            ranking.append(text)

    # Extrair os modelos a partir dos títulos
    cleaned_ranking = []
    for item in ranking:
        if '–' in item:
            parts = item.split('–')
        elif '-' in item:
            parts = item.split('-')
        else:
            parts = [item]

        model = parts[1].strip() if len(parts) > 1 else parts[0].strip()
        cleaned_ranking.append(model)

    results = defaultdict(lambda: [0,0,0])
    for i, model in enumerate(cleaned_ranking[:3]):
        results[model][i] += 1

    data = []
    for model, positions in results.items():
        data.append({
            "modelo": model,
            "1º_lugar": positions[0] * 100,
            "2º_lugar": positions[1] * 100,
            "3º_lugar": positions[2] * 100
        })
    return data

@app.route('/ranking/celulares-ate-1000', methods=['GET'])
def ranking_celulares():
    data = get_top_celulares_canaltech()
    return jsonify({"fonte": "Canaltech", "ranking": data})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
