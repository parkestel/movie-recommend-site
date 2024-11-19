<template>
  <div>
    <h3>제목: {{ movieInfo.title }}</h3>
    <p>summary: {{ movieInfo.summary }}</p>
    <p>genre: {{ movieInfo.genre }}</p>
    <p>release_date: {{ movieInfo.release_date }}</p>
    <button v-if="!movieInfo.isLiked" @click="store.toggleLikeMovie(movieInfo.id)">🤍</button>
    <button v-else  @click="store.toggleLikeMovie(movieInfo.id)">💖</button>
  </div>
</template>

<script setup>
defineProps({
  movieInfo:Object
})

import { useMovieStore } from "@/stores/movie"

const store = useMovieStore()
</script>

<style scoped>

</style>