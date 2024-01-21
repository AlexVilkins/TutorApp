<template>
     <v-container>
    <v-row justify="center">
      <v-col cols="12" sm="8" md="4">
        <v-card>
          <v-card-title class="text-center">Войти</v-card-title>
          <v-card-text>
            <v-form @submit="login">
              <v-text-field v-model="username" label="Имя" required></v-text-field>
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
import axios from 'axios';
export default {
  data() {
    return {
      username: '',
      password: '',
    };
  },
  methods: {
    async login() {
      const data = new FormData()
      data.append('username', this.username);
      data.append('password', this.password)

      await axios.post(
        "http://127.0.0.1:8000/auth/jwt/login", data)
      
      .then(response => {
        console.log('cooke has been received!')
      localStorage.authToken = response.data.access_token
    })
      this.$router.push('/user/main')
    },

    register() {
      this.$router.push('/register')
    }
  },
  
  watch: {
    name(newName) {
      localStorage.authToken = newName;
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