<template>
  <div class="card best-review-card">
    <p class="card-content">{{ comment.content }}</p>
    <p class="card-author">작성자 : {{ comment.users[0].nickname }}</p>
    <div class="card-footer">
      <span class="like-count">추천 수: {{ comment.liked_user_count }}</span>
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
/* 베스트 리뷰 카드 스타일 */
.best-review-card {
  background-color: rgba(245, 245, 255, 0.95);
  border: 1px solid rgba(180, 180, 255, 0.6);
  border-radius: 15px;
  padding: 20px;
  margin: 20px 0;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  transition: transform 0.2s;
}

.best-review-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 6px 14px rgba(0, 0, 0, 0.2);
}

/* 카드 제목 */
.card-title {
  font-size: 18px;
  font-weight: bold;
  color: rgb(70, 70, 130);
  margin-bottom: 10px;
  text-align: center;
}

/* 카드 내용 */
.card-content {
  font-size: 14px;
  line-height: 1.6;
  color: rgb(60, 60, 60);
  margin-bottom: 15px;
}

/* 작성자 */
.card-author {
  font-size: 14px;
  font-weight: 500;
  color: rgb(90, 90, 150);
  margin-bottom: 10px;
  text-align: right;
}

/* 추천 수 */
.card-footer {
  display: flex;
  justify-content: flex-end;
  align-items: center;
}

.like-count {
  font-size: 13px;
  font-weight: bold;
  color: rgb(120, 120, 180);
}
</style>