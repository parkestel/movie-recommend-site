import { ref, computed, reactive } from 'vue'
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
  const genres = ref(null)
  const otts = ref(null)
  const difficulties = ref(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'])
  const wishMovies = ref(null)

  const vocaNoteList = ref([
    {id:1, movieId: 1, movie: 'Toy Story', is_public: true},
    {id:2, movieId: 1, movie: 'Toy Story', is_public: false},
    {id:3, movieId: 2, movie: 'Toy Story 2', is_public: true},
  ])

  const vocaList = ref([
    {id:1, word: 'toy', word_mean: '장난감', note_id: 1, examples:'I buy a toy', memo:'', is_memorized:true},
    {id:2, word: 'play', word_mean: '놀다', note_id: 1, examples:'I play with my sister', memo:'play-played-played', is_memorized:false},
  ])

  const userProfile = ref(null)
  
  const getMovies = function () {
    axios({
      method:'get',
      url:`${API_BASE_URL}/movies/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      // console.log(res.data)
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
    axios({
      method:'get',
      url:`${API_BASE_URL}/movies/wish-movie/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      wishMovies.value=res.data
    })
    .catch(err=>{
      console.log(err)
    })
  }

  const getGenres = function () {
    axios({
      method:'get',
      url:`${API_BASE_URL}/movies/genres-list/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      genres.value=res.data
    })
    .catch(err=>{
      console.log(err)
    })
  }

  const getOtts = function () {
    axios({
      method:'get',
      url:`${API_BASE_URL}/movies/otts-list/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      otts.value=res.data
    })
    .catch(err=>{
      console.log(err)
    })
  }

  const getUserProfile = function (username) {
    axios({
      method:'get',
      url:`${API_BASE_URL}/accounts/dj-rest-auth/user/${username}/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      userProfile.value=res.data
    })
    .catch(err=>{
      console.log(err)
    })
  }

  const toggleFollowerbutton = function (userId, username) {
    axios({
      method:'post',
      url:`${API_BASE_URL}/accounts/${userId}/follow/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      // console.log('팔로잉 완료')
      getUserProfile(username)
    })
    .catch(err=>{
      console.log('팔로우 실패')
      console.log(err)
    })
  }
  const getNote = function (noteId) {
    const targetNote = vocaNoteList.value.find((note)=>note.id===Number(noteId))
    return targetNote
  }

  const getVocas = function (noteId) {
    return vocaList.value.filter((voca)=>voca.note_id===Number(noteId))
  }

  const addToggleWishMovie = function (movieId){
    axios({
      method:'post',
      url:`${API_BASE_URL}/movies/${movieId}/wish-movie/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      console.log('좋아요 성공')
      getWishMovies()
    })
    .catch(err=>{
      console.log(err)
    })
  }

  const isLikedMovie = function (movieId) {
    return wishMovies.value?.some(movie => movie.id===movieId)
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
      console.log(err)
      window.alert('회원가입에 실패했습니다! 다시 시도 해주십시오.')
      router.push({name:'signup'})
    })
  }


  const logIn = function(payload) {

    if (!payload || !payload.username || !payload.password) {
      console.error("로그인 정보가 누락되었습니다.", payload);
      window.alert("아이디와 비밀번호를 입력해주세요.");
      return;
    }
    const username = payload.username;
    const password = payload.password;
  
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
      getLogedInUserName()
      getWishMovies()
      router.push({name:'movies'})
    })
    .catch(err=>{
      window.alert('로그인에 실패 했습니다!')
      // router.push({name:'login'})
    })
  }

  const logOut = function () {
    token.value=null
    logedinUsername.value=null
    userProfile.value=null
    axios({
      method:'post',
      url: `${API_BASE_URL}/accounts/dj-rest-auth/logout/`
    })
    .then(res=>{
      window.alert('Bye! See you soon')
      router.push({name:'login'})
    })
    .catch(err=>{
      window.alert('로그아웃에 실패했습니다.')
    })

  }

  const SignOut = function() {
    window.confirm('탈퇴하면 되돌릴 수 없습니다. 진행하시겠습니까?')
    logedinUsername.value = null
    token.value = null
    userProfile.value=null
    axios({
      method:'post',
      url:`${API_BASE_URL}/accounts/delete/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      window.alert('탈퇴 완료')
      router.push({name:'login'})
    })
    .catch(err=>{
      window.alert('탈퇴에 실패하셨습니다.')
    })
  }

  const getLogedInUserName = function() {
    axios({
      method:'get',
      url:`${API_BASE_URL}/accounts/dj-rest-auth/user/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      console.log(res.data)
      logedinUsername.value=res.data.username
    })
    .catch(err=>{
      console.log(err)
    })
  }
  
  return { API_BASE_URL, IMAGE_BASE_URL, movies, otts, difficulties, wishMovies, userProfile, genres, vocaNoteList, vocaList, getImgUrl, getMovies, getGenres, getOtts, getMovie, getUserProfile, toggleFollowerbutton, getNote, getVocas,  signUp, logIn, logOut, SignOut, getLogedInUserName, addToggleWishMovie, isLikedMovie, getWishMovies, deleteNote, token, isLogin, logedinUsername }
}, { persist: true })
