<template>
  <div>
    <p>작성된 댓글 수: {{ reviews.number_of_count }}</p>
    <MovieDetailReviewListItem
    v-for="review in reviews.comments" 
    :key="review.id" 
    :review="review"/>
  </div>
</template>

<script setup>
import MovieDetailReviewListItem from './MovieDetailReviewListItem.vue';

defineProps({
  reviews:Object
})

</script>

<style scoped>

</style>