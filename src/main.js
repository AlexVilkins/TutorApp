import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import axios from 'axios'
import vuetify from './plugins/vuetify'
import vueResource from 'vue-resource'

Vue.use(vueResource)

Vue.config.productionTip = false
Vue.prototype.axios = axios


new Vue({
  router,
  store,
  axios,
  vuetify,
  render: h => h(App)
}).$mount('#app')
