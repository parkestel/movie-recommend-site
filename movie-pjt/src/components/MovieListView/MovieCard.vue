<template>
  <div>
    <button v-if="!isLiked(movie.id)" @click="store.addToggleWishMovie(movie.id)">🤍</button>
    <button v-else  @click="store.addToggleWishMovie(movie.id)">💖</button>

    <div>
      <img :src="store.getImgUrl(movie.poster_path,200)" alt="">
    </div>
    <h5>{{ movie.title }}</h5>
    <button @click="moveToDetail(movie.id)">Detail</button>
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

const isLiked = function (movieId) {
  return userProfile.value.wish_movies?.some(movie => movie.id===movieId)
}
</script>

<style scoped>

</style>