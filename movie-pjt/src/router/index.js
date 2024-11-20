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
      path:'/logout',
      name:'logout',
      // https://codesandbox.io/p/sandbox/vue-router-logout-route-dcnh3?file=%2Fsrc%2Frouter%2Findex.js%3A28%2C7-43%2C8
      component: {
        beforeRouteEnter(to, from, next) {
          console.log({ from });
          const destination = {
            path: from.path || "/",
            query: from.query,
            params: from.params
          };
          if (!from) {
            console.log("no from");
          }
          console.log("running before hook");
          next(destination);
        }
      }
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
        }
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
