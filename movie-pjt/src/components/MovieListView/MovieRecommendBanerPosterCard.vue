<template>
  <img :src="store.getImgUrl(movie.poster_path,200)" alt="">
  <div class="carousel-caption d-none d-md-block">
    <h5>{{ movie.title_kr }}</h5>
    <p>{{ movie.title }}</p>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()
defineProps({
    movie:Object
})
</script>

<style scoped>

</style>