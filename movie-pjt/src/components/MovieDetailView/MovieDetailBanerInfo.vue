<template>
  <div>
    <h3>제목: {{ movieInfo.title }}</h3>
    <p>summary: {{ movieInfo.summary }}</p>
    <p>genre: {{ movieInfo.genre }}</p>
    <p>release_date: {{ movieInfo.release_date }}</p>

  </div>
</template>

<script setup>
defineProps({
  movieInfo:Object
})
</script>

<style scoped>

</style>