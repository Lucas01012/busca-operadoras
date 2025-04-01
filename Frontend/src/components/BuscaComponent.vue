<template>
    <div class="search-container">
      <input
        v-model="query"
        type="text"
        class="search-input"
        placeholder="Digite o termo de busca (ex.: Nome de uma Operadora)"
        @keyup.enter="buscarOperadoras"
      />
      <button class="search-button" @click="buscarOperadoras">Buscar</button>
      
      <div v-if="loading">Buscando...</div>
      <ul v-else>
        <li v-for="(item, index) in operadoras" :key="index">
          <strong>{{ item.Razao_Social }}</strong>
          <br>
          CNPJ: {{ item.CNPJ }} <br>
          Cidade: {{ item.Cidade }} - UF: {{ item.UF }} <br>
          Modalidade: {{ item.Modalidade }} <br>
          Data Registro: {{ item.Data_Registro_ANS }}
        </li>
      </ul>
      <p v-if="!loading && operadoras.length === 0">Nenhuma operadora encontrada.</p>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        query: '',
        operadoras: [],
        loading: false,
      };
    },
    methods: {
        async buscarOperadoras() {
  if (!this.query.trim()) {
    alert('Por favor, insira um termo de busca.');
    return;
  }
  this.loading = true;
  try {
    const response = await fetch(`http://127.0.0.1:5000/buscar?termo=${encodeURIComponent(this.query)}`, {
      headers: {
        'Content-Type': 'application/json; charset=utf-8'
      }
    });

    if (!response.ok) {
      throw new Error(`Erro na requisição: ${response.statusText}`);
    }
    
    const data = await response.json();
    console.log('Resposta recebida:', data);

    this.operadoras = data;
  } catch (error) {
    console.error('Erro ao buscar operadoras:', error);
  } finally {
    this.loading = false;
  }
}

    },
  };
  </script>
  
  <style scoped>
  .search-container {
    margin-top: 20px;
    padding: 10px;
  }
  
  .search-input {
    width: 100%;
    padding: 10px;
    margin: 5px 0;
  }
  
  .search-button {
    padding: 10px 20px;
    margin-top: 10px;
  }
  
  .result-item {
    margin-bottom: 10px;
  }
  </style>  