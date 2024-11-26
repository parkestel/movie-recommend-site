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
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 2rem;
  padding: 20px;
  margin: 20px 0;
  box-shadow: 
    0 4px 12px rgba(0, 0, 0, 0.1),
    inset 0 0 0 1px rgba(255, 255, 255, 0.1);
  transition: all 0.2s ease;
  width: 300px;
  height: 180px;
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
  color: rgba(255, 255, 255, 0.9);
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
  color: var(--point-peach);
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
  color: var(--point-rose);
}

.best-review-card:hover {
  transform: translateY(-5px);
  background: rgba(255, 255, 255, 0.15);
  box-shadow: 
    0 8px 16px rgba(0, 0, 0, 0.2),
    inset 0 0 0 1px rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.3);
}
</style>