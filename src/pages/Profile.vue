
<template>
    <v-container>
      <v-card>
        <v-img :src="profile.image" height="300"></v-img>
        <v-card-title>{{ profile.name }}</v-card-title>
        <v-card-subtitle>{{ profile.occupation }}</v-card-subtitle>
        <v-card-text>{{ profile.bio }}</v-card-text>
        <v-card-actions>
          <v-btn color="primary" @click="editProfile">Редактировать</v-btn>
        </v-card-actions>
      </v-card>
    </v-container>
  </template>
  
  <script>
  export default {
    data() {
      return {
        profile: {
          name: 'Иван Иванов',
          occupation: 'Разработчик',
          bio: 'Я занимаюсь разработкой веб-приложений уже более 5 лет. У меня опыт работы с различными технологиями, такими как Vue.js, React и Node.js.',
          image: 'profile.jpg'
        }
      };
    },
    methods: {
      editProfile() {
        // Логика для редактирования профиля
        console.log('Редактирование профиля');
      }
    }
  };
  </script>