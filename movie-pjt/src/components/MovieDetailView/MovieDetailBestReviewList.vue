<template>
  <div class="best-reviews-section" v-if="movieBestComments.length > 0">
    <div class="best-reviews">
      <h5>Popular User Reviews</h5>
      <swiper
        :modules="modules"
        :slides-per-view="slidesPerView"
        :space-between="20"
        :navigation="movieBestComments.length > 1"
        :pagination="{ clickable: true }"
        :loop="movieBestComments.length > 2"
        :autoplay="movieBestComments.length > 2 ? {
          delay: 3000,
          disableOnInteraction: false,
        } : false"
        class="review-swiper"
      >
        <swiper-slide v-for="comment in movieBestComments" :key="comment.id">
          <MovieDetailBestReviewListItem :comment="comment"/>
        </swiper-slide>
      </swiper>
    </div>
  </div>
  <div v-else class="no-reviews">
    <p>아직 등록된 리뷰가 없습니다.</p>
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
import { computed } from 'vue';

const store = useMovieStore()
const {movieBestComments} = storeToRefs(store)

// Swiper 모듈을 변수로 정의
const modules = [SwiperAutoplay, SwiperPagination, SwiperNavigation]

const slidesPerView = computed(() => {
  const count = movieBestComments.value.length
  if (count === 1) return 1
  if (count === 2) return 2
  return 3
})
</script>

<style scoped>
.best-reviews-section {
  width: 80%;
  max-width: 1200px;
  margin: 0 auto;
  background: rgb(0, 0, 0);
  padding: 40px 20px;
  position: relative;
  box-shadow: none;
  border: none;
}

.best-reviews h5 {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.5rem;
  font-weight: 700;
  margin-bottom: 20px;
  padding-left: 20px;
  position: relative;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.best-reviews h5::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  width: 4px;
  height: 20px;
  background-color: var(--main-coral);
  transform: translateY(-50%);
  border-radius: 2px;
  box-shadow: 0 0 10px rgba(255, 103, 103, 0.3);
}

.no-reviews {
  width: 80%;
  max-width: 1200px;
  margin: 0 auto;
  background: rgb(0, 0, 0);
  padding: 40px;
  text-align: center;
  color: rgba(255, 255, 255, 0.7);
  font-size: 1.2rem;
  position: relative;
}

/* Swiper 스타일 수정 */
:deep(.swiper) {
  padding: 20px 10px;
}

:deep(.swiper-slide) {
  display: flex;
  justify-content: center;
  transition: all 0.3s ease;
}

:deep(.swiper-slide:hover) {
  transform: translateY(-5px);
}

/* 스와이퍼 네비게이션 버튼 스타일링 */
:deep(.swiper-button-next),
:deep(.swiper-button-prev) {
  color: var(--point-peach);
  opacity: 0.7;
  transition: all 0.3s ease;
}

:deep(.swiper-button-next:hover),
:deep(.swiper-button-prev:hover) {
  opacity: 1;
  transform: scale(1.1);
}

/* 페이지네이션 스타일링 */
:deep(.swiper-pagination-bullet) {
  background: var(--point-peach);
  opacity: 0.5;
}

:deep(.swiper-pagination-bullet-active) {
  opacity: 1;
  background: var(--point-peach);
}
</style>