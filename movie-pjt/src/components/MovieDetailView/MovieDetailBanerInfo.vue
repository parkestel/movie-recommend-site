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

    <!-- 추가 정보 섹션 -->
    <div class="additional-info">
      <div class="info-row">
        <div class="info-item directors-item">
          <span class="info-label">감독</span>
          <div class="directors-list">
            <div v-for="director in movieInfo.directors" :key="director.tmdb_id" class="director">
              <img 
                :src="store.getImgUrl(director.profile_path, 45)" 
                :alt="director.name"
                class="director-image"
              >
              <span class="info-value">{{ director.name }}</span>
            </div>
          </div>
        </div>
        <div class="info-item">
          <span class="info-label">평점</span>
          <span class="info-value">⭐ {{ movieInfo.rank }}</span>
        </div>
      </div>

      <div class="info-row">
        <div class="info-item actors-item">
          <span class="info-label">주연</span>
          <div class="actors-list">
            <div v-for="actor in movieInfo.stars" 
                 :key="actor.tmdb_id" 
                 class="actor"
                 :title="actor.characters[0].character">
              <img 
                :src="store.getImgUrl(actor.profile_path, 45)" 
                :alt="actor.name"
                class="actor-image"
              >
              <div class="actor-info">
                <span class="info-value">{{ actor.name_kr || actor.name }}</span>
                <span class="character-name">{{ actor.characters[0].character }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- OTT 섹션 -->
      <div class="ott-section">
        <span class="info-label">시청 가능한 곳</span>
        <div v-if="movieInfo.otts && movieInfo.otts.length > 0" class="ott-logos">
          <a v-for="ott in movieInfo.otts" 
             :key="ott.tmdb_id"
             :href="ott.site_url"
             target="_blank"
             class="ott-link"
             :title="ott.name">
            <img :src="store.getImgUrl(ott.logo_path, 45)" :alt="ott.name" class="ott-logo">
          </a>
        </div>
        <div v-else class="no-ott-message">
          현재 스트리밍 서비스에서 제공되지 않습니다
        </div>
      </div>
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
  min-height: 70%;
  color: #fff;
  padding: 20px;
  width: 100%;
  z-index: 2;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(0, 0, 0, 0.6) 30%,
    rgba(0, 0, 0, 0.95) 70%,
    rgb(0, 0, 0) 100%
  );
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  padding-bottom: 40px;
  padding-left: 40px;
  padding-right: 40px;
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
  margin-bottom: 10px;
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

.additional-info {
  margin-top: 30px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding-top: 30px;
}

.info-row {
  display: flex;
  justify-content: flex-start;
  gap: 60px;
  margin-bottom: 20px;
}

.info-item {
  display: flex;
  align-items: center;
  gap: 10px;
}

.info-label {
  color: #999;
  font-size: 0.9rem;
  min-width: 50px;
}

.info-value {
  color: #fff;
  font-size: 0.9rem;
}

.ott-section {
  margin-top: 15px;
}

.ott-logos {
  display: flex;
  gap: 15px;
  margin-top: 10px;
}

.ott-link {
  transition: transform 0.2s ease;
}

.ott-link:hover {
  transform: scale(1.1);
}

.ott-logo {
  width: 40px;
  height: 40px;
  border-radius: 8px;
  object-fit: cover;
}

.directors-item {
  flex-direction: column;
  align-items: flex-start;
}

.directors-list {
  display: flex;
  gap: 15px;
  margin-top: 5px;
}

.director {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 5px;
}

.director-image {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(255, 255, 255, 0.2);
}

.actors-item {
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
}

.actors-list {
  display: flex;
  gap: 25px;
  margin-top: 15px;
  flex-wrap: wrap;
  margin-bottom: 20px;
}

.actor {
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 8px;
  width: 120px;
}

.actor-image {
  width: 60px;
  height: 60px;
  border-radius: 50%;
  object-fit: cover;
  border: 2px solid rgba(255, 255, 255, 0.2);
}

.actor-info {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

.character-name {
  color: #999;
  font-size: 0.8rem;
}

.no-ott-message {
  color: #999;
  font-size: 0.9rem;
  margin-top: 10px;
  font-style: italic;
}
</style>