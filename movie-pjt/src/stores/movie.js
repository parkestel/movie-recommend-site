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
    { id: 1, title: 'Toy Story', tmdb_id: 862, summary:'summary of movie', release_date: '1995-04-01', genre:'Animation', poster_path:'/uXDfjJbdP4ijW5hWSBrPrlKpxab.jpg', isLiked: true},
    { id: 2, title: 'Toy Story 2', tmdb_id: 9082, summary:'summary of movie', release_date: '2003-04-01', genre:'Animation',  poster_path:'/2MFIhZAW0CVlEQrFyqwa4U6zqJP.jpg', isLiked: false},
    { id: 3, title: 'Toy Story 3', tmdb_id: 234235, summary:'summary of movie', release_date: '2009-04-01', genre:'Animation', poster_path:'/AbbXspMOwdvwWZgVN0nabZq03Ec.jpg', isLiked: false}
  ])

  const vocaNoteList = ref([
    {id:1, movieId: 1, movie: 'Toy Story', is_public: true},
    {id:2, movieId: 1, movie: 'Toy Story', is_public: false},
    {id:3, movieId: 2, movie: 'Toy Story 2', is_public: true},
  ])
  

  const getImgUrl = function(poster_path,width) {
    return `${IMAGE_BASE_URL}/w${width}/${poster_path}`
  }

  const getMovie = function (movieId) {
    const targetMovie = movies.value.find((movie)=>movie.id==Number(movieId))
    return targetMovie
  }

  const getWishMovies = function () {
    return movies.value.filter((movie)=>movie.isLiked===true)
  }

  const getNote = function (noteId) {
    const targetNote = vocaNoteList.value.find((note)=>note.id===Number(noteId))
    return targetNote
  }

  const toggleLikeMovie = function (movieId){
    const targetMovieId = movies.value.findIndex((movie)=>movie.id==movieId)
    const isLiked = movies.value[targetMovieId].isLiked
    movies.value[targetMovieId].isLiked = !isLiked
  }


  const logIn = function(payload) {
    const username = payload.username
    const password = payload.password
    // axios 요청...! then -> token 값 받아오기
  }
  
  return { IMAGE_BASE_URL, movies, vocaNoteList, getImgUrl, getMovie, getNote, logIn, toggleLikeMovie, getWishMovies, token, isLogin }

})
