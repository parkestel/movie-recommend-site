import { createRouter, createWebHistory } from 'vue-router'
import MovieListView from '@/views/MovieListView.vue'
import MovieDetail from '@/views/MovieDetail.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'
import VocaNote from '@/views/VocaNote.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/movies',
      name: 'movies',
      component: MovieListView
    },
    {
      path: '/:movieid',
      name:'movie-detail',
      component: MovieDetail
    },
    {
      path:'/login',
      name:'login',
      component: LogInView
    },
    {
      path:'/signup',
      name:'signup',
      component: SignUpView
    },
    {
      path:'/vocanote',
      name:'vocanote',
      component: VocaNote
    },
    {
      path:'/myprofie',
      name:'profile',
      component: ProfileView
    }
  ],
})

export default router
