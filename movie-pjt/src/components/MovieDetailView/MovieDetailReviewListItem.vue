<template>
  <div>
    <span>{{ review.content }}</span>
    <button v-if="review.users[0].username!==store.logedinUsername" @click="likeReview(review.id)">추천</button>
    <p>작성자: {{ review.users[0].nickname }}</p>
    <p>추천 수: {{ review.liked_user_count }}</p>
    <!-- 작성자 === 로그인한 사람 일 때만 삭제 버튼 보이게 -->
    <button v-if="review.users[0].username===store.logedinUsername" @click="deleteReview(review.id)">삭제</button>
    <button v-if="review.users[0].username===store.logedinUsername" @click="openUpdateForm">{{ isVisable ? '취소' : '수정' }}</button>
    <form v-if="isVisable" @submit.prevent="updateReview(review.id)">
      <textarea id="update"></textarea>
      <input type="submit">
    </form>
    <hr>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { ref } from 'vue';
import { useRoute } from 'vue-router';

defineProps({
  review:Object
})
const store = useMovieStore()
const route = useRoute()
const movieId = route.params.movieid
const isVisable = ref(false) 

const likeReview = function (id) {
  store.likeCommentsinMovie(id, movieId)
  store.getMovieComments(movieId)
}
const deleteReview = function (id) {
  store.deleteCommentinMovie(id,movieId)
}

const updateReview = function (id,movieId) {
  //store.updateCommentinMovie(id,movieId)
}
const openUpdateForm = function () {
  isVisable.value = !isVisable.value
}

</script>

<style scoped>

</style>