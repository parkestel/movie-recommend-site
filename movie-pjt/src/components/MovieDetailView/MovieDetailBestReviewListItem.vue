<template>
  <div class="card best-review-card">
    <div class="card-content-wrapper">
      <p class="card-content">{{ comment.content }}</p>
    </div>
    <div class="card-footer-wrapper">
      <p class="card-author">작성자 : {{ comment.users[0].nickname }}</p>
      <div class="card-footer">
        <span class="like-count">추천 수: {{ comment.liked_user_count }}</span>
      </div>
    </div>
  </div>
</template>

<script setup>
// 인기 많은 유저 리뷰
defineProps({
  comment:Object
})
</script>

<style scoped>
.best-review-card {
  background-color: rgba(245, 245, 255, 0.95);
  border: 1px solid rgba(180, 180, 255, 0.6);
  border-radius: 2rem;
  padding: 20px;
  margin: 20px 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: transform 0.2s;
  width: 300px;  /* 너비 고정 */
  height: 180px; /* 높이 고정 */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-content-wrapper {
  flex: 1;
  margin-bottom: 10px;
}

.card-content {
  font-size: 14px;
  line-height: 1.6;
  color: rgb(60, 60, 60);
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;  /* 최대 5줄까지 표시 */
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  word-break: break-word;
}

.card-footer-wrapper {
  margin-top: auto;
}

.card-author {
  font-size: 14px;
  font-weight: 500;
  color: rgb(90, 90, 150);
  margin: 0;
  text-align: right;
}

.card-footer {
  display: flex;
  justify-content: flex-end;
  align-items: center;
  margin-top: 5px;
}

.like-count {
  font-size: 13px;
  font-weight: bold;
  color: rgb(120, 120, 180);
}

.best-review-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 14px rgba(0, 0, 0, 0.2);
}
</style>