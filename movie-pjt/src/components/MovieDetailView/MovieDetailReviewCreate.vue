<template>
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
/* 댓글 작성 컨테이너 */
.comment-container {
  background-color: rgba(250, 250, 255, 0.5);
  border: 1px solid rgba(200, 200, 255, 0.5);
  border-radius: 15px;
  padding: 20px;
  margin-bottom: 20px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

/* 제목 */
.comment-title {
  font-size: 16px;
  font-weight: bold;
  color: rgb(80, 80, 120);
  margin-bottom: 15px;
}

/* 폼 스타일 */
.comment-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

/* 텍스트 영역 */
.comment-textarea {
  width: 100%;
  height: 100px;
  padding: 15px;
  border: 1px solid rgba(200, 200, 255, 0.5);
  border-radius: 10px;
  font-size: 14px;
  resize: none;
  background-color: rgba(255, 255, 255, 0.8);
  color: rgb(80, 80, 80);
  transition: border-color 0.3s;
}

.comment-textarea:focus {
  border-color: rgba(150, 150, 255, 0.8);
  outline: none;
}

/* 제출 버튼 */
.comment-submit-button {
  align-self: flex-end;
  background-color: rgba(200, 200, 255, 0.8);
  border: none;
  border-radius: 10px;
  padding: 10px 20px;
  font-size: 14px;
  color: rgb(60, 60, 60);
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.comment-submit-button:hover {
  background-color: rgba(150, 150, 255, 0.8);
  transform: translateY(-2px);
}
</style>