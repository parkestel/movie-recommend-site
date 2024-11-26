<template>
  <div class="card best-review-card">
    <div class="card-content-wrapper">
      <p class="card-content">{{ comment.content }}</p>
    </div>
    <div class="card-footer-wrapper">
      <div class="card-info">
        <p class="card-author">{{ comment.users[0].nickname }}</p>
        <span class="like-count">
          <font-awesome-icon :icon="['fas', 'thumbs-up']" id="thumbup"/> {{ comment.liked_user_count }}
        </span>
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
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.1) 0%,
    rgba(255, 103, 103, 0.05) 50%,
    rgba(255, 255, 255, 0.1) 100%
  );
  backdrop-filter: blur(10px);
  -webkit-backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: 2rem;
  padding: 20px;
  margin: 20px 0;
  box-shadow: 
    0 4px 24px rgba(0, 0, 0, 0.2),
    inset 0 0 0 1px rgba(255, 255, 255, 0.1);
  transition: all 0.3s ease;
  width: 300px;
  height: 180px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  position: relative;
  overflow: hidden;
}

.best-review-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(
    90deg,
    transparent,
    rgba(255, 255, 255, 0.2),
    transparent
  );
}

.card-content {
  font-size: 14px;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  text-overflow: ellipsis;
  word-break: break-word;
  position: relative;
  z-index: 1;
}

.card-footer-wrapper {
  margin-top: auto;
}

.card-info {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 8px;
}

.card-author {
  font-size: 14px;
  font-weight: 500;
  color: var(--point-peach);
  margin: 0;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.like-count {
  font-size: 13px;
  font-weight: bold;
  color: var(--point-rose);
  background: rgba(255, 255, 255, 0.1);
  padding: 4px 12px;
  border-radius: 12px;
  backdrop-filter: blur(4px);
  -webkit-backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  align-items: center;
  gap: 5px;
}

.like-count i {
  font-size: 12px;
}

.best-review-card:hover {
  transform: translateY(-5px);
  background: linear-gradient(
    135deg,
    rgba(255, 255, 255, 0.15) 0%,
    rgba(255, 103, 103, 0.1) 50%,
    rgba(255, 255, 255, 0.15) 100%
  );
  box-shadow: 
    0 8px 32px rgba(0, 0, 0, 0.3),
    inset 0 0 0 1px rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.25);
}

.best-review-card:hover .like-count {
  background: rgba(255, 255, 255, 0.15);
  border-color: rgba(255, 255, 255, 0.2);
}
</style>