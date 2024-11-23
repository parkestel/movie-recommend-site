<template>
  <div>
    <h1>좋아요한 리뷰 목록</h1>
    <MyLikedReviewList :liked-reviews="myLikedReviews"/>
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

</style>