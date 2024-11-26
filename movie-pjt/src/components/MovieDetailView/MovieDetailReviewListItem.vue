<template>
  <div class="review-item-container">
    <span class="review-content">{{ review.content }}</span>
    <br>
    <div class="review-header">
      <span id="review-nickname" @click="goToUserProfile(review.users[0].username)">작성자: {{ review.users[0].nickname }}</span>
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
        class="review-like"
        :class="{ 'liked': review.liked_users.some(user => user.username === store.logedinUsername) }"
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
import { useRoute, useRouter } from 'vue-router';

const props = defineProps({
  review:Object
})
const store = useMovieStore()
const route = useRoute()
const movieId = route.params.movieid
const isVisable = ref(false) 
const content = ref(props.review.content)
const router = useRouter()
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

const goToUserProfile = function (username) {
  router.push({ name: 'profile', params: { username } })
}
</script>

<style scoped>
.review-item-container {
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: 2rem;
  padding: 25px;
  margin-bottom: 20px;
  backdrop-filter: blur(10px);
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  transition: transform 0.2s ease;
}

.review-item-container:hover {
  transform: translateY(-3px);
  background: rgba(255, 255, 255, 0.08);
}

.review-content {
  font-size: 1rem;
  line-height: 1.6;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 15px;
  display: block;
  border-left: 3px solid var(--point-peach);
  padding-left: 15px;
}

.review-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 15px 0;
}

#review-nickname {
  font-size: 0.9rem;
  color: var(--point-peach);
  opacity: 0.9;
  cursor: pointer;
  transition: all 0.3s ease;
}

#review-nickname:hover {
  text-decoration: underline;
  opacity: 1;
}

#my-review-update button {
  background: transparent;
  border: 1px solid var(--point-peach);
  margin-left: 8px;
  border-radius: 8px;
  padding: 6px 12px;
  font-size: 0.85rem;
  color: var(--point-peach);
  cursor: pointer;
  transition: all 0.3s ease;
}

#my-review-update button:hover {
  background: rgba(255, 103, 103, 0.1);
  transform: translateY(-2px);
  border-color: var(--main-coral);
  color: var(--main-coral);
}

.review-form {
  display: flex;
  flex-direction: column;
  gap: 15px;
  margin-top: 15px;
}

.review-textarea {
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

.review-textarea:focus {
  border-color: rgba(200, 200, 255, 0.4);
  background-color: rgba(255, 255, 255, 0.08);
  outline: none;
}

.review-submit-button {
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

.review-submit-button:hover {
  background-color: rgba(200, 200, 255, 0.25);
  transform: translateY(-2px);
}

.review-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-top: 15px;
  padding-top: 15px;
  border-top: 1px solid rgba(255, 103, 103, 0.2);
}

#liked_count {
  font-size: 0.9rem;
  color: var(--point-peach);
  opacity: 0.9;
  display: flex;
  align-items: center;
  gap: 5px;
}

.review-like {
  background: transparent;
  border: 1px solid var(--point-peach);
  border-radius: 8px;
  padding: 8px 15px;
  cursor: pointer;
  font-size: 0.9rem;
  color: var(--point-peach);
  transition: all 0.3s ease;
}

.review-like:hover {
  background: rgba(255, 103, 103, 0.1);
  transform: translateY(-2px);
  border-color: var(--main-coral);
  color: var(--main-coral);
}

.review-like.liked {
  background: linear-gradient(
    135deg,
    var(--point-peach) 0%,
    var(--main-coral) 100%
  );
  border: none;
  color: rgba(255, 255, 255, 0.95);
  box-shadow: 0 2px 8px rgba(255, 103, 103, 0.2);
}

.review-like.liked:hover {
  opacity: 0.9;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 103, 103, 0.3);
}

hr {
  display: none;
}

.delete-button {
  border-color: rgba(255, 103, 103, 0.5) !important;
  color: rgba(255, 103, 103, 0.7) !important;
}

.delete-button:hover {
  border-color: var(--main-coral) !important;
  color: var(--main-coral) !important;
}
</style>