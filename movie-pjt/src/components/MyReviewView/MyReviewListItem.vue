<template>
  <div class="my-review-item">
    <span>{{ review.content }}</span>
    <p><RouterLink :to="{name:'movie-detail',params:{movieid:review.movies[0].id}}">{{ review.movies[0].title }}</RouterLink></p> 
    <!-- 작성자 === 로그인한 사람 일 때만 삭제 버튼 보이게 -->
    <button @click="deleteReview(review.id)" class="emoji-button"><font-awesome-icon :icon="['fas', 'trash-can']"/> </button>
    <hr>
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
.my-review-item {
    display: flex;
    flex-direction: column; /* 세로로 나열 */
    padding: 15px;
    border: 1px solid #ddd; /* 테두리 */
    border-radius: 8px;
    background-color: #fff; /* 배경색 */
}

.my-review-item span {
    font-size: 16px;
    font-weight: bold; /* 텍스트 강조 */
    margin-bottom: 10px;
}

.my-review-item p {
    font-size: 14px;
    color: #666;
    margin-bottom: 10px;
}

.my-review-item a {
    text-decoration: none;
    color: #3498db; /* 링크 색상 */
    font-weight: bold;
}

.my-review-item a:hover {
    text-decoration: underline;
}

.my-review-item button {
    align-self: flex-end; /* 오른쪽 정렬 */
}

.my-review-item button:hover {
    background-color: #c0392b; /* 호버 색상 */
}
</style>