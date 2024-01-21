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
      <!-- <div class="filter"> -->
        <div class="filter">
          <v-col md="4">
          <v-select
            multiple
            chips
            v-model="searchObject" 
            :items="['Математика', 'Русский язык', 'Литература', 'Georgia', 'Texas', 'Wyoming']" 
            label="Предмет"
          ></v-select>
          </v-col>
          <v-col md="4">
          <v-select
            multiple
            chips
            v-model="searcPrice"
            label="Цена"
            :items="['500', '1000', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
            variant="outlined"
          ></v-select>
        </v-col>
        <v-col md="4">
          <v-select
            multiple
            chips
            v-model="serachHour"
            label="Часы"
            :items="['California', 'Colorado', 'Florida', 'Georgia', 'Texas', 'Wyoming']"
            variant="outlined"
          ></v-select>
        </v-col>
        </div>
      <v-row>
        <v-col cols="12" sm="6" md="4" v-for="(request, index) in filteredItems" :key="index">
          <v-card>
            <v-card-title>{{ request.username }}</v-card-title>
            <v-card-text>
              <div>Предмер: {{ request.object }}</div>
              <div>Цена: {{ request.price }}</div>
              <div>Часы на занятие: {{ request.hour }}</div>
              <div>Опубликовано: {{ request.datetime }}</div>
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
        applications: [],
        filterText: '',
        searchObject: [],
        searchPrice: [],
        searchHour: [],
      };
    },
    computed: {
      filteredItems() {
        return this.applications.filter(item => {
          if (!this.searchObject.length == 0 && !this.searchObject.includes(item.object)){
            return false;
          }
          if (!this.searchPrice.length == 0 && !this.searchPrice.includes(item.price)) {
            return false;
          }
        if (this.selectedS && item.size !== this.selectedSize) {
          return false;
        }
          return true;
      })
        // return this.applications.filter(item => item.object.toLowerCase().includes(this.filterText.toLowerCase()));
      }
    },
    async mounted() {
      await this.get_applications();
      
    },
    methods: {
      async get_applications(){
        await axios.get(
          'http://127.0.0.1:8000/operations/application'
        )
        .then(response => (this.applications = response.data));

      }
    }
  };
  </script>

<style>
.filter {
  display: flex;
  justify-content: space-between;
  /* margin: 10px; */
}
</style>