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
  width: 80%;
  max-width: 1200px;
  margin: 0 auto;
  background: linear-gradient(
    to bottom,
    rgba(25, 25, 25, 1) 0%,
    rgba(30, 30, 30, 1) 100%
  );
  padding: 40px 20px;
  border-bottom-left-radius: 2rem;
  border-bottom-right-radius: 2rem;
  position: relative;
  z-index: 1;
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
  background-color: var(--point-peach);
  transform: translateY(-50%);
}

.count-number {
  color: var(--point-peach);
  font-weight: 600;
}

.reviews-list {
  padding: 0 20px;
  padding-bottom: 20px;
}
</style>