<template>
  <div>
    <img :src="store.getImgUrl(movieInfo.poster_path,500)" alt="">
  </div>
  <MovieDetailInfo :movie-info="movieInfo"/>
</template>

<script setup>
defineProps({
  movieInfo:Object
})

import { useMovieStore } from '@/stores/movie';
import MovieDetailInfo from '@/components/MovieDetailView/MovieDetailBanerInfo.vue';

const store = useMovieStore()

</script>
<style scoped>

</style>