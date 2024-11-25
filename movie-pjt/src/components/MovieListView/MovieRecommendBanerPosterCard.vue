<template>
  <img :src="store.getImgUrl(movie.poster_path,780)" alt="" class="banner-img">
  <div class="carousel-caption d-none d-md-block">
  <div class="d-flex align-items-center h-100">
    <!-- 포스터 -->
    <div class="carousel-poster">
      <img :src="store.getImgUrl(movie.poster_path, 154)" alt="poster img">
    </div>
    <!-- 영화 정보 -->
    <div class="carousel-info ms-4">
      <h5 class="movie-title">{{ movie.title_kr }}</h5>
      <p class="movie-subtitle">{{ movie.title }} | 평점: {{ movie.rating }}</p>
      <p class="movie-overview">{{ movie.overview }}</p>
      <div class="genres mt-2">
        <span v-for="genre in movie.genres" :key="genre.id" class="badge bg-secondary me-1">{{ genre.name }}</span>
      </div>
    </div>
  </div>
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
.banner-img {
  width: 100%;
  height: 300px;
  object-fit: cover;
  opacity: 20%;
  border-radius: 1.5rem;
}

.carousel-caption {
  display: flex;
  align-items: center;
  justify-content: start;
  height: 100%;
  text-align: left;
}

.carousel-poster {
  flex-shrink: 0;
  max-height: 100%;
}

.carousel-poster img {
  max-height: 100%;
  width: auto;
  border-radius: 10px;
  object-fit: cover;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

.carousel-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
  max-width: 60%;
}

.movie-title {
  font-size: 1.8rem;
  font-weight: bold;
  margin-bottom: 0.5rem;
}

.movie-subtitle {
  font-size: 1rem;
  margin-bottom: 1rem;
}

.movie-overview {
  font-size: 0.9rem;
  line-height: 1.5;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: normal;
  max-height: 6rem;
}

.genres .badge {
  font-size: 0.8rem;
}


</style>