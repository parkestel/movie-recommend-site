<template>
  <div class="movie-detail">
    <div class="movie-poster">
      <img :src="store.getImgUrl(movieInfo.poster_path, 780)" alt="Poster" />
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
  width: 80%;
  max-width: 1200px;
  height: 900px;
  display: flex;
  justify-content: center;
  align-items: center;
  overflow: hidden;
  border-top-left-radius: 2rem;
  border-top-right-radius: 2rem;
  margin: 20px auto 0;
}

.movie-poster {
  width: 100%;
  height: 100%;
  position: relative;
}

.movie-poster::after {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: linear-gradient(
    to bottom,
    rgba(0, 0, 0, 0) 0%,
    rgba(0, 0, 0, 0.4) 50%,
    rgba(0, 0, 0, 0.8) 70%,
    rgba(0, 0, 0, 0.95) 100%
  );
  pointer-events: none;
}

.movie-poster img {
  width: 100%;
  height: 100%;
  opacity: 70%;
  object-fit: cover; /* 비율을 유지하면서 영역에 맞게 확대/축소 */
  object-position: top; /* 이미지를 상단과 맞추기 */
}
</style>