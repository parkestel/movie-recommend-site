<template>
  <div>
    <div>
      <img :src="getImgUrl(movie.poster_path)" alt="">
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

const getImgUrl = function(poster_path) {
  return `${store.IMAGE_BASE_URL}/${poster_path}`
}

const moveToDetail = function (movieId) {
  router.push({name:'movie-detail', params:{'movieid':movieId}})
}
</script>

<style scoped>

</style>