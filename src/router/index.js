import Vue from 'vue'
import VueRouter from 'vue-router'


Vue.use(VueRouter)

const routes = [
    {
        path: '/',
        component: () =>
            import ('@/pages/Main.vue'),    
    },
    {
        path: '/login',
        component: () =>
            import ('@/pages/Login.vue'),    
    },
    {
        path: '/register',
        component: () =>
            import ('@/pages/Register.vue'),    
    }
]

const router = new VueRouter({
    routes
})

export default router