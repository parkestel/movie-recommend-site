<template>
  <form @submit.prevent="submitVoca(note.id)" class="create-form" v-if="isOwner">
    <div class="input-group">
      <label for="word">word:</label>
      <input type="text" id="word" v-model.trim="word">
    </div>
    <div class="input-group">
      <label for="word_mean">mean:</label>
      <input type="text" id="word_mean" v-model.trim="word_mean">
    </div>
    <div class="input-group">
      <label for="examples">ex:</label>
      <input type="text" id="examples" v-model.trim="examples">
    </div>
    <div class="input-group">
      <label for="memo">memo:</label>
      <input type="text" id="memo" v-model.trim="memo">
    </div>
    <button type="submit" class="submit-btn">작성</button>
  </form>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';
import { storeToRefs } from 'pinia';

const store = useMovieStore()

const word = ref(null)
const word_mean = ref(null)
const examples = ref(null)
const memo = ref(null)
const { userProfile } = storeToRefs(store)

defineProps({
  note:Object,
  isOwner: Boolean  // prop 정의
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
.create-form {
  background: rgba(255, 255, 255, 0.9);
  border-radius: 15px;
  padding: 15px;
  margin: 10px 0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.05);
}

.input-group {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

label {
  min-width: 50px;
  font-size: 0.9rem;
  color: #666;
  font-weight: normal;
}

input, textarea {
  flex: 1;
  padding: 8px 12px;
  border: 1.5px solid rgba(40, 44, 52, 0.2);
  border-radius: 8px;
  font-size: 0.95rem;
  background: rgba(255, 255, 255, 0.95);
  transition: all 0.2s ease;
  height: 24px;
  line-height: 24px;
}

input:focus, textarea:focus {
  outline: none;
  border-color: rgba(255, 103, 103, 0.8);
  box-shadow: 0 0 0 3px rgba(255, 103, 103, 0.15);
  transform: translateY(-1px);
}

textarea {
  resize: none;
  height: 24px !important;
  overflow-y: hidden;
  padding-top: 4px;
}

.submit-btn {
  width: 100%;
  padding: 8px 12px;
  margin-top: 12px;
  background: rgba(255, 103, 103, 0.1);
  color: var(--main-coral);
  border: 1px solid rgba(255, 103, 103, 0.2);
  border-radius: 8px;
  font-size: 0.9rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.submit-btn:hover {
  background: rgba(255, 103, 103, 0.2);
  transform: translateY(-1px);
}
</style>