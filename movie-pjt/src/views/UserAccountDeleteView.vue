<template>
  <div>
    <h1>정말 삭제 하시겠습니까</h1>
    <p>가지마....</p>
    <button @click="store.SignOut">진짜 계정 삭제 하기</button>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
const store = useMovieStore()
</script>

<style scoped>

</style>