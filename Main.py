from flask import Flask, jsonify
import requests
from bs4 import BeautifulSoup
from collections import defaultdict

app = Flask(__name__)

def get_top_celulares_canaltech():
    url = "https://www.canaltech.com.br/smartphone/melhores-celulares-ate-1000-reais/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    headers = soup.find_all(["h2", "h3"])

    ranking = []
    for header in headers:
        text = header.get_text().strip()
        if any(k in text.lower() for k in ["1º", "2º", "3º", "primeiro", "segundo", "terceiro"]):
            ranking.append(text)

    cleaned_ranking = []
    for item in ranking:
        parts = item.split("–")
        if len(parts) < 2:
            parts = item.split("-")
        model = parts[1].strip() if len(parts) > 1 else parts[0].strip()
        cleaned_ranking.append(model)

    results = defaultdict(lambda: [0, 0, 0])
    for i, model in enumerate(cleaned_ranking[:3]):
        results[model][i] += 1

    data = []
    for model, positions in results.items():
        data.append({
            "modelo": model,
            "1º_lugar": positions[0] * 100,
            "2º_lugar": positions[1] * 100,
            "3º_lugar": positions[2] * 100,
        })
    return data

@app.route("/ranking/celulares-ate-1000", methods=["GET"])
def ranking_celulares():
    data = get_top_celulares_canaltech()
    return jsonify({"fonte": "Canaltech", "ranking": data})

app.run(host="0.0.0.0", port=3000)
