<template>
    <div class="movie-banner">
        <h4>오늘 이런 영화 어떠세요?</h4>
        <MovieRecommendBanerPosterCard
        v-for="movie in randomMovies"
        :key="movie.id"
        :movie="movie"
        />
    </div>
</template>

<script setup>
import MovieRecommendBanerPosterCard from './MovieRecommendBanerPosterCard.vue';
const props = defineProps({
    randomMovies:Array
})
</script>

<style scoped>
.movie-banner {
    display: flex; /* 가로로 나열 */
    gap: 16px; /* 카드 간격 조정 */
    align-items: center; /* 세로 정렬 */
    overflow-x: auto; /* 카드가 많을 경우 스크롤 가능하게 */
    padding: 10px;
}

.movie-banner h4 {
    flex-shrink: 0; /* 제목이 줄어들지 않도록 고정 */
    margin-right: 16px; /* 제목과 카드 사이 간격 */
}

</style>