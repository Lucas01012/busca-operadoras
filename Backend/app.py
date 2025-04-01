from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd

app = Flask(__name__)

CORS(app, resources={r"/*": {"origins": "*"}})

try:
    df = pd.read_csv('data/Relatorio_cadop.csv', encoding='utf-8', sep=';')
except FileNotFoundError:
    df = pd.DataFrame()

@app.route('/buscar', methods=['GET'])
def buscar():
    termo = request.args.get('termo', '').strip().lower()
    
    if not termo:
        return jsonify({'erro': 'Parâmetro "termo" não fornecido.'}), 400
    
    if df.empty:
        return jsonify({'erro': 'Arquivo de dados não encontrado ou vazio.'}), 500

    resultados = df[df.apply(lambda row: termo in ' '.join(map(str, row.fillna('').values)).lower(), axis=1)]
    
    if resultados.empty:
        return jsonify([])

    resultados = resultados.where(pd.notnull(resultados), None)
    
    return jsonify(resultados.fillna("").to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
