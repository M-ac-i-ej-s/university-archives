import { createRouter, createWebHistory } from 'vue-router'
import WelcomePage from '../views/WelcomePage.vue'
import GamePage from '../views/GamePage.vue'

const routes = [
  {
    path: '/',
    name: 'WelcomePage',
    component: WelcomePage
  },
  {
    path: '/game',
    name: 'GamePage',
    component: GamePage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router