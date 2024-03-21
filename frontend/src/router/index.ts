import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      name: 'playground',
      path: '/playground',
      component: () => import("../views/Playground.vue")
    },
    {
      name: 'home',
      path: '/',
      component: () => import("../views/HomeView.vue")
    },{
      name: 'dashboard',
      path: '/dashboard',
      component: () => import("../views/DashboardView.vue")
    }
  ]
})

export default router
