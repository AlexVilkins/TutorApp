import Vue from 'vue'
import VueRouter from 'vue-router'
// import Login from '@/components/Login.vue'
// import { nextTick } from 'vue/types/umd'


Vue.use(VueRouter)

const routes = [
    {
        path: '/user',
        component: () => 
            import ('@/pages/Main.vue'),
        children: [
            {
                path: 'main',
                name: 'main',
                component: () => 
                    import ('@/pages/user/UserMain.vue'),
            },
            {
                path: 'events',
                component: () =>
                    import ('@/pages/Events.vue'),    
            },
            {
                path: 'profile',
                component: () =>
                    import ('@/pages/Profile.vue'),    
            },
            {
                path: 'chat',
                name: 'chat',
                component: () =>
                    import ('@/pages/Chat.vue'),    
            }
        ] 
    },
    {
        path: '/login',
        name: "Login",
        component: () =>
            import ('@/pages/Login.vue'),    
    },
    {
        path: '/register',
        name: 'Register',
        component: () =>
            import ('@/pages/Register.vue'),    
    }
]

const router = new VueRouter({
    
    routes
})

router.beforeEach((to, from, next) => {
    if (to.name !== 'Login' && to.name !== 'Register' && !localStorage.getItem('authToken')) {
        next({ name: 'Login' })
    } else next()
})

export default router