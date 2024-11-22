<template>
  <div>
    <p>영화 리뷰, 이 영화를 사용한 공부법 추천 해주세요</p>
    <form @submit.prevent="submitComment()">
      <textarea v-model="content"></textarea>
      <input type="submit" value="작성">
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

</style>