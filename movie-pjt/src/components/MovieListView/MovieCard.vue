<template>
  <div>
    <button v-if="!movie.isLiked" @click="store.addWishMovie(movie.id)">🤍</button>
    <button v-else  @click="store.toggleLikeMovie(movie.id)">💖</button>

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
import { useRouter } from 'vue-router'

const store = useMovieStore()
const router = useRouter()

const moveToDetail = function (movieId) {
  router.push({name:'movie-detail', params:{'movieid':movieId}})
}
</script>

<style scoped>

</style>