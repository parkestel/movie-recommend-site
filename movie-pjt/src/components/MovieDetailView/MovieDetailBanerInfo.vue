<template>
  <div>
    <h3>제목: {{ movieInfo.title }}</h3>
    <p>summary: {{ movieInfo.summary }}</p>
    <p>genre: {{ movieInfo.genres.map(genre => genre.name).join(' ') }}</p>
    <p>release_date: {{ movieInfo.release_date }}</p>
    <button v-if="!store.isLikedMovie(movieInfo.id)" @click="store.addToggleWishMovie(movieInfo.id)">🤍</button>
    <button v-else  @click="store.addToggleWishMovie(movieInfo.id)">💖</button>
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