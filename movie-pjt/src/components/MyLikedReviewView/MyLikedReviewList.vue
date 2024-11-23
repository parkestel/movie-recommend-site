<template>
    <div>
      <MyLikedReviewListItem
      v-for="review in likedReviews" 
      :key="review.id" 
      :review="review"
      />
    </div>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import MyLikedReviewListItem from '@/components/MyLikedReviewView/MyLikedReviewListItem.vue';
  
  const props = defineProps({
    likedReviews:Array
  })
  </script>
  
  <style scoped>
  
  </style>