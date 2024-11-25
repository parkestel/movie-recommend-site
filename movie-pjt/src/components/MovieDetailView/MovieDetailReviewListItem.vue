<template>
  <div class="review-item-container">
    <span class="review-content">{{ review.content }}</span>
    <br>
    <div class="review-header">
      <span id="review-nickname">작성자: {{ review.users[0].nickname }}</span>
      <span id="my-review-update">
        <button 
          v-if="review.users[0].username === store.logedinUsername" 
          @click="deleteReview(review.id, movieId)" 
          class="delete-button"
        >
          삭제
        </button>
        <button 
          v-if="review.users[0].username === store.logedinUsername" 
          @click="openUpdateForm" 
          class="update-button"
        >
          {{ isVisable ? '취소' : '수정' }}
        </button>
      </span>
    </div>
    <form 
      v-if="isVisable" 
      @submit.prevent="updateReview(review.id, movieId)" 
      class="review-form"
    >
      <textarea 
        id="update" 
        v-model.trim="content" 
        class="review-textarea" 
        placeholder="댓글을 입력하세요..."
      ></textarea>
      <input type="submit" value="수정" class="review-submit-button">
    </form>
    <div class="review-footer">
      <span id="liked_count">추천 수: {{ review.liked_user_count }}</span>
      <button 
        v-if="review.users[0].username !== store.logedinUsername" 
        @click="likeReview(review.id, movieId)" 
        class="emoji-button review-like"
      >
        <font-awesome-icon :icon="['far', 'thumbs-up']" id="thumbup"/>
      </button>
    </div>
    <hr>
  </div>
</template>

<script setup>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { useMovieStore } from '@/stores/movie';
import { onMounted, ref } from 'vue';
import { useRoute } from 'vue-router';

const props = defineProps({
  review:Object
})
const store = useMovieStore()
const route = useRoute()
const movieId = route.params.movieid
const isVisable = ref(false) 
const content = ref(props.review.content)

const likeReview = function (id, movieId) {
  store.likeCommentsinMovie(id, movieId)
  store.getMovieComments(movieId)
}
const deleteReview = function (id, movieId) {
  store.deleteCommentinMovie(id,movieId)
}

const updateReview = function (id,movieId) {
  const payload = {
    content: content.value
  }
  store.updateCommentinMovie(id, movieId, payload)
  isVisable.value=false
}
const openUpdateForm = function () {
  isVisable.value = !isVisable.value
}
</script>

<style scoped>
/* 최상위 리뷰 컨테이너 */
.review-item-container {
  background-color: rgba(250, 250, 255, 0.5);
  border: 1px solid rgba(200, 200, 255, 0.5);
  border-radius: 15px;
  padding: 20px;
  margin-bottom: 15px;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease-in-out;
}

.review-container:hover {
  transform: translateY(-5px);
}

/* 리뷰 내용 */
.review-content {
  font-size: 16px;
  line-height: 1.5;
  color: rgb(80, 80, 80);
  margin-bottom: 10px;
}

/* 헤더 */
.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

/* 닉네임 */
#review-nickname {
  font-size: 14px;
  color: rgb(120, 120, 120);
}

/* 삭제 및 수정 버튼 */
#my-review-update button {
  margin-left: 5px;
  background-color: rgba(255, 200, 200, 0.5);
  border: 1px solid rgba(255, 150, 150, 0.8);
  border-radius: 10px;
  padding: 5px 10px;
  font-size: 14px;
  cursor: pointer;
  transition: background-color 0.3s ease-in-out;
}

#my-review-update button:hover {
  background-color: rgba(255, 150, 150, 0.8);
}

/* 폼 스타일 */
.review-form {
  margin-top: 10px;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.review-textarea {
  width: 100%;
  height: 80px;
  padding: 10px;
  border: 1px solid rgba(200, 200, 255, 0.5);
  border-radius: 10px;
  font-size: 14px;
  resize: none;
  background-color: rgba(255, 255, 255, 0.8);
  color: rgb(80, 80, 80);
}

.review-submit-button {
  align-self: flex-end;
  background-color: rgba(200, 200, 255, 0.8);
  border: none;
  border-radius: 10px;
  padding: 8px 16px;
  font-size: 14px;
  color: rgb(60, 60, 60);
  cursor: pointer;
  transition: background-color 0.3s, transform 0.2s;
}

.review-submit-button:hover {
  background-color: rgba(150, 150, 255, 0.8);
  transform: translateY(-2px);
}

/* 푸터 */
.review-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 10px;
}

#liked_count {
  font-size: 14px;
  color: rgb(120, 120, 120);
}

.review-like {
  background-color: rgba(255, 255, 255, 0.8);
  border: 1px solid rgba(200, 200, 255, 0.5);
  border-radius: 10px;
  padding: 5px 10px;
  cursor: pointer;
  font-size: 14px;
  color: rgb(60, 60, 60);
  transition: background-color 0.3s ease-in-out;
}

.review-like:hover {
  background-color: rgba(200, 200, 255, 0.5);
}
</style>