import { createRouter, createWebHistory } from 'vue-router'
import FrontPage from '../views/FrontPage.vue';
import Partenaires from '../views/Partenaires.vue';
import MisterCommuz from '../views/MisterCommuz.vue';
import Equipe from '../views/Equipe.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      component: FrontPage
    }, 
    {
      path: '/partenaires',
      component: Partenaires
    },
    {
      path: '/equipe',
      component: Equipe
    },
    {
      path: '/mistercommuz',
      component: MisterCommuz
    }
  ]
})

export default router
