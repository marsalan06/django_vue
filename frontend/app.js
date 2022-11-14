// import order from 'order.js'
const routes = [
    {path: '/order',component:order},
]

const router = new VueRouter.createRouter({
    history: VueRouter.createWebHashHistory(),
    routes
})

const app = Vue.createApp({})
app.use(router)
app.mount('#app')