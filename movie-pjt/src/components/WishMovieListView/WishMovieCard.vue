<template>
  <div>
    <button v-if="!wishMovie.isLiked" @click="store.addToggleWishMovie(wishMovie.id)">🤍</button>
    <button v-else  @click="store.addToggleWishMovie(wishMovie.id)">💖</button>
    <div>
      <img :src="store.getImgUrl(wishMovie.poster_path,200)" alt="">
    </div>
    <h5>{{ wishMovie.title }}</h5>
    <button @click="moveToDetail(wishMovie.id)">Detail</button>
    <button @click="popUp(noteId)">VocaNote</button>
  </div>
</template>

<script setup>
defineProps({
  wishMovie:Object
})

import { useMovieStore } from "@/stores/movie"
import { useRouter } from "vue-router"
import { ref } from 'vue';

const store = useMovieStore()
const router = useRouter()

const noteId = ref(1)
// noteId는 현재 로그인된 유저, movieId를 가지고 해당 noteId를 반환하고,,, ref에 넣어줌
// voca note가 없으면 create, 있으면 해당 페이지로 넘어감!

const moveToDetail = function (movieId) {
  router.push({name:'movie-detail', params:{'movieid':movieId}})
}

const popUp = function (noteId) {
  window.open(`/note/${noteId}`, '__blank', 'width=400,height=650')
}
</script>

<style scoped>

</style>