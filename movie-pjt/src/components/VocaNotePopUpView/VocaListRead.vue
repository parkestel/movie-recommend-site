<template>
  <div>
    <input type="checkbox" id="is_memorized">
    <span>{{ voca.word }}</span> : 
    <span>{{ voca.word_mean }}</span>
    <button @click="deleteWord(voca.id)" v-if="showDelete">X</button>
    <button @click="toggleFormShow" v-if="showUpdate">{{ isVisiable ? '취소' : '수정' }}</button>
    <br>
    <form v-if="isVisiable" @submit.prevent="updateWord(voca.id)">
      <label for="word">word:</label>
      <input type="text" id="word" v-model.trim="word">
      <br>
      <label for="word_mean">mean:</label>
      <input type="text" id="word_mean" v-model.trim="mean">
      <br>
      <label for="examples">examples:</label>
      <input type="text" id="examples" v-model.trim="examples">
      <br>
      <label for="memo">memo:</label>
      <textarea id="memo" v-model.trim="memo"></textarea>
      <br>
      <input type="submit" id="submit" value="update">
    </form>
    <p>{{ voca.example }}</p>
    <p>{{ voca.memo }}</p>
  </div>
</template>

<script setup>
import { ref } from 'vue';
defineProps({
  voca:Object,
  showDelete:Boolean,
  showUpdate:Boolean
})
const emit = defineEmits(['deleteEvent', 'updateEvent'])
const isVisiable = ref(false)

const deleteWord = function (id) {
  emit('deleteEvent', id)
}

const updateWord = function (id) {
  emit('updateEvent', id)
}

const toggleFormShow = function () {
  isVisiable.value = !isVisiable.value
}
</script>

<style scoped>

</style>