<template>
  <div>
    <span>{{ review.content }}</span>
    <button @click="likeReview(review.id, store.logedinUsername)">추천</button>
    <p>{{ review.nickname }}</p> 
    <!-- 작성자 === 로그인한 사람 일 때만 삭제 버튼 보이게 -->
    <button v-if="review.username===store.logedinUsername" @click="deleteReview(review.id)">삭제</button>
    <button v-if="review.username===store.logedinUsername" @click="openUpdateForm">{{ isVisable ? '취소' : '수정' }}</button>
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

defineProps({
  review:Object
})
const store = useMovieStore()
const isVisable = ref(false) 
const emit = defineEmits(['deleteEvent', 'updateReview', 'likeEvent'])

const likeReview = function (id, user) {
  emit('likeEvent', id, user)
}
const deleteReview = function (id) {
  emit('deleteEvent', id)
}

const openUpdateForm = function () {
  isVisable.value = !isVisable.value
}

const updateReview = function (id) {
  emit('updateReview', id)
}
</script>

<style scoped>

</style>