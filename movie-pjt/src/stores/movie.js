import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'


export const useMovieStore = defineStore('movie', () => {
  const router = useRouter()
  const token = ref(null)
  const logedinUsername = ref(null)
  const API_BASE_URL = 'http://127.0.0.1:8000'
  const IMAGE_BASE_URL = 'https://image.tmdb.org/t/p'

  const isLogin = computed(()=>{
    if (token.value===null) {
      return false
    } else {
      return true
    }
  })

  const movies = ref([])

  const genres = ref([
    {id: 1, name: 'Animation'},
    {id: 2, name:'Adventure'},
  ])

  const vocaNoteList = ref([
    {id:1, movieId: 1, movie: 'Toy Story', is_public: true},
    {id:2, movieId: 1, movie: 'Toy Story', is_public: false},
    {id:3, movieId: 2, movie: 'Toy Story 2', is_public: true},
  ])

  const vocaList = ref([
    {id:1, word: 'toy', word_mean: '장난감', note_id: 1, examples:'I buy a toy', memo:'', is_memorized:true},
    {id:2, word: 'play', word_mean: '놀다', note_id: 1, examples:'I play with my sister', memo:'play-played-played', is_memorized:false},
  ])
  
  const getMovies = function () {
    axios({
      method:'get',
      url:`${API_BASE_URL}/movies/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      console.log(res.data)
      movies.value = res.data
    })
    .catch(err=>{
      console.log(err)
    })
  }
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

  const getVocas = function (noteId) {
    return vocaList.value.filter((voca)=>voca.note_id===Number(noteId))
  }

  const addWishMovie = function (movieId){
    axios({
      method:'post',
      url:`${API_BASE_URL}/movies/${movieId}/wish-movie/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      console.log('좋아요 성공')

    })
    .catch(err=>{
      console.log(err)
    })
  }

  const deleteNote = function (id) {
    const targetId = vocaNoteList.value.findIndex(note => note.id===id)
    vocaNoteList.value.splice(targetId, 1)
  }

  const signUp = function (payload) {
    const username = payload.username
    const password1 = payload.password1
    const password2 = payload.password2
    const email = payload.email
    const last_name = payload.last_name
    const first_name = payload.first_name
    const birth = payload.birth
    const nickname = payload.nickname
    const study_level = payload.study_level

    axios({
      method:'post',
      url:`${API_BASE_URL}/accounts/dj-rest-auth/registration/`,
      data: {
        username,
        password1,
        password2,
        email,
        last_name,
        first_name,
        birth,
        nickname,
        study_level,
      }
    })
    .then(res=>{
      // console.log('회원가입 완료')
      // 자동 로그인 구현
      const password = password1
      logIn({username, password})
      router.push({name:'movies'})
    })
    .catch(err=>{
      window.alert('회원가입에 실패했습니다! 다시 시도 해주십시오.')
      router.push({name:'signup'})
    })
  }


  const logIn = function(payload) {
    const username = payload.username
    const password = payload.password
    // axios 요청...! then -> token 값 받아오기
    axios({
      method:'post',
      url:`${API_BASE_URL}/accounts/dj-rest-auth/login/`,
      data:{
        username, password
      }
    })
    .then(res=>{
      token.value = res.data.key
      getLogedInUserName(token.value)
      localStorage
      console.log(res)
      router.push({name:'movies'})
    })
    .catch(err=>{
      window.alert('로그인에 실패 했습니다!')
      router.push({name:'login'})
    })
  }

  const logOut = function () {
    axios({
      method:'post',
      url: `${API_BASE_URL}/accounts/dj-rest-auth/logout/`
    })
    .then(res=>{
      token.value=null
      userPk.value=null
      window.alert('Bye! See you soon')
      router.push({name:'login'})
    })
    .catch(err=>{
      window.alert('로그아웃에 실패했습니다.')
    })

  }

  const getLogedInUserName = function(key) {
    axios({
      method:'get',
      url:``,
      params:{
        key:key
      }
    })
    .then(res=>{
      logedinUsername.value=res.data.username
    })
    .catch(err=>{
      console.log(err)
    })
  }
  
  return { API_BASE_URL, IMAGE_BASE_URL, movies, genres, vocaNoteList, vocaList, getImgUrl, getMovies, getMovie, getNote, getVocas,  signUp, logIn, logOut, getLogedInUserName, addWishMovie, getWishMovies, deleteNote, token, isLogin, logedinUsername }
}, { persist: true })
