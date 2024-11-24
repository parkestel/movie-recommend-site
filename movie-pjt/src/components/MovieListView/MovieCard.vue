<template>
  <div @click="moveToDetail(movie.id)">
    <img :src="store.getImgUrl(movie.poster_path,200)" alt="" class="card-img" >
    <h4>{{ movie.title_kr }}</h4>
    <h5>{{ movie.title }}</h5>
    <button v-if="!store.isLikedMovie(movie.id)" @click="store.addToggleWishMovie(movie.id)" class="movie-like-button">🤍</button>
    <button v-else  @click="store.addToggleWishMovie(movie.id)" class="movie-like-button">💖</button>
  </div>
</template>

<script setup>
defineProps({
  movie:Object
})

import { useMovieStore } from "@/stores/movie"
import { storeToRefs } from "pinia";
import { useRouter } from 'vue-router'

const store = useMovieStore()
const router = useRouter()
const { userProfile } = storeToRefs(store)

const moveToDetail = function (movieId) {
  router.push({name:'movie-detail', params:{'movieid':movieId}})
}

// const isLikedMovie = function (movieId) {
//   return userProfile.value.wish_movies?.some(movie => movie.id===movieId)
// }
</script>

<style scoped>

</style>