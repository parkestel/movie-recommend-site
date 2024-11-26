<template>
  <div>
    <div>
      <img :src="store.getImgUrl(wishMovie.poster_path,200)" alt="" class="card-img"  @click="moveToDetail(wishMovie.id)">
    </div>
    <h4>{{ wishMovie.title_kr }}</h4>
    <h5>{{ wishMovie.title }}</h5>
    <button v-if="!store.isLikedMovie(wishMovie.id)" @click="store.addToggleWishMovie(wishMovie.id)" class="movie-like-button">🤍</button>
    <button v-else  @click="store.addToggleWishMovie(wishMovie.id)" class="movie-like-button">🖤</button>
    <div v-if="userProfile.username === store.logedinUsername">
      <button class="btn" v-if="isHavingNote(wishMovie.id)" @click="popUp(findNoteIdByMovieId(wishMovie.id))">See VocaNote</button>
    </div>
  </div>
</template>

<script setup>
defineProps({
  wishMovie:Object
})

import { useMovieStore } from "@/stores/movie"
import { useRouter } from "vue-router"
import { onMounted, ref } from 'vue';
import { storeToRefs } from "pinia";

const store = useMovieStore()
const router = useRouter()
const { userProfile, vocaNoteList } = storeToRefs(store)

const noteId = ref(1)
// noteId는 현재 로그인된 유저, movieId를 가지고 해당 noteId를 반환하고,,, ref에 넣어줌
// voca note가 없으면 create, 있으면 해당 페이지로 넘어감!

const moveToDetail = function (movieId) {
  router.push({name:'movie-detail', params:{'movieid':movieId}})
}

const isHavingNote = function (movieId) {
  return vocaNoteList.value.some((note)=>note.movies[0].id===movieId)
}
const popUp = function (noteId) {
  window.open(`/note/${noteId}?isPopup=true`, '__blank', 'width=400,height=650')
}

const findNoteIdByMovieId = (movieId) => {
  // vocaNoteList를 순회하면서
  for (const note of vocaNoteList.value) {
    // 각 노트의 movies 배열을 확인
    const foundMovie = note.movies.find(movie => movie.id === movieId)
    if (foundMovie) {
      // 영화를 포함하고 있는 노트의 ID를 반환
      return note.id
    }
  }
  return null
}

onMounted(()=>{
  store.getVocaNote(userProfile.value.id)
})
</script>

<style scoped>

</style>