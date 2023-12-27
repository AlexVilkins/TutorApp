<template>
    <div>
      <v-toolbar color="primary" dark>
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>Меню</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-btn text>О нас</v-btn>
        <v-btn text>Контакты</v-btn>
        <v-btn text @click="$router.push('/login')">Выход</v-btn>
      </v-toolbar-items>
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
    </v-navigation-drawer>
    <router-view></router-view>
</div>
</template>

<script>
export default {
data() {
    return {
      drawer: false,
      items: [
        { title: 'Главная', icon: 'mdi-home', link: "main" },
        { title: 'Чат', icon: 'mdi-chat', link: "chat" },
        { title: 'События', icon: 'mdi-calendar', link: 'events'},
        { title: 'Каталог', icon: 'mdi-book' },
        { title: 'Профиль', icon: 'mdi-account', link: 'profile' },
      ],
    };
  },
  methods: {
    handleButtonClick (path) {
        console.log(String(path))
      this.$router.push('/user/' + String(path))
    }
  }
}
  </script>