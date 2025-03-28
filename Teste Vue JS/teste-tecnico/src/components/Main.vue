<template>
    <div class="wrapper">
      <div class="container">
        <h1>🔍 Buscar Operadoras</h1>
        <div class="search-box">
          <input 
            type="text" 
            v-model="query" 
            @input="buscarOperadoras" 
            placeholder="Digite o Registro ANS." 
          />
          <button @click="resetarPesquisa">🔄</button>
        </div>
  
        <div class="table-container" v-if="operadoras.length">
          <table>
            <thead>
              <tr>
                <th>CNPJ</th>
                <th>Razão Social</th>
                <th>Nome Fantasia</th>
                <th>Modalidade</th>
                <th>Representante</th>
                <th>Número</th>
                <th>Complemento</th>
                <th>Bairro</th>
                <th>Cidade</th>
                <th>UF</th>
                <th>CEP</th>
                <th>Telefone</th>
                <th>Email</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="operadora in operadoras" :key="operadora.CNPJ">
                <td>{{ operadora.CNPJ }}</td>
                <td>{{ operadora.Razao_Social }}</td>
                <td>{{ operadora.Nome_Fantasia }}</td>
                <td>{{ operadora.Modalidade }}</td>
                <td>{{ operadora.Representante }}</td>
                <td>{{ operadora.Numero }}</td>
                <td>{{ operadora.Complemento }}</td>
                <td>{{ operadora.Bairro }}</td>
                <td>{{ operadora.Cidade }}</td>
                <td>{{ operadora.UF }}</td>
                <td>{{ operadora.CEP }}</td>
                <td>{{ operadora.Telefone }}</td>
                <td>{{ operadora.Endereco_eletronico }}</td>
              </tr>
            </tbody>
          </table>
        </div>
  
        <p v-else>Nenhuma operadora encontrada.</p>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return {
        query: '',
        operadoras: []
      };
    },
    methods: {
      async buscarOperadoras() {
        if (this.query.trim() === '') {
          this.operadoras = [];
          return;
        }
        try {
          const response = await axios.get(`http://127.0.0.1:8000/buscar?q=${this.query}`);
          this.operadoras = response.data;
        } catch (error) {
          console.error('Erro ao buscar operadoras:', error);
        }
      },
      resetarPesquisa() {
        this.query = '';
        this.operadoras = [];
      }
    }
  };
  </script>
  
  <style>
  /* Reset básico */
  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }
  
  body {
    font-family: 'Arial', sans-serif;
    background: linear-gradient(135deg, #6a11cb, #2575fc);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
    color: white;
    justify-content: center;
    align-items: center;
    margin-right: 400px;
  }
  
  /* Wrapper para centralizar tudo */
  .wrapper {
    display: flex;
    justify-content: center;
    align-items: center;
    width: 100%;
    padding: 20px;
  }
  
  /* Container principal */
  .container {
    width: 90%;
    max-width: 1200px;
    background: rgba(255, 255, 255, 0.95);
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
    text-align: center;
    color: #333;
  }
  
  /* Título */
  h1 {
    font-size: 28px;
    margin-bottom: 20px;
    color: #6a11cb;
  }
  
  /* Input + botão */
  .search-box {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 10px;
    margin-bottom: 20px;
  }
  
  input {
    padding: 12px;
    width: 100%;
    max-width: 400px;
    border: 2px solid #6a11cb;
    border-radius: 8px;
    outline: none;
    font-size: 16px;
    text-align: center;
    background: #fff;
    color: #333;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
  }
  
  button {
    padding: 12px 15px;
    border: none;
    border-radius: 8px;
    background: #2575fc;
    color: white;
    font-size: 16px;
    cursor: pointer;
    transition: 0.3s;
  }
  
  button:hover {
    background: #1a5cd8;
  }
  
  /* Responsividade da tabela */
  .table-container {
    max-width: 100%;
    overflow-x: auto;
  }
  
  /* Tabela */
  table {
    width: 100%;
    border-collapse: collapse;
    background: white;
    color: black;
    border-radius: 5px;
    overflow: hidden;
    min-width: 1000px;
  }
  
  /* Cabeçalho */
  th {
    background: #6a11cb;
    color: white;
    padding: 12px;
    text-align: center;
  }
  
  /* Linhas */
  td {
    padding: 10px;
    border-bottom: 1px solid #ddd;
    text-align: center;
  }
  
  /* Linhas alternadas */
  tr:nth-child(even) {
    background: #f8f9fa;
  }
  
  /* Mensagem sem resultados */
  p {
    font-size: 18px;
    margin-top: 20px;
    color: #6a11cb;
  }
  
  /* Responsividade */
  @media (max-width: 768px) {
    th, td {
      font-size: 14px;
      padding: 8px;
    }
  
    table {
      min-width: 700px;
    }
  
    .search-box {
      flex-direction: column;
    }
  
    input {
      width: 100%;
    }
  
    button {
      width: auto;
      padding: 10px 15px;
    }
  }
  </style>
  