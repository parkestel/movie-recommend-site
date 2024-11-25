<template>
  <div class="reviews-list-container">
    <div class="reviews-header">
      <h5 class="reviews-count">
        <span class="count-number">{{ reviews.number_of_count }}</span>
        개의 리뷰
      </h5>
    </div>
    <div class="reviews-list">
      <MovieDetailReviewListItem
        v-for="review in reviews.comments" 
        :key="review.id" 
        :review="review"
      />
    </div>
  </div>
</template>

<script setup>
import MovieDetailReviewListItem from './MovieDetailReviewListItem.vue';

defineProps({
  reviews:Object
})
</script>

<style scoped>
.reviews-list-container {
  background: linear-gradient(
    to bottom,
    rgb(36, 36, 66) 0%,
    rgb(46, 46, 76) 100%
  );
  padding: 40px 20px;
  margin-top: -1px;
  border-bottom-left-radius: 10px;
  border-bottom-right-radius: 10px;
}

.reviews-header {
  padding: 0 40px;
  margin-bottom: 30px;
}

.reviews-count {
  color: rgba(255, 255, 255, 0.9);
  font-size: 1.2rem;
  font-weight: 500;
  position: relative;
  padding-left: 15px;
  display: flex;
  align-items: center;
  gap: 8px;
}

.reviews-count::before {
  content: '';
  position: absolute;
  left: 0;
  top: 50%;
  width: 4px;
  height: 20px;
  background-color: #ff4444;
  transform: translateY(-50%);
}

.count-number {
  color: #ff4444;
  font-weight: 600;
}

.reviews-list {
  padding: 0 20px;
  padding-bottom: 20px;
}
</style>