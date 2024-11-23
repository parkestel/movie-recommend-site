<template>
  <div>
    <span>{{ review.content }}</span>
    <button v-if="review.users[0].username!==store.logedinUsername" @click="likeReview(review.id, movieId)">추천</button>
    <p>작성자: {{ review.users[0].nickname }}</p>
    <p>추천 수: {{ review.liked_user_count }}</p>
    <!-- 작성자 === 로그인한 사람 일 때만 삭제 버튼 보이게 -->
    <button v-if="review.users[0].username===store.logedinUsername" @click="deleteReview(review.id,movieId)">삭제</button>
    <button v-if="review.users[0].username===store.logedinUsername" @click="openUpdateForm">{{ isVisable ? '취소' : '수정' }}</button>
    <form v-if="isVisable" @submit.prevent="updateReview(review.id, movieId)">
      <textarea id="update" v-model.trim="content"></textarea>
      <input type="submit">
    </form>
    <hr>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { ref } from 'vue';
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
}
const openUpdateForm = function () {
  isVisable.value = !isVisable.value
}

</script>

<style scoped>

</style>