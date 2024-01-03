<template>
    <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title class="text-center">Регистрация</v-card-title>
          <v-card-text>
            <v-form @submit="register">
              <v-text-field v-model="name" label="Имя" required></v-text-field>
              <v-text-field v-model="email" label="Email" type="email" required></v-text-field>
              <v-text-field v-model="password" label="Пароль" type="password" required></v-text-field>
              <v-btn type="submit" color="primary" block>Зарегистрироваться</v-btn>
            </v-form>
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
      name: '',
      email: '',
      password: ''
    };
  },
  methods: {
    register() {
      // Здесь можно добавить логику для отправки данных на сервер и выполнения регистрации
      console.log('Имя:', this.name);
      console.log('Email:', this.email);
      console.log('Пароль:', this.password);

      // После успешной регистрации можно перенаправить пользователя на другую страницу
      this.$router.push('/');
    }
  }
};
</script>

<style scoped>


</style>