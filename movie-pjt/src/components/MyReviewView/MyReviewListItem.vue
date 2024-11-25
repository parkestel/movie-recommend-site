<template>
  <div class="review-item">
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

</style>