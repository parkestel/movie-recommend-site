<template>
  <div>
    <form>
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
  </div>
</template>

<script setup>
import { ref } from 'vue';

const word = ref(null)
const mean = ref(null)
const examples = ref(null)
const memo = ref(null)

const submitVoca = function () {
  //axios data 넘겨주기
}
</script>

<style scoped>

</style>