<template>
  <div>
    <form @submit.prevent="submitVoca(note.id)">
      <label for="word">word:</label>
      <input type="text" id="word" v-model.trim="word">
      <br>
      <label for="word_mean">mean:</label>
      <input type="text" id="word_mean" v-model.trim="word_mean">
      <br>
      <label for="examples">examples:</label>
      <input type="text" id="examples" v-model.trim="examples">
      <br>
      <label for="memo">memo:</label>
      <textarea id="memo" v-model.trim="memo"></textarea>
      <br>
      <input type="submit" id="submit" value="update">
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()

const word = ref(null)
const word_mean = ref(null)
const examples = ref(null)
const memo = ref(null)

defineProps({
  note:Object
})

const submitVoca = function (noteId = note.id) {
  //axios data 넘겨주기
  const payload = {
    word: word.value,
    word_mean: word_mean.value,
    examples: examples.value,
    memo: memo.value
  }

  store.createVoca(noteId, payload)
  
  word.value=""
  word_mean.value=""
  examples.value=""
  memo.value=""
}
</script>

<style scoped>

</style>