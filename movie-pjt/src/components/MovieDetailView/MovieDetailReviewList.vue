<template>
  <div>
    <p>작성된 댓글 수: {{ reviews.number_of_count }}</p>
    <MovieDetailReviewListItem
    v-for="review in reviews.comments" 
    :key="review.id" 
    :review="review"
    @delete-event="deleteReview"
    @update-event="updateReview"
    @like-event="likeReview"/>
  </div>
</template>

<script setup>
import MovieDetailReviewListItem from './MovieDetailReviewListItem.vue';

defineProps({
  reviews:Object
})

const deleteReview = function (id) {
  console.log(id)
  const targetid = reviews.value.findIndex((review)=>review.id === id)
  reviews.value.splice(targetid, 1)
}

const updateReview = function (id) {
  console.log(id)
  // update가 발생하면 수정 post 보내는 함수를 사용해서 수정 내용 저장 할 것
}

const likeReview = function (id, user) {
  console.log(id, user)
  // 이벤트 발생 시 좋아요 post 요청하는 내용
}
</script>

<style scoped>

</style>