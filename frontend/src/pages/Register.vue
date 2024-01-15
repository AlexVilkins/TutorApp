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
          <div class="register-button">
            <button class="transparent-button" @click="login">Войти</button>
          </div>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  data() {
    return {
      name: '',
      email: '',
      password: '',
      role: 1,
    };
  },
  methods: {
    async register() {
      const data = {
        "email": this.email,
        "password": this.password,
        "is_active": true,
        "is_superuser": false,
        "is_verified": false,
        "username": this.name,
        "role_id": 1
      }

      const response = await axios.post(
        "http://127.0.0.1:8000/auth/register", data
      )
      this.username = response.data.username

      this.$router.push('/user/main');
    },
    login() {
      this.$router.push('/user/login');
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