<template>
  <div>
    <span>{{ review.content }}</span>
    <button>추천</button>
    <p>{{ review.nickname }}</p> 
    <hr>
  </div>
</template>

<script setup>
defineProps({
  review:Object
})
</script>

<style scoped>

</style>