<template>
     <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title class="text-center">Вход</v-card-title>
          <v-card-text>
            <v-form @submit="login">
              <v-text-field v-model="email" label="Email" type="email" required></v-text-field>
              <v-text-field v-model="password" label="Пароль" type="password" required></v-text-field>
              <v-btn type="submit" color="primary" block>Войти</v-btn>
            </v-form>
          </v-card-text>
          <div class="register-button">
            <button class="transparent-button" @click="register">Зарегистрироваться</button>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  data() {
    return {
      email: '',
      password: ''
    };
  },
  methods: {
    login() {
      // Здесь можно добавить логику для отправки данных на сервер и проверки входа
      this.$router.push('/user/main')

      
    },
    register() {
      // Здесь можно добавить логику для перехода на страницу регистрации
      this.$router.push('/register')
    }
  }
};
</script>

<style scoped>
.register-button {
  display: flex;
  justify-content: center;
}

.transparent-button {
  background-color: transparent;
  border: none;
  color: grey;;
  font-size: 16px;
  cursor: pointer;
}
</style>