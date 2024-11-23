<template>
  <div>
    <h1>비밀 번호 수정</h1>
    <form @submit.prevent="changePW">
      <label for="password1">new password</label>
      <input type="password" id="password1" v-model.trim="password1">
      <br>
      <label for="password2">new password confirm</label>
      <input type="password" id="password2" v-model.trim="password2">
      <br>
      <input type="submit" value="submit">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()
const password1 = ref(null)
const password2 = ref(null)

const changePW = function(){
  const payload = {
    new_password1:password1.value,
    new_password2:password2.value,
  }
  store.changePassword(payload)
}
</script>

<style scoped>

</style>