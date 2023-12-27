<template>
    <v-container>
      <h1 class="text-center">События</h1>
      <v-row>
        <v-col cols="12" md="4" v-for="event in events" :key="event.id">
          <v-card>
            <v-img :src="event.image" height="200px"></v-img>
            <v-card-title>{{ event.title }}</v-card-title>
            <v-card-text>{{ event.description }}</v-card-text>
            <v-card-actions>
              <v-btn color="primary" text>Подробнее</v-btn>
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        events: [
          {
            id: 1,
            title: 'Конференция',
            description: 'Присоединяйтесь к нашей конференции!',
            image: 'conference.jpg'
          },
          {
            id: 2,
            title: 'Вебинар',
            description: 'Узнайте все о новейших технологиях веб-разработки.',
            image: 'webinar.jpg'
          },
          {
            id: 3,
            title: 'Выставка',
            description: 'Посетите нашу выставку и откройте для себя новые возможности.',
            image: 'exhibition.jpg'
          }
        ]
      };
    }
  };
  </script>
  
  <style>
    .text-center {
      text-align: center;
    }
  </style>