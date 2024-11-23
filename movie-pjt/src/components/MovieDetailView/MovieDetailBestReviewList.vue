<template>
  <div>
    <h5>Popular User Reviews</h5>
    <MovieDetailBestReviewListItem v-for="comment in movieBestComments" :key="comment.id" :comment="comment"/>
  </div>
</template>

<script setup>
// user comment를 axios로 받아와서
// 인기 많은 comment - 도움 되는 코멘트 5개를 맨 위에 띄워줌!
// 화살표 버튼을 넘기면서 (캐슬롯?) 코멘트 볼 수 있게 구현
import MovieDetailBestReviewListItem from './MovieDetailBestReviewListItem.vue';
import { useMovieStore } from '@/stores/movie';
import { storeToRefs } from 'pinia';

const store = useMovieStore()
const {movieBestComments} = storeToRefs(store)
</script>

<style scoped>

</style>