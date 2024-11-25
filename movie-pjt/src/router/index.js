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
import LikedReviews from '@/views/ProfileNesting/LikedReviews.vue'
import ChatBot from '@/components/chatBot.vue'
import HomeView from '@/views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path:'/',
      name:'home',
      component: HomeView
    },
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
      path:'/userinfoupdate/:username',
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
      component:VocaNotePopUpView,
      meta: { isPopup: true }, 
    },
    {
      path:'/profile/:username',
      name:'profile',
      component: ProfileView,
      redirect: to => {
        // 동적 매개변수 (:username) 사용
        return `/userlevel/${to.params.username}`;
      },
      children:[
        {
          path:'/userlevel/:username',
          name:'userlevel',
          component:MyLevel
        },
        {
          path:'/vocanotes/:username',
          name:'mynotelist',
          component: VocaNoteListView,
        },
        {
          path:'/mywishmovies/:username',
          name:'wishmovies',
          component:WishMovieListView
        },
        {
          path:'/myreviews/:username',
          name:'myreviews',
          component:MyReview
        },
        {
          path:'/likedreviews/:username',
          name:'likedreviews',
          component:LikedReviews
        },
      ]
    },
    {
      path:'/chatbot',
      name:'chatbot',
      component:ChatBot
    }
  ],
})

router.beforeEach((to, from) => {
  const store = useMovieStore()
  // 앞으로 로그인 권한이 필요한 곳이라면 로그인이 필요하다고 알려주고
  // 로그인 창으로 보내기
  if (to.name === 'movie-detail' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name:'login'}
  }
  if (to.name === 'userinfoupdate' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name:'login'}
  }
  if (to.name === 'accountdelete' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name:'login'}
  }
  if (to.name === 'password' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name:'login'}
  }
  if (to.name === 'vocanote' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name:'login'}
  }
  if (to.name === 'profile' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name:'login'}
  } 

  if (to.name === 'myreviews' && (store.logedinUsername !== to.params.username)) {
    return {name:'movies'}
  }

  if (to.name === 'likedreviews' && (store.logedinUsername !== to.params.username)) {
    return {name:'movies'}
  }

  if ((to.name === 'signup' || to.name === 'login') && (store.isLogin)) {
    window.alert('이미 로그인 되어 있습니다.')
    return {name:'movies'}
  }
})
export default router
