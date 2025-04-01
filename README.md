📌 Busca de Operadoras

Este projeto é uma aplicação web para buscar operadoras de saúde registradas na ANS. Ele consiste em um backend em Flask para processar os dados e um frontend em Vue.js para exibir os resultados.

🚀 Tecnologias Utilizadas

Backend: Python (Flask, Pandas)

Banco de Dados: Arquivo CSV

Frontend: Vue.js

API Client: Postman (para testes)

📂 Estrutura do Projeto

📦 busca-operadoras
├── 📂 Backend
│   ├── app.py  # Servidor Flask
│   ├── data/Relatorio_cadop.csv  # Base de dados
│   ├── requirements.txt  # Dependências do Python
│   └── ...
│
├── 📂 Frontend
│   ├── src/
│   │   ├── components/
│   │   │   ├── BuscaComponent.vue  # Componente principal da busca
│   │   ├── App.vue  # Página principal
│   │   ├── main.js  # Configuração do Vue
│   ├── public/
│   ├── package.json  # Dependências do projeto
│   └── ...

🛠️ Configuração do Projeto

📌 1. Clonar o repositório

git clone https://github.com/SEU-USUARIO/busca-operadoras.git
cd busca-operadoras

⚙️ 2. Configurar o Backend (Flask)

cd Backend
python -m venv venv  # Criar ambiente virtual
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate  # Windows
pip install -r requirements.txt  # Instalar dependências
python app.py  # Iniciar servidor

O backend rodará em http://127.0.0.1:5000

🎨 3. Configurar o Frontend (Vue.js)

cd Frontend
npm install  # Instalar dependências
npm run serve  # Rodar servidor Vue

O frontend estará disponível em http://localhost:8080

🔍 Testando a API no Postman

Abrir o Postman

Criar uma nova requisição GET para:

http://127.0.0.1:5000/buscar?termo=saúde

Configurar os Headers:

Content-Type: application/json; charset=utf-8

Verificar o retorno dos dados JSON.
