<template>
    <v-container>
      <h1>Заявки на репетиторство</h1>
      <v-row>
        <v-col cols="12" sm="6" md="4" v-for="(request, index) in acceptedRequests" :key="index">
          <v-card>
            <v-card-title>{{ request.fullName }}</v-card-title>
            <v-card-text>
              <div>Цена: {{ request.price }}</div>
              <div>Часы на занятие: {{ request.hours }}</div>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        acceptedRequests: [
          { fullName: 'Иван Иванов', price: 500, hours: 1 },
          { fullName: 'Алексей Петров', price: 600, hours: 1.5 },
          { fullName: 'Елена Смирнова', price: 450, hours: 2 },
        ],
      };
    },
  };
  </script>