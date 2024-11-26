<template>
  <div class="banner-slide-content">
    <img :src="store.getImgUrl(movie.poster_path,780)" alt="" class="banner-img">
    <div class="carousel-caption">
      <div class="content-wrapper">
        <!-- 포스터 -->
        <div class="carousel-poster">
          <img :src="store.getImgUrl(movie.poster_path, 154)" alt="poster img" @click="goToDetail(movie.id)">
        </div>
        <!-- 영화 정보 -->
        <div class="carousel-info">
          <h5 class="movie-title">{{ movie.title_kr }}</h5>
          <p class="movie-subtitle">{{ movie.title }} | 평점: {{ movie.rank }}</p>
          <p class="movie-overview">{{ movie.summary }}</p>
          <div class="genres">
            <span v-for="genre in movie.genres" :key="genre.id" class="badge bg-secondary me-1">{{ genre.name }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { useRouter } from 'vue-router';

const router = useRouter()
const store = useMovieStore()

defineProps({
    movie:Object
})

const goToDetail = function (movieId) {
  router.push({name:'movie-detail', params:{movieid:movieId}})
}
</script>

<style scoped>
.banner-slide-content {
  position: relative;
  width: 100%;
  height: 100%;
  overflow: hidden;
}

.banner-img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
  filter: brightness(0.5);
}

.carousel-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 2rem;
  background: linear-gradient(to top, rgba(0,0,0,0.8), transparent);
  color: white;
  height: 100%;
  display: flex;
  align-items: center;
}

.content-wrapper {
  display: flex;
  align-items: center;
  gap: 2rem;
  max-width: 1200px;
  margin: 0 auto;
}

.carousel-poster img {
  width: 200px;
  height: 300px;
  object-fit: cover;
  border-radius: 8px;
  box-shadow: 0 4px 8px rgba(0,0,0,0.3);
  transition: transform 0.2s;
}

.carousel-poster img:hover {
  transform: scale(1.05);
  cursor: pointer;
}

.carousel-info {
  flex: 1;
}

.movie-title {
  font-size: 2rem;
  margin-bottom: 0.5rem;
  font-weight: bold;
  text-align: left;
}

.movie-subtitle {
  font-size: 1.1rem;
  opacity: 0.8;
  margin-bottom: 1rem;
  text-align: left;
}

.movie-overview {
  font-size: 1rem;
  line-height: 1.6;
  margin-bottom: 1rem;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-align: left;
}

.genres {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.badge {
  padding: 0.5rem 1rem;
  font-size: 0.9rem;
}
</style>