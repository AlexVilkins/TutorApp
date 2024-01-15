<template>
    <div>
      <v-toolbar color="primary" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Меню</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-title>{{ username }}</v-toolbar-title>
      <v-icon>mdi-account-circle</v-icon>
    </v-toolbar>

    <v-navigation-drawer v-model="drawer" app>
      <v-list>
        <v-list-item 
            v-for="(item, index) in items" 
            :key="index" link
            @click="handleButtonClick(item.link)"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
      <v-btn @click="$router.push('/login')">Выход</v-btn>
    </v-navigation-drawer>
    <router-view></router-view>
</div>
</template>

<script>

export default {
  data() {
    return {
      drawer: false,
      username: 'user',
      items: [
        { title: 'Главная', icon: 'mdi-home', link: "main" },
        { title: 'Чат', icon: 'mdi-chat', link: "chat" },
        { title: 'События', icon: 'mdi-calendar', link: 'events'},
        { title: 'Расписание', icon: 'mdi-book' },
        { title: 'Профиль', icon: 'mdi-account', link: 'profile' },
      ],
    };
  },
  methods: {
    handleButtonClick (path) {
      console.log(String(path))
      this.$router.push('/user/' + String(path))
    }
  },

  // mounted: {
  //   async getUserName() {
  //     const response = await axios.get(
  //       "http://127.0.0.1:8000/auth/register"
  //     )
  //     this.username = response.data.name
  //     .catch(function (error) {
  //       console.log(error);
  //     })
  //   }
  // }
}
</script>