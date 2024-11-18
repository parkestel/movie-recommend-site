import { ref, computed } from 'vue'
import { defineStore } from 'pinia'

export const useMovieStore = defineStore('movie', () => {
  const token = ref(null)
  const IMAGE_BASE_URL = 'https://image.tmdb.org/t/p'

  const isLogin = computed(()=>{
    if (token.value===null) {
      return false
    } else {
      return true
    }
  })

  const movies = ref([
    { id: 1, title: 'Toy Story', tmdb_id: 862, summary:'summary of movie', release_date: '1995-04-01', genre:'Animation', poster_path:'/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg' },
    { id: 2, title: 'Toy Story 2', tmdb_id: 9082, summary:'summary of movie', release_date: '2003-04-01', genre:'Animation',  poster_path:'/2MFIhZAW0CVlEQrFyqwa4U6zqJP.jpg'},
    { id: 3, title: 'Toy Story 3', tmdb_id: 234235, summary:'summary of movie', release_date: '2009-04-01', genre:'Animation', poster_path:'/AbbXspMOwdvwWZgVN0nabZq03Ec.jpg'},
  ])

  const getImgUrl = function(poster_path,width) {
    return `${IMAGE_BASE_URL}/w${width}/${poster_path}`
  }

  const getMovie = function (movieId) {
    const targetMovie = movies.value.find((movie)=>movie.id==Number(movieId))
    return targetMovie
  }

  const logIn = function(payload) {
    const username = payload.username
    const password = payload.password
    // axios 요청...! then -> token 값 받아오기
  }
  return { IMAGE_BASE_URL, movies, getImgUrl, getMovie, logIn, token, isLogin }
})
