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
  const todayRandomMovie = ref(null)
  const genres = ref(null)
  const otts = ref(null)
  const difficulties = ref(['A1', 'A2', 'B1', 'B2', 'C1', 'C2'])
  const wishMovies = ref(null)
  const wishMoviesWithOutNote = ref(null)
  const vocaNoteList = ref(null)
  const vocaList = ref(null)
  const vocaNote = ref(null)
  const userProfile = ref(null)
  const moviecomments = ref(null)
  const movieBestComments = ref(null)
  const myReviews = ref(null)
  const myLikedReviews = ref(null)
  const isLoading = ref(true)
  const isDataLoaded = ref(false)
  const logedinUserPoint = ref(0)
  
  const getMovies = function () {
    console.log('getMovies 호출됨, token:', token.value)
    isLoading.value = true
    isDataLoaded.value = false
    
    return new Promise((resolve, reject) => {
      axios({
        method:'get',
        url:`${API_BASE_URL}/movies/`,
        headers:{
          Authorization: `Token ${token.value}`
        }
      })
      .then(res => {
        movies.value = res.data
        resolve(res.data)
      })
      .catch(err => {
        if (err.response && err.response.status === 401 && token.value) {
          token.value = null
          logedinUsername.value = null
          userProfile.value = null
          router.push({name:'login'})
        }
        reject(err)
      })
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
    console.log('getWishMovies 호출됨, token:', token.value)
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
      if (err.response && err.response.status === 401 && token.value) {
        token.value=null
        logedinUsername.value=null
        userProfile.value=null
        router.push({name:'login'})
      }
    })
  }

  const getRandomMovies = function () {
    return new Promise((resolve, reject) => {
      axios({
        method:'get',
        url:`${API_BASE_URL}/movies/random-movies/`,
        headers:{
          Authorization: `Token ${token.value}`
        }
      })
      .then(res => {
        console.log('Random movies response:', res.data)
        todayRandomMovie.value = Array.isArray(res.data) ? res.data : [res.data]
        console.log('Stored random movies:', todayRandomMovie.value)
        resolve(res.data)
      })
      .catch(err => {
        console.error('Random movies loading error:', err)
        todayRandomMovie.value = []
        if (err.response && err.response.status === 401 && token.value) {
          token.value = null
          logedinUsername.value = null
          userProfile.value = null
          router.push({name:'login'})
        }
        reject(err)
      })
    })
  }

  const getWishMovieWithOutNote = function () {
    axios({
      method:'get',
      url:`${API_BASE_URL}/movies/wish-movies-without-vocanote/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      wishMoviesWithOutNote.value=res.data
    })
    .catch(err=>{
      if (err.response && err.response.status === 401 && token.value) {
        token.value=null
        logedinUsername.value=null
        userProfile.value=null
        router.push({name:'login'})
      }
    })
  }

  const getGenres = function () {
    return new Promise((resolve, reject) => {
      axios({
        method:'get',
        url:`${API_BASE_URL}/movies/genres-list/`,
        headers:{
          Authorization: `Token ${token.value}`
        }
      })
      .then(res => {
        genres.value = res.data
        resolve(res.data)
      })
      .catch(err => {
        if (err.response && err.response.status === 401 && token.value) {
          token.value = null
          logedinUsername.value = null
          userProfile.value = null
          router.push({name:'login'})
        }
        reject(err)
      })
    })
  }

  const getOtts = function () {
    return new Promise((resolve, reject) => {
      axios({
        method:'get',
        url:`${API_BASE_URL}/movies/otts-list/`,
        headers:{
          Authorization: `Token ${token.value}`
        }
      })
      .then(res => {
        otts.value = res.data
        resolve(res.data)
      })
      .catch(err => {
        if (err.response && err.response.status === 401 && token.value) {
          token.value = null
          logedinUsername.value = null
          userProfile.value = null
          router.push({name:'login'})
        }
        reject(err)
      })
    })
  }

  const getUserProfile = function (username) {
    console.log('getUserProfile 호출됨, token:', token.value)
    axios({
      method:'get',
      url:`${API_BASE_URL}/accounts/dj-rest-auth/user/${username}/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      userProfile.value=res.data
      getVocaNote(userProfile.value.id)
      getWishMovieWithOutNote()
    })
    .catch(err=>{
      if (err.response && err.response.status === 401 && token.value) {
        token.value=null
        logedinUsername.value=null
        userProfile.value=null
        router.push({name:'login'})
      }
    })
  }

  const getMyLevel = function () {
    axios({
      method:'get',
      url:`${API_BASE_URL}/accounts/dj-rest-auth/user/level/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      logedinUserPoint.value=res.data
    })
    .catch(err=>{
      if (err.response && err.response.status === 401 && token.value) {
        token.value=null
        logedinUsername.value=null
        userProfile.value=null
        router.push({name:'login'})
      }
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
      // console.log('팔로우 실패')
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const getNote = function (noteId) {
    const targetNote = vocaNoteList.value.find((note)=>note.id===Number(noteId))
    return targetNote
  }

  const getVocaNote = function (profileuserId) {
    axios({
      method:'get',
      url:`${API_BASE_URL}/voca/vocanote/list/${profileuserId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      vocaNoteList.value = res.data
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const createVocaNote = function (movieId, userId) {
    axios({
      method:'post',
      url:`${API_BASE_URL}/voca/${movieId}/vocanote/create/${userId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      window.open(`/note/${res.data.id}`, '__blank', 'width=400,height=650')
      // router.push({name:'vocanote', params:{note_id:res.data.id}})
      getVocaNote(userId)
      getWishMovieWithOutNote()
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    }) 
  }

  const deleteNote = function (movieId, userId) {
    axios({
      method:'delete',
      url:`${API_BASE_URL}/voca/${movieId}/vocanote/create/${userId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      getVocaNote(userId)
      getWishMovieWithOutNote()
      getWishMovies()
      return res
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
      throw err
    })
  }

  const togglePublicVocaNote = function (movieId, userId) {
    axios({
      method:'put',
      url:`${API_BASE_URL}/voca/${movieId}/vocanote/ispublic/${userId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      getVocaNote(userId)
      getVocas(res.data.id)
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const getVocas = function (noteId) {
    axios({
      method:'get',
      url:`${API_BASE_URL}/voca/vocanote-detail/${noteId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      vocaList.value = res.data
      // console.log(res.data)
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
    // return vocaList.value.filter((voca)=>voca.note_id===Number(noteId))
  }

  const createVoca = function(noteId, payload){
    axios({
      method:'post',
      url: `${API_BASE_URL}/voca/create-voca/${noteId}/`,
      data:{
        word: payload.word,
        word_mean: payload.word_mean,
        examples: payload.examples,
        memo: payload.memo,
        is_memorized: false
      },
      headers:{
          Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      getVocas(noteId)
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const deleteVoca = function(vocaId,noteId) {
    axios({
      method:'delete',
      url:`${API_BASE_URL}/voca/delete-voca/${noteId}/${vocaId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      getVocas(noteId)
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const updateVoca = function (vocaId,noteId,payload) {
    axios({
      method:'put',
      url:`${API_BASE_URL}/voca/update-voca/${noteId}/${vocaId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
      data:{
        word: payload.word,
        word_mean: payload.word_mean,
        examples: payload.examples,
        memo: payload.memo,
      }
    })
    .then(res=>{
      getVocas(noteId)
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const memorizedVoca = function(vocaId, noteId) {
    axios({
      method:'post',
      url:`${API_BASE_URL}/voca/${noteId}/is_memorized/${vocaId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      getVocas(noteId)
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
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
      // console.log('좋아요 성공')
      getWishMovies()
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const isLikedMovie = function (movieId) {
    return wishMovies.value?.some(movie => movie.id===movieId)
  }

  const getMovieComments = function (movieId) {
    axios({
      method:'get',
      url:`${API_BASE_URL}/movies/comment-list/${movieId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      }
    })
    .then(res=>{
      moviecomments.value=res.data
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const createComment = function (movieId, payload) {
    axios({
      method:'post',
      url:`${API_BASE_URL}/movies/${movieId}/create-comment/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
      data:{
        content: payload.content
      }
    })
    .then(res=>{
      getMovieComments(movieId)
      getBestComments(movieId)
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const likeCommentsinMovie = function (reviewId, movieId) {
    axios({
      method: 'post',
      url:`${API_BASE_URL}/movies/like-comment/${reviewId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
    })
    .then(res=>{
      // console.log("댓글 추천 토글")
      getMovieComments(movieId)
      getBestComments(movieId)
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const deleteCommentinMovie = function (reviewId, movieId) {
    axios({
      method:'delete',
      url:`${API_BASE_URL}/movies/comment-list/delete/${reviewId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
    })
    .then(res=>{
      // console.log('댓글 삭제 완료')
      getMovieComments(movieId)
      getBestComments(movieId)
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const updateCommentinMovie = function(reviewId, movieId, payload) {
    axios({
      method:'put',
      url:`${API_BASE_URL}/movies/${movieId}/comment-update/${reviewId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
      data:{
        content: payload.content
      }
    })
    .then(res=>{
      // console.log('댓글 수정 완료')
      getMovieComments(movieId)
      getBestComments(movieId)
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const getBestComments = function(movieId) {
    axios({
      method:'get',
      url:`${API_BASE_URL}/movies/top-5-comment/${movieId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
    })
    .then(res=>{
      movieBestComments.value = res.data
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const getMyReviews = function() {
    axios({
      method:'get',
      url:`${API_BASE_URL}/movies/comment-list/user/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
    })
    .then(res=>{
      myReviews.value=res.data
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const getLikedReviewInMyPage = function() {
    axios({
      method:'get',
      url:`${API_BASE_URL}/movies/like-comment/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
    })
    .then(res=>{
      myLikedReviews.value=res.data
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const deleteCommentinMyPage = function (reviewId) {
    axios({
      method:'delete',
      url:`${API_BASE_URL}/movies/comment-list/delete/${reviewId}/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
    })
    .then(res=>{
      // console.log('댓글 삭제 완료')
      getMyReviews()
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
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
    .then((res)=>{
      // console.log('회원가입 완료')
      // 자동 로그인 구현
      const password = password1
      logIn({username, password})
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
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
    .then((res)=>{
      token.value = res.data.key
      getLogedInUserName()
      getWishMovies()
      getMyLevel()
      router.push({name:'movies'})
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
      // window.alert('로그인에 실패 했습니다!')
      // router.push({name:'login'})
    })
  }

  const logOut = function () {
    console.log('로그아웃 시작')
    // 먼저 상태 초기화
    token.value = null
    logedinUsername.value = null
    userProfile.value = null
    wishMovies.value = null
    todayRandomMovie.value = null
    movies.value = []  // 이것도 초기화
    
    axios({
      method: 'post',
      url: `${API_BASE_URL}/accounts/dj-rest-auth/logout/`
    })
    .then(res => {
      console.log('로그아웃 성공')
      window.alert('Bye! See you soon')
      router.push({ name: 'home' })
    })
    .catch(err => {
      console.log('로그아웃 에러')
      router.push({ name: 'home' })
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
      router.push({name:'home'})
    })
    .catch(err=>{
      if (err) {
        let values = Object.values(err.response.data);
        let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
        window.alert(formattedData);
        // window.alert('탈퇴에 실패하셨습니다.')
      }
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
      // console.log(res.data)
      logedinUsername.value=res.data.username
    })
    .catch(err=>{
      // console.log(err)
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const updateUserInfo = function(payload, username){
    axios({
      method:'put',
      url:`${API_BASE_URL}/accounts/user/update/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
      data:{
        last_name:payload.last_name,
        first_name:payload.first_name,
        nickname:payload.nickname,
        email:payload.email,
        birth:payload.birth
      }
    })
    .then(res=>{
      getLogedInUserName()
      getUserProfile(username)
      router.push({name:'profile', params:{username:username}})
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const userInfo = ref(null)
  const getUserInfoForUpdate = function () {
    axios({
      method:'get',
      url:`${API_BASE_URL}/accounts/user/update/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
    })
    .then(res=>{
      // console.log(res.data)
      userInfo.value = res.data
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }

  const updateUserStudyLevel = function(payload, username){
    axios({
      method:'put',
      url:`${API_BASE_URL}/accounts/user/update/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
      data:{
        study_level:payload.study_level
      }
    })
    .then(res=>{
      getUserProfile(username)
      router.push({name:'profile', params:{username:username}})
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }
  
  
  const changePassword = function (payload) {
    axios({
      method:'post',
      url:`${API_BASE_URL}/accounts/dj-rest-auth/password/change/`,
      headers:{
        Authorization: `Token ${token.value}`
      },
      data: {
        new_password1:payload.new_password1,
        new_password2:payload.new_password2,
      }
    })
    .then(res=>{
      window.alert('비밀번호 변경이 완료 되었습니다.')
      router.push({name:'movies'})
    })
    .catch(err=>{
      let values = Object.values(err.response.data);
      let formattedData = values.join("\n");  // 각 값을 줄바꿈으로 구분
      window.alert(formattedData);
    })
  }
      isLoading.value=false
  return { API_BASE_URL, IMAGE_BASE_URL, movies, todayRandomMovie, otts, difficulties, wishMovies, userProfile, genres, isLoading, vocaNoteList, vocaList, wishMoviesWithOutNote, vocaNote, moviecomments, movieBestComments, myReviews, myLikedReviews, getImgUrl, getMovies, getRandomMovies, getGenres, getOtts, getMovie, getMyLevel, getUserProfile, getVocaNote, getWishMovieWithOutNote, getNote, createVocaNote, togglePublicVocaNote, toggleFollowerbutton, getVocas, createVoca, deleteVoca, updateVoca, memorizedVoca, getMovieComments, createComment, likeCommentsinMovie, deleteCommentinMovie, updateCommentinMovie, getBestComments, getMyReviews, deleteCommentinMyPage, getLikedReviewInMyPage, signUp, logIn, logOut, SignOut, getLogedInUserName, addToggleWishMovie, isLikedMovie, getWishMovies, deleteNote, updateUserInfo, getUserInfoForUpdate, updateUserStudyLevel, changePassword, token, isLogin, logedinUsername, logedinUserPoint, userInfo, isDataLoaded }
}, { persist: true })
