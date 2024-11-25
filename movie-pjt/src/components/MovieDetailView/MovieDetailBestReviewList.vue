<template>
  <div class="best-reviews-section">
    <div class="best-reviews">
      <h5>Popular User Reviews</h5>
      <swiper
        :modules="modules"
        :slides-per-view="3"
        :space-between="20"
        :navigation="true"
        :pagination="{ clickable: true }"
        :loop="true"
        :autoplay="{
          delay: 3000,
          disableOnInteraction: false,
        }"
        class="review-swiper"
      >
        <swiper-slide v-for="comment in movieBestComments" :key="comment.id">
          <MovieDetailBestReviewListItem :comment="comment"/>
        </swiper-slide>
      </swiper>
    </div>
  </div>
</template>

<script setup>
import { Swiper, SwiperSlide } from 'swiper/vue';
import { Autoplay as SwiperAutoplay, Pagination as SwiperPagination, Navigation as SwiperNavigation } from 'swiper/modules';
import 'swiper/css';
import 'swiper/css/pagination';
import 'swiper/css/navigation';

import MovieDetailBestReviewListItem from './MovieDetailBestReviewListItem.vue';
import { useMovieStore } from '@/stores/movie';
import { storeToRefs } from 'pinia';

const store = useMovieStore()
const {movieBestComments} = storeToRefs(store)

// Swiper 모듈을 변수로 정의
const modules = [SwiperAutoplay, SwiperPagination, SwiperNavigation]
</script>

<style scoped>
.best-reviews-section {
  background: linear-gradient(to bottom, #1a1a2e, #16213e);
  padding: 40px 0;
  margin: 20px 0;
  border-radius: 15px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.2);
}

.best-reviews {
  padding: 20px 0;
  max-width: 1200px;
  margin: 0 auto;
}

h5 {
  font-size: 1.8rem;
  font-weight: bold;
  color: #fff;
  margin-bottom: 20px;
  text-align: center;
}

.review-swiper {
  padding: 20px 40px;
}

:deep(.swiper-button-next),
:deep(.swiper-button-prev) {
  color: #fff;
  background-color: rgba(255, 255, 255, 0.1);
  padding: 25px;
  border-radius: 50%;
  transition: background-color 0.3s ease;
}

:deep(.swiper-button-next:hover),
:deep(.swiper-button-prev:hover) {
  background-color: rgba(255, 255, 255, 0.2);
}

:deep(.swiper-button-next::after),
:deep(.swiper-button-prev::after) {
  font-size: 1.2rem;
}

:deep(.swiper-pagination-bullet) {
  background: #fff;
  opacity: 0.5;
}

:deep(.swiper-pagination-bullet-active) {
  background: #fff;
  opacity: 1;
}
</style>