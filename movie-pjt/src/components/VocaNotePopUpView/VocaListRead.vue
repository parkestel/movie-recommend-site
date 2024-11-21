<template>
  <div>
    <input type="checkbox" id="is_memorized">
    <span>{{ voca.word }}</span> : 
    <span>{{ voca.word_mean }}</span>
    <button @click="deleteWord(voca.id)" v-if="showDelete">X</button><br>
    <p>{{ voca.example }}</p>
    <p>{{ voca.memo }}</p>
  </div>
</template>

<script setup>
defineProps({
  voca:Object,
  showDelete:Boolean
})
const emit = defineEmits(['deleteEvent'])

const deleteWord = function (id) {
  emit('deleteEvent', id)
} 
</script>

<style scoped>

</style>