<template>
  <div class="card">
    <h6>User Review</h6>
    <p>{{ comment.content }}</p>
    <p>{{ comment.nickname }}</p>
    <p>이 리뷰를 좋아요한 유저: {{ comment.liked_user }}</p>
  </div>
</template>

<script setup>
// 인기 많은 유저 리뷰
defineProps({
  comment:Object
})
</script>

<style scoped>

</style>