<template>
    <div class="banner-container">
      <h5 class="banner-title">Today's Movie for You</h5>
      <Swiper
        :modules="[Navigation, Pagination, Autoplay]"
        :spaceBetween="30"
        :slidesPerView="1"
        :autoplay="{ delay: 3000, disableOnInteraction: false }"
        navigation
        pagination
        loop
      >
        <SwiperSlide v-for="movie in randomMovies" :key="movie.id">
          <MovieRecommendBanerPosterCard :movie="movie" />
        </SwiperSlide>
      </Swiper>
    </div>
  </template>
  
  <script setup>
  import { Swiper, SwiperSlide } from "swiper/vue"; // Swiper 컴포넌트
  import "swiper/swiper-bundle.css"; // Swiper 스타일
  import { Navigation, Pagination, Autoplay } from "swiper/modules"; // Swiper 모듈
  import MovieRecommendBanerPosterCard from "./MovieRecommendBanerPosterCard.vue";
  import { useMovieStore } from "@/stores/movie";
  

  const store= useMovieStore()
  const props = defineProps({
    randomMovies: Array, // 랜덤 영화 배열
  });
  </script>


<style scoped>
/* 배너 전체 컨테이너 */
.banner-container {
  background-color: rgba(0, 0, 0, 0.5); /* 짙은 검정 배경색 */
  border-radius: 1.5rem;
  position: relative;
  margin-top: 20px;
  height: 400px;
  display: flex;
  align-items: center;  /* 수직 중앙 정렬 */
  justify-content: center;  /* 수평 중앙 정렬 */
}

/* 제목 스타일 */
.banner-title {
  position: absolute; /* 절대 위치로 설정하여 배너 오른쪽 상단에 고정 */
  top: 20px; /* 상단에서 10px 정도의 여백 */
  right: 50px; /* 오른쪽에서 10px 정도의 여백 */
  color: #dbdbdb;  /* 색상을 좀 더 밝은 흰색으로 변경 */
  font-size: 24px;
  margin: 0; /* 기본 마진 제거 */
  z-index: 10; /* 다른 콘텐츠보다 위에 표시되도록 설정 */
  font-family: 'NanumSquareRoundEB', sans-serif !important;
  text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5),   /* 주요 그림자 */
               0 0 10px rgba(255, 255, 255, 0.3);  /* 은은한 글로우 효과 */
}

/* Swiper 네비게이션 버튼 스타일 오버라이드 */
:deep(.swiper-button-next),
:deep(.swiper-button-prev) {
  color: #a8a8a8 !important; /* 버튼 색상 */
  font-size: 30px; /* 버튼 크기 */
}

:deep(.swiper-button-next:hover),
:deep(.swiper-button-prev:hover) {
  color: #ffffff !important; /* 버튼 호버 시 색상 변경 */
}

/* 페이지네이션 버튼 스타일 */
:deep(.swiper-pagination-bullet) {
  background-color: rgb(172, 172, 172) !important; /* 페이지네이션 버튼 색상 */
}

:deep(.swiper-pagination-bullet-active) {
  background-color: #ffffff !important; /* 활성화된 페이지네이션 색상 */
}
</style>