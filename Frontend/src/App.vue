<template>
  <div id="app">
    <h1>Busca de Operadoras</h1>
    <BuscaComponent/>
  </div>
</template>

<script>
import BuscaComponent from './components/BuscaComponent.vue';

export default {
  name: 'App',
  components: {
    BuscaComponent,
  },
};
</script>

<style>
@import './assets/styles.css';
</style>