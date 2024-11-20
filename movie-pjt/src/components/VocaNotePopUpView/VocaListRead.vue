<template>
  <div>
    <input type="checkbox" id="is_memorized">
    <span>{{ voca.word }}</span> : 
    <span>{{ voca.word_mean }}</span>
    <button @click="deleteWord(voca.id)">X</button><br>
    <p>{{ voca.example }}</p>
    <p>{{ voca.memo }}</p>
  </div>
</template>

<script setup>
defineProps({
  voca:Object
})
const emit = defineEmits(['deleteEvent'])
const deleteWord = function (id) {
  emit('deleteEvent', id)
} 
</script>

<style scoped>

</style>