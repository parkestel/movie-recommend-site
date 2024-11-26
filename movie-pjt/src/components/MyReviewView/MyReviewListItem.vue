<template>
  <div class="review-item">
    <span>{{ review.content }}</span>
    <p><RouterLink :to="{name:'movie-detail',params:{movieid:review.movies[0].id}}">{{ review.movies[0].title }}</RouterLink></p> 
    <hr>
    <!-- 작성자 === 로그인한 사람 일 때만 삭제 버튼 보이게 -->
    <button @click="deleteReview(review.id)" class="emoji-button"><font-awesome-icon :icon="['fas', 'trash-can']"/> </button>
  </div>
</template>

<script setup>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()

defineProps({
  review:Object
})

const deleteReview = function (id) {
  store.deleteCommentinMyPage(id)
}
</script>

<style scoped>
.emoji-button {
  background: transparent;
  border: none;
  padding: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.9rem;
  color: rgba(255, 103, 103, 0.7);  /* 코랄 색상 */
}

.emoji-button:hover {
  color: rgba(255, 103, 103, 0.9);  /* hover 시 더 진한 코랄 색상 */
  transform: scale(1.1);  /* hover 시 살짝 커지는 효과 */
}
</style>