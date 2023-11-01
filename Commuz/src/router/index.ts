import { createRouter, createWebHistory } from 'vue-router'
import FrontPage from '../views/FrontPage.vue';
import Partenaires from '../views/Partenaires.vue';

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
    }
  ]
})

export default router
