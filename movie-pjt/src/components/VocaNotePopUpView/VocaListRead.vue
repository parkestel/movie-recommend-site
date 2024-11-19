<template>
  <div>
    <input type="checkbox" id="is_memorized">
    <span>{{ voca.word }}</span> : 
    <span>{{ voca.word_mean }}</span><br>
    <p>{{ voca.example }}</p>
    <p>{{ voca.memo }}</p>
  </div>
</template>

<script setup>
defineProps({
  voca:Object
})
</script>

<style scoped>

</style>