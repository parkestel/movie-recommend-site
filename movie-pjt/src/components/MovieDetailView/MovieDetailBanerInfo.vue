<template>
  <div class="movie-info">
    <div class="basic-info">
      <div class="movie-header">
        <h3 class="movie-title">{{ movieInfo.title }}</h3>
      </div>
      <div class="movie-subinfo">
        <span class="movie-release-date">({{ movieInfo.release_date }})</span>
        <span class="movie-rating">⭐ {{ movieInfo.rank }}</span>
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

    <div class="additional-info">
      <div class="info-row">
        <div class="info-item ott-section">
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

        <div class="info-item actors-item">
          <span class="info-label">CAST</span>
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
  width: 100%;
  color: #fff;
  padding: 20px 0;
  z-index: 2;
  background: linear-gradient(
    to bottom,
    transparent 0%,
    rgba(0, 0, 0, 0.6) 20%,
    rgba(0, 0, 0, 0.95) 50%,
    rgb(0, 0, 0) 100%
  );
  transition: max-height 0.5s ease;
  max-height: 350px;
  overflow: hidden;
}

.basic-info {
  margin-left: 40px;
  margin-right: 40px;
  margin-bottom: 15px;
}

.movie-header {
  margin-bottom: 12px;
}

.movie-title {
  font-size: 2.5rem;
  margin: 0;
  color: #fff;
}

.movie-subinfo {
  display: flex;
  align-items: center;
  gap: 15px;
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 20px;
}

.movie-summary {
  margin: 20px 0;
  font-size: 1.1rem;
  color: #ddd;
  line-height: 1.6;
}

.movie-genres-actions {
  margin-top: 15px;
  margin-bottom: 10px;
}

.additional-info {
  margin-top: 10px;
  padding-top: 20px;
  margin-left: 40px;
  width: calc(100% - 80px);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  opacity: 0;
  transform: translateY(20px);
  transition: all 0.5s ease;
}

.movie-info:hover {
  max-height: 1000px;
}

.movie-info:hover .additional-info {
  opacity: 1;
  transform: translateY(0);
}

.movie-genres-actions {
  display: flex;
  justify-content: space-between;
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

.like-button {
  background-color: rgba(255, 100, 100, 0.2);
  color: #fff;
  border: 1px solid rgba(255, 100, 100, 0.4);
  border-radius: 20px;
  padding: 10px 20px;
  font-size: 0.9rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.like-button:hover {
  background-color: rgba(255, 100, 100, 0.4);
  border-color: rgba(255, 100, 100, 0.6);
}

.like-button.liked {
  background-color: rgba(255, 50, 50, 0.6);
  border-color: rgba(255, 50, 50, 0.6);
}


.info-row {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 15px;
  width: 100%;
}

.info-item {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
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
  margin-bottom: 20px;
}

.ott-logos {
  display: flex;
  gap: 15px;
  justify-content: flex-start;
}

.ott-link {
  transition: transform 0.2s ease;
}

.ott-link:hover {
  transform: scale(1.1);
}

.ott-logo {
  width: 65px;
  height: 65px;
  border-radius: 8px;
  object-fit: cover;
  transition: transform 0.2s ease;
}

.ott-link:hover .ott-logo {
  transform: scale(1.1);
}

.directors-item {
  margin-bottom: 15px;
}

.directors-list {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  justify-content: flex-start;
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
  justify-content: flex-start;
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