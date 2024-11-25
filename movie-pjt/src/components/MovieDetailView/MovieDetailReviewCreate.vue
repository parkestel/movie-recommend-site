<template>
  <div class="reviews-background">
    <div class="comment-container">
      <p class="comment-title">영화 리뷰, 이 영화를 사용한 공부법 추천 해주세요</p>
      <form @submit.prevent="submitComment()" class="comment-form">
        <textarea 
          v-model="content" 
          class="comment-textarea" 
          placeholder="댓글을 입력하세요..."
        ></textarea>
        <input type="submit" value="작성" class="comment-submit-button">
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
const emit = defineEmits(['commentCreateEvent'])
const content = ref("")

const submitComment = function () {
  const payload = {
    content:content.value
  }
  emit('commentCreateEvent', payload)
  content.value=""
}
</script>

<style scoped>
.reviews-background {
  background: linear-gradient(
    to bottom,
    rgb(26, 26, 46) 0%,
    rgb(36, 36, 66) 100%
  );
  padding: 40px 20px;
  margin-top: -1px;
}

.comment-container {
  background-color: rgba(250, 250, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  padding: 25px;
  margin: 0 20px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
}

.comment-title {
  font-size: 1.1rem;
  font-weight: 500;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 20px;
}

.comment-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.comment-textarea {
  width: 100%;
  height: 120px;
  padding: 15px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  font-size: 0.95rem;
  resize: none;
  background-color: rgba(255, 255, 255, 0.05);
  color: rgba(255, 255, 255, 0.9);
  transition: all 0.3s ease;
}

.comment-textarea:focus {
  border-color: rgba(200, 200, 255, 0.4);
  background-color: rgba(255, 255, 255, 0.08);
  outline: none;
}

.comment-submit-button {
  align-self: flex-end;
  background-color: rgba(200, 200, 255, 0.15);
  border: 1px solid rgba(200, 200, 255, 0.3);
  border-radius: 10px;
  padding: 10px 25px;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.9);
  cursor: pointer;
  transition: all 0.3s ease;
}

.comment-submit-button:hover {
  background-color: rgba(200, 200, 255, 0.25);
  transform: translateY(-2px);
}
</style>