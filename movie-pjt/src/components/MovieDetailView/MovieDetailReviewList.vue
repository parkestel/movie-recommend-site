<template>
  <div>
    <MovieDetailReviewListItem
    v-for="review in reviews" 
    :key="review.id" 
    :review="review"
    @delete-event="deleteReview"
    @update-event="updateReview"/>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import MovieDetailReviewListItem from './MovieDetailReviewListItem.vue';

const reviews = ref([
  {id:1, content:'영어 공부에 도움이 되어요.', liked_user:20, nickname:'user1'},
  {id:2, content:'내용이 재미있고, 좋아요!', liked_user:18, nickname:'user2'},
  {id:3, content:'저는 영화 반복하면서 계속 들었더니 귀가 트였어용', liked_user:11, nickname:'user3'},
])

const deleteReview = function (id) {
  console.log(id)
  const targetid = reviews.value.findIndex((review)=>review.id === id)
  reviews.value.splice(targetid, 1)
}

const updateReview = function (id) {
  console.log(id)
  // update가 발생하면 수정 post 보내는 함수를 사용해서 수정 내용 저장 할 것
}
</script>

<style scoped>

</style>