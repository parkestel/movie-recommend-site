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
.review-item-container {
  background-color: rgba(250, 250, 255, 0.07);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 15px;
  padding: 25px;
  margin-bottom: 20px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}

.review-item-container:hover {
  transform: translateY(-3px);
  background-color: rgba(250, 250, 255, 0.09);
}

.review-content {
  font-size: 1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 15px;
  display: block;
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 15px 0;
}

#review-nickname {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.7);
}

#my-review-update button {
  margin-left: 8px;
  background-color: rgba(200, 200, 255, 0.15);
  border: 1px solid rgba(200, 200, 255, 0.3);
  border-radius: 8px;
  padding: 6px 12px;
  font-size: 0.85rem;
  color: rgba(255, 255, 255, 0.9);
  cursor: pointer;
  transition: all 0.3s ease;
}

#my-review-update button:hover {
  background-color: rgba(200, 200, 255, 0.25);
}

.review-textarea {
  width: 100%;
  height: 100px;
  padding: 12px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 10px;
  font-size: 0.95rem;
  resize: none;
  background-color: rgba(255, 255, 255, 0.05);
  color: rgba(255, 255, 255, 0.9);
}

.review-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 15px;
  padding-top: 15px;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
}

#liked_count {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.7);
}

.review-like {
  background-color: rgba(200, 200, 255, 0.15);
  border: 1px solid rgba(200, 200, 255, 0.3);
  border-radius: 8px;
  padding: 6px 12px;
  cursor: pointer;
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.9);
  transition: all 0.3s ease;
}

.review-like:hover {
  background-color: rgba(200, 200, 255, 0.25);
}

hr {
  display: none;
}
</style>