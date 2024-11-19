<template>
  <div>
    <h5>Popular User Reviews</h5>
    <MovieDetailBestReviewListItem v-for="comment in bestComments" :key="comment.id" :comment="comment"/>
  </div>
</template>

<script setup>
// user comment를 axios로 받아와서
// 인기 많은 comment - 도움 되는 코멘트 5개를 맨 위에 띄워줌!
// 화살표 버튼을 넘기면서 (캐슬롯?) 코멘트 볼 수 있게 구현
import MovieDetailBestReviewListItem from './MovieDetailBestReviewListItem.vue';
import { ref } from 'vue';

const bestComments = ref([
  {id:1, content:'영어 공부에 도움이 되어요.', liked_user:20, nickname:'user1'},
  {id:2, content:'내용이 재미있고, 좋아요!', liked_user:18, nickname:'user2'},
  {id:3, content:'저는 영화 반복하면서 계속 들었더니 귀가 트였어용', liked_user:11, nickname:'user3'},
])
</script>

<style scoped>

</style>