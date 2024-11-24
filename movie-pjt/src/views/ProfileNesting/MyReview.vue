<template>
    <div>
        <h1>내가 쓴 리뷰들</h1>
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

</style>