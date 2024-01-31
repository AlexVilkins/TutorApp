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
        <div class="filter">
          <v-select
            chips
            v-model="searchObject" 
            :items="['Математика', 'Русский язык', 'Литература', 'Georgia', 'Texas', 'Wyoming']" 
            label="Предмет"
          ></v-select>
          <v-select
            chips
            v-model="searchPrice"
            label="Цена"
            :items="[500, 1000]"
            variant="outlined"
          ></v-select>
          <v-select
            chips
            v-model="searchHour"
            label="Часы"
            :items="[1, 1.5]"
            variant="outlined"
          ></v-select>
        <v-btn 
          @click="changePage()"
          color="primary">Применить
        </v-btn>
        </div>
        <v-div>
          <v-row>
        <v-col cols="12" sm="6" md="6" v-for="item in applications" :key="item.id">
          <v-card>
            <v-card-title>{{ item.username }}</v-card-title>
            <v-card-text>
              <div>Предмер: {{ item.object }}</div>
              <div>Цена: {{ item.price }}</div>
              <div>Часы на занятие: {{ item.hour }}</div>
              <div>Опубликовано: {{ item.datetime }}</div>
            </v-card-text>
          </v-card>
        </v-col>
        </v-row>
        <v-pagination
          v-model="currentPage"
          :length="totalPages"
          @input="changePage"
          color="primary"
        ></v-pagination>
      </v-div>
    </v-container>
  </template>
  
  <script>
  import axios from 'axios';

  export default {
    data() {
      return {
        applications: [],
        filterText: '',
        searchObject: '',
        searchPrice: '',
        searchHour: '',
        currentPage: 1,
        itemsPerPage: 10,
        totalItems: 0,
      };
    },
    computed: {
      paginatedData() {
        const startIndex = (this.currentPage - 1) * this.itemsPerPage;
        const endIndex = startIndex + this.itemsPerPage;
        // changePage();
        return this.applications.slice(startIndex, endIndex);
      },
      totalPages() {
        return Math.ceil(this.totalItems / this.itemsPerPage);
      },
      
    },
    methods: {
      async get_applications(){
        await axios.get(
          'http://127.0.0.1:8000/operations/application'
        )
        .then(response => (this.applications = response.data));
      },
      async filteredItems(){
        const data = { 'searchObject': this.searchObject};

        await axios.post(
          "http://127.0.0.1:8000/operations/filter_data", data
        )
        .then(response => (this.applications = response.data))
      },
      async changePage() {
        let query = `http://127.0.0.1:8000/operations/application?page=${this.currentPage}`;

        if (this.searchObject) query += `&object=${this.searchObject}`;
        if (this.searchPrice) query += `&price=${this.searchPrice}`;
        if (this.searchHour) query += `&hour=${this.searchHour}`;

        console.log(query)

        const response = await axios.get(
          query
        );
          this.applications = response.data.items,
          this.totalItems = response.data.totalItems
      },
    },
    created() {    
      this.changePage();
    },
  };
  </script>

<style>
.filter {
  display: flex;
  justify-content: space-around;
}
</style>