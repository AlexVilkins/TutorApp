<template>
    <v-container>
      <h1>Заявки на репетиторство</h1>
      <div>
    <v-text-field
      v-model="filterText"
      label="Найти предмет..."
      outlined
    ></v-text-field>
  </div>
      <v-row>
        <v-col cols="12" sm="6" md="4" v-for="(request, index) in filteredItems" :key="index">
          <v-card>
            <v-card-title>{{ request.fullName }}</v-card-title>
            <v-card-text>
              <div>Предмер: {{ request.object }}</div>
              <div>Цена: {{ request.price }}</div>
              <div>Часы на занятие: {{ request.hours }}</div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        applications: [
          { fullName: 'Иван Иванов', price: 500, object: 'Математика', hours: 1 },
          { fullName: 'Алексей Петров', price: 600, object: 'Русский', hours: 1.5 },
          { fullName: 'Елена Смирнова', price: 450, object: 'Английский', hours: 2 },
        ],
        filterText: '',
      };
    },
    computed: {
      filteredItems() {
        return this.applications.filter(item => item.object.toLowerCase().includes(this.filterText.toLowerCase()));
      }
    },
    mounted() {
      this.get_applications();
      
    },
    methods: {
      async get_applications(){
        await axios.get(
          'http://127.0.0.1:8000/get_application'
        )
        .then(response => (this.applications = response.data));

      }
    }
  };
  </script>