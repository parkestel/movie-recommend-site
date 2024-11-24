<template>
  <div class="card">
    <h6>User Best Review</h6>
    <p>{{ comment.content }}</p>
    <p>작성자 : {{ comment.users[0].nickname }}</p>
    <p>{{ comment.liked_user_count }}</p>
  </div>
</template>

<script setup>
// 인기 많은 유저 리뷰
defineProps({
  comment:Object
})
</script>

<style scoped>
.card {
  position: relative; /* 위치를 상대적으로 설정 */
  width: 100%; /* 가로 크기를 부모 컨테이너에 맞춤 */
  height: auto; /* 고정된 높이 */
  overflow: hidden; /* 넘치는 내용 숨기기 */
  border-radius: 1.5rem; /* 둥근 테두리 */
  background: rgba(255, 255, 255, 0.9); /* 약간 투명한 흰색 배경 */
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); /* 부드러운 그림자 */
}
</style>