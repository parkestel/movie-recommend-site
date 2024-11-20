import { createRouter, createWebHistory } from 'vue-router'
import MovieListView from '@/views/MovieListView.vue'
import MovieDetail from '@/views/MovieDetailView.vue'
import LogInView from '@/views/LogInView.vue'
import SignUpView from '@/views/SignUpView.vue'
import ProfileView from '@/views/ProfileView.vue'
import VocaNoteListView from '@/views/ProfileNesting/VocaNoteListView.vue'
import { useMovieStore } from '@/stores/movie'
import WishMovieListView from '@/views/ProfileNesting/WishMovieListView.vue'
import VocaNotePopUpView from '@/views/VocaNotePopUpView.vue'
import MyLevel from '@/views/ProfileNesting/MyLevel.vue'
import UserInfoUpdateView from '@/views/UserInfoUpdateView.vue'
import UserAccountDeleteView from '@/views/UserAccountDeleteView.vue'
import PasswordUpdateView from '@/views/PasswordUpdateView.vue'
import MyReview from '@/views/ProfileNesting/MyReview.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/movies',
      name: 'movies',
      component: MovieListView
    },
    {
      path: '/movies/:movieid',
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
      path:'/userinfoupdate',
      name:'userinfoupdate',
      component:UserInfoUpdateView
    },
    {
      path:'/accountdelete',
      name:'accountdelete',
      component:UserAccountDeleteView
    },
    {
      path:'/password',
      name:'password',
      component:PasswordUpdateView
    },
    {
      path:'/note/:note_id',
      name:'vocanote',
      component:VocaNotePopUpView
    },
    {
      path:'/myprofie',
      component: ProfileView,
      children:[
        {
          path:'',
          name:'profile',
          component:MyLevel
        },
        {
          path:'/vocanotes',
          name:'mynotelist',
          component: VocaNoteListView,
        },
        {
          path:'/mywishmovies',
          name:'wishmovies',
          component:WishMovieListView
        },
        {
          path:'/myreviews',
          name:'myreviews',
          component:MyReview
        },
      ]
    },

  ],
})

router.beforeEach((to, from) => {
  const store = useMovieStore()
  // 앞으로 로그인 권한이 필요한 곳이라면 로그인이 필요하다고 알려주고
  // 로그인 창으로 보내기
})
export default router
