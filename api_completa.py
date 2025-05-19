
from flask import Flask, jsonify

app = Flask(__name__)

dados = {
    "celulares": {
        "ate_1000": [
            {
                "modelo": "Xiaomi Redmi Note 12",
                "caracteristicas": "Câmera tripla de 50MP, Tela AMOLED de 120Hz, 128GB",
                "preco": "R$979",
                "link": "https://www.google.com/search?q=Smartphone+Xiaomi+Redmi+Note+12+128GB"
            },
            {
                "modelo": "Samsung Galaxy A03",
                "caracteristicas": "Câmera dupla de 48MP, 64GB",
                "preco": "R$899",
                "link": "https://www.google.com/search?q=Smartphone+Samsung+Galaxy+A03+64GB"
            },
            {
                "modelo": "Motorola Moto E22",
                "caracteristicas": "Tela de 6.5\" HD+, 64GB",
                "preco": "R$999",
                "link": "https://www.google.com/search?q=Smartphone+Motorola+Moto+E22"
            }
        ],
        "ate_2000": [
            {"modelo": "Samsung Galaxy M14", "caracteristicas": "128GB, 5G", "preco": "R$1.499", "link": "https://www.google.com/search?q=Samsung+Galaxy+M14"},
            {"modelo": "Redmi Note 13", "caracteristicas": "6GB RAM, 128GB", "preco": "R$1.799", "link": "https://www.google.com/search?q=Redmi+Note+13"}
        ],
        "ate_3000": [
            {"modelo": "Galaxy A54", "caracteristicas": "8GB RAM, 256GB", "preco": "R$2.599", "link": "https://www.google.com/search?q=Galaxy+A54"}
        ],
        "acima_5000": [
            {"modelo": "iPhone 15", "caracteristicas": "128GB, Tela OLED", "preco": "R$7.299", "link": "https://www.google.com/search?q=iPhone+15"}
        ]
    },
    "notebooks": {
        "ate_1500": [
            {"modelo": "Multilaser Legacy", "caracteristicas": "Intel Celeron, 64GB", "preco": "R$1.499", "link": "https://www.google.com/search?q=Notebook+Multilaser+Legacy"}
        ],
        "ate_2500": [
            {"modelo": "Acer Aspire 3", "caracteristicas": "Intel Core i3, 256GB SSD", "preco": "R$2.399", "link": "https://www.google.com/search?q=Acer+Aspire+3"}
        ],
        "ate_3500": [
            {"modelo": "Samsung Book", "caracteristicas": "Core i5, 8GB RAM", "preco": "R$3.499", "link": "https://www.google.com/search?q=Samsung+Book+Core+i5"}
        ],
        "ate_4500": [
            {"modelo": "Lenovo IdeaPad 3i", "caracteristicas": "Core i7, 512GB SSD", "preco": "R$4.399", "link": "https://www.google.com/search?q=Lenovo+IdeaPad+3i"}
        ],
        "acima_5000": [
            {"modelo": "MacBook Air M2", "caracteristicas": "8GB RAM, 256GB SSD", "preco": "R$7.999", "link": "https://www.google.com/search?q=MacBook+Air+M2"}
        ]
    },
    "televisores": {
        "ate_1500": [
            {"modelo": "AOC 32\"", "caracteristicas": "HD, Smart TV", "preco": "R$1.299", "link": "https://www.google.com/search?q=TV+AOC+32+polegadas"}
        ],
        "ate_2500": [
            {"modelo": "Samsung 43\"", "caracteristicas": "4K UHD, Tizen", "preco": "R$2.299", "link": "https://www.google.com/search?q=Samsung+43+4K"}
        ],
        "ate_3500": [
            {"modelo": "LG 50\"", "caracteristicas": "4K UHD, WebOS", "preco": "R$3.299", "link": "https://www.google.com/search?q=LG+50+4K"}
        ],
        "ate_4500": [
            {"modelo": "TCL 55\"", "caracteristicas": "QLED, Google TV", "preco": "R$4.399", "link": "https://www.google.com/search?q=TCL+QLED+55"}
        ],
        "acima_4500": [
            {"modelo": "Samsung 65\" Neo QLED", "caracteristicas": "8K, Mini LED", "preco": "R$8.499", "link": "https://www.google.com/search?q=Samsung+Neo+QLED+65"}
        ]
    }
}

@app.route('/api/<categoria>/<faixa>', methods=['GET'])
def obter_ranking(categoria, faixa):
    if categoria in dados and faixa in dados[categoria]:
        return jsonify(dados[categoria][faixa])
    return jsonify({"erro": "Categoria ou faixa de preço não encontrada"}), 404

if __name__ == '__main__':
    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
