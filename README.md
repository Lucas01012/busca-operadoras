API de Busca de Operadoras de Saúde ⚕️Este projeto consiste numa API backend construída com Flask que permite buscar informações sobre operadoras de saúde a partir de um ficheiro CSV, e um frontend simples em Vue.js para interagir com a API. O sistema permite ao utilizador buscar operadoras por diferentes termos, como nome, CNPJ, cidade e modalidade.FuncionalidadesBackend (API): Exposição de dados em formato JSON para permitir buscas por operadoras de saúde. 🔍Frontend (Vue.js): Interface de busca onde o utilizador pode digitar um termo e visualizar os resultados retornados pela API. 🖥️Tecnologias UtilizadasBackend: Flask (Python) 🐍Frontend: Vue.js ⚛️Base de Dados: Ficheiro CSV (relatório de operadoras) 🗄️Como Executar o ProjetoPasso 1: Configuração do BackendInstalar dependências:Certifique-se de ter o Python 3 e o pip instalados.Criar um ambiente virtual (opcional, mas recomendado):python -m venv venv
source venv/bin/activate  # No Windows use `venv\Scripts\activate`
Instalar pacotes necessários:pip install flask pandas flask-cors
Executar o servidor Flask:Certifique-se de que o ficheiro Relatorio_cadop.csv esteja na pasta data/.Execute o script do servidor Flask:python app.py
O servidor Flask irá rodar em http://127.0.0.1:5000/ por padrão. 🚀Passo 2: Configuração do Frontend (Vue.js)Instalar dependências do Vue:Certifique-se de ter o Node.js e o npm instalados.No diretório do frontend, execute:npm install
Executar o servidor Vue:Inicie o servidor de desenvolvimento:npm run serve
O frontend Vue estará disponível em http://localhost:8080/. ⚡Passo 3: Testando a AplicaçãoNo frontend, digite um termo de busca (exemplo: nome de uma operadora de saúde) e pressione Enter ou clique em "Buscar".O frontend fará uma requisição à API backend, que irá buscar as operadoras que correspondem ao termo informado no ficheiro CSV.Os resultados serão exibidos na tela. ✅Exemplos de Teste com o PostmanRequisição de Busca (GET)URL: http://127.0.0.1:5000/buscar?termo=operadoraMétodo: GET ➡️Exemplo de resposta:Imagem de Exemplo de Resposta  JSON 📦Como Funciona a BuscaO script Python usa o pandas para carregar o ficheiro CSV e procurar registos que correspondam ao termo de pesquisa fornecido. O frontend envia essa solicitação para o servidor, e os resultados são retornados como um JSON, que o Vue.js então exibe. 🔍Estrutura do ProjetoTESTE-API/
├── app.py                     # Script do backend Flask 🐍
├── data/                       # Diretório onde o CSV de operadoras é armazenado 🗂️
│   └── Relatorio_cadop.csv
├── frontend/                   # Código do frontend Vue.js ⚛️
│   ├── src/                   # Componentes Vue.js 🧩
│   └── public/                # Arquivos estáticos 📁
├── images/                     # Imagens usadas no README 🖼️
│   ├── postman_json.png
│   └── vue.png
└── README.md                  # Este ficheiro 📝
Funcionamento no FrontendA seguir está uma captura de tela que demonstra o funcionamento da interface do utilizador em Vue.js.Imagem de Vue Js 🖥️
