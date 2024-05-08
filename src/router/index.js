import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import AddMovieFormView from "../views/AddMovieFormView.vue";
import MovieProfileView from "../views/MovieProfileView.vue";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
    },
    {
      path: "/movies/create",
      name: "AddMovieForm",
      component: () => import('../views/AddMovieFormView.vue')
    },
    {
      path: "/movieprofile",
      name: "MovieProfileView",
      component: () => import('../views/MovieProfileView.vue') 
    },
  ],
});

export default router
