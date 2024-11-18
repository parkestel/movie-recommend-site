<template>
  <div>
    <img :src="getImgUrl(movie.poster_path)" alt="">
    <h5>{{ movie.title }}</h5>
  </div>
</template>

<script setup>
defineProps({
  movie:Object
})


import { useMovieStore } from "@/stores/movie"

const store = useMovieStore()

const getImgUrl = function(poster_path) {
  return `${store.IMAGE_BASE_URL}/${poster_path}`
}
</script>

<style scoped>

</style>