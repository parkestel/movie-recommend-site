<template>
  <div class="movie-detail">
    <div class="movie-poster">
      <img :src="store.getImgUrl(movieInfo.poster_path, 500)" alt="Poster" />
    </div>
    <MovieDetailInfo :movie-info="movieInfo"/>
  </div>
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
.movie-detail {
  position: relative;
  width: 100%;
  height: 500px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  border-radius: 10px;
}

.movie-poster {
  width: 100%;
  height: 100%;
  position: relative;
}

.movie-poster img {
  width: 100%;
  height: 100%;
  opacity: 60%;
  object-fit: cover; /* 비율을 유지하면서 영역에 맞게 확대/축소 */
}

</style>