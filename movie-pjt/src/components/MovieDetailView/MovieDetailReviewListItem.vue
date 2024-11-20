<template>
  <div>
    <span>{{ review.content }}</span>
    <button>추천</button>
    <p>{{ review.nickname }}</p> 
    <!-- 작성자 === 로그인한 사람 일 때만 삭제 버튼 보이게 -->
    <button @click="deleteReview(review.id)">삭제</button>
    <hr>
  </div>
</template>

<script setup>
defineProps({
  review:Object
})

const emit = defineEmits(['deleteEvent'])
const deleteReview = function (id) {
  emit('deleteEvent', id)
}
</script>

<style scoped>

</style>