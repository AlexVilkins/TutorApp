import Vue from 'vue'
import VueRouter from 'vue-router'


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