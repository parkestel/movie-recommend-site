<template>
  <div class="movie-info">
    <div class="movie-header">
      <h3 class="movie-title">{{ movieInfo.title }}</h3>
      <span class="movie-release-date">({{ movieInfo.release_date }})</span>
    </div>
    <p class="movie-summary">{{ movieInfo.summary }}</p>
    <div class="movie-genres-actions">
      <div class="movie-genres">
        <button v-for="genre in movieInfo.genres" :key="genre.id" class="genre-button">
          {{ genre.name }}
        </button>
      </div>
      <button
        v-if="!store.isLikedMovie(movieInfo.id)"
        @click="store.addToggleWishMovie(movieInfo.id)"
        class="like-button"
      >
        🤍 Add to Favorites
      </button>
      <button
        v-else
        @click="store.addToggleWishMovie(movieInfo.id)"
        class="like-button liked"
      >
        💖 Favorited
      </button>
    </div>
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
.movie-info {
  position: absolute;
  bottom: 0;
  left: 0;
  height: 40%;
  color: #fff;
  background: rgba(0, 0, 0, 0.7);
  padding: 20px;
  border-radius: 10px;
  width: 100%;
  z-index: 2;
}

.movie-header {
  display: flex;
  align-items: baseline; /* 제목과 날짜 하단을 수평 정렬 */
  gap: 10px; /* 제목과 날짜 사이 간격 */
}

.movie-title {
  font-size: 1.8rem;
  font-weight: bold;
  color: #fff;
  margin: 0;
}

.movie-release-date {
  font-size: 0.9rem;
  color: #ccc;
  font-style: italic;
  margin-bottom: -3px; /* 하단 정렬 미세 조정 */
}

.movie-summary {
  margin-top: 10px;
  font-size: 1rem;
  color: #ddd;
  display: -webkit-box;
  -webkit-line-clamp: 2; /* 줄 수 제한 */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
}

.movie-genres-actions {
  display: flex;
  justify-content: space-between; /* 장르와 버튼 좌우 정렬 */
  align-items: center;
  margin: 10px 0;
}

.movie-genres {
  display: flex;
  gap: 10px;
  flex-wrap: wrap;
}

.genre-button {
  background-color: rgba(255, 255, 255, 0.1);
  color: #fff;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 20px;
  padding: 10px 20px;
  font-size: 0.9em;
  transition: all 0.3s ease;
}

/* .genre-button:hover {
  background-color: rgba(255, 255, 255, 0.3);
  border-color: rgba(255, 255, 255, 0.5);
} */

.like-button {
  background-color: rgba(255, 100, 100, 0.2); /* 배경색을 조금 더 진하게 */
  color: #fff;
  border: 1px solid rgba(255, 100, 100, 0.4); /* 테두리 색도 조금 더 진하게 */
  border-radius: 20px;
  padding: 10px 20px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.like-button:hover {
  background-color: rgba(255, 100, 100, 0.4); /* 호버 시 더 진한 배경 */
  border-color: rgba(255, 100, 100, 0.6); /* 호버 시 더 진한 테두리 */
}

.like-button.liked {
  background-color: rgba(255, 50, 50, 0.6); /* 선택된 상태에서 더 진한 배경 */
  border-color: rgba(255, 50, 50, 0.6); /* 선택된 상태에서 더 진한 테두리 */
}
</style>