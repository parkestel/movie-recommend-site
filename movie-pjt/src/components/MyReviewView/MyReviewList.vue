<template>
  <div>
    <MyReviewListItem
    v-for="review in myReviews" 
    :key="review.id" 
    :review="review"
    @delete-event="deleteReview"/>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import MyReviewListItem from '@/components/MyReviewView/MyReviewListItem.vue'
import MyReview from '@/views/ProfileNesting/MyReview.vue';

const props = defineProps({
  myReviews:Array
})
const deleteReview = function (id) {
  console.log(id)
  const targetid = reviews.value.findIndex((review)=>review.id === id)
  reviews.value.splice(targetid, 1)
}
</script>

<style scoped>

</style>