<template>
  <div>
    <button v-if="!wishMovie.isLiked" @click="store.toggleLikeMovie(wishMovie.id)">🤍</button>
    <button v-else  @click="store.toggleLikeMovie(wishMovie.id)">💖</button>
    <div>
      <img :src="store.getImgUrl(wishMovie.poster_path,200)" alt="">
    </div>
    <h5>{{ wishMovie.title }}</h5>
    <button @click="moveToDetail(wishMovie.id)">Detail</button>
  </div>
</template>

<script setup>
defineProps({
  wishMovie:Object
})

import { useMovieStore } from "@/stores/movie"
import { useRouter } from "vue-router"

const store = useMovieStore()
const router = useRouter()

const moveToDetail = function (movieId) {
  router.push({name:'movie-detail', params:{'movieid':movieId}})
}
</script>

<style scoped>

</style>