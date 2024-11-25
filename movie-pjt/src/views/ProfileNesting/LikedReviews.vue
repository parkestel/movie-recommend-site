<template>
  <div class="container">
    <h2>좋아요한 리뷰 목록</h2>
    <div class="review-container">
      <MyLikedReviewList :liked-reviews="myLikedReviews" class="review-box"/>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { storeToRefs } from 'pinia';
import MyLikedReviewList from '@/components/MyLikedReviewView/MyLikedReviewList.vue';
import { onMounted } from 'vue';

const store = useMovieStore()
const { myLikedReviews } = storeToRefs(store)

onMounted(()=>{
  store.getLikedReviewInMyPage()
})
</script>

<style scoped>
.container {
    max-width: 100%;
    margin: 0 auto;
    padding: 20px;
    background-color: #ffffff83;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    text-align: center;
  }
</style>