<template>
    <div class="container">
        <h2>내가 쓴 리뷰들</h2>
        <div class="review-container">
            <MyReviewList :my-reviews="myReviews" class="review-box"/>
        </div>
    </div>
</template>

<script setup>
import MyReviewList from '@/components/MyReviewView/MyReviewList.vue'
import { useMovieStore } from '@/stores/movie';
import { onMounted } from 'vue';
import { storeToRefs } from 'pinia';

const store = useMovieStore()
const {myReviews} = storeToRefs(store)

onMounted(()=>{
    store.getMyReviews()
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