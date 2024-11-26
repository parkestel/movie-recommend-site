<template>
  <div class="voca-item">
    <div class="voca-header">
      <input type="checkbox" @input="memorizedWord(voca.id)" v-model="voca.is_memorized" v-if="isOwner">
      <span class="word-content" @click="toggleMemoShow">
        <span class="word">{{ voca.word }}</span> : 
        <span>{{ voca.word_mean }}</span>
      </span>
      <button v-if="showDelete" @click="deleteWord(voca.id)" class="action-btn delete-btn">
        <font-awesome-icon :icon="['fas', 'trash-can']"/>
      </button>
      <button v-if="showUpdate" @click="toggleFormShow" class="action-btn edit-btn">
        <font-awesome-icon :icon="['fas', 'pen-to-square']"/>
      </button>
    </div>

    <div v-if="isMemoVisiable" class="memo-content">
      <p v-if="voca.examples"><strong>Ex:</strong> {{ voca.examples }}</p>
      <p v-if="voca.memo"><strong>Memo:</strong> {{ voca.memo }}</p>
    </div>

    <form v-if="isVisiable" @submit.prevent="updateWord(voca.id)" class="edit-form">
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
        <textarea id="memo" v-model.trim="memo"></textarea>
      </div>
      <button type="submit" class="submit-btn">수정</button>
    </form>
  </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
const props = defineProps({
  voca:Object,
  showDelete:Boolean,
  showUpdate:Boolean,
  closeEditForm: Boolean,
  isOwner: Boolean
})
const emit = defineEmits(['deleteEvent', 'updateEvent', 'checkEvent'])
const isVisiable = ref(false)
const isMemoVisiable = ref(false)

const word = ref(props.voca.word)
const word_mean = ref(props.voca.word_mean)
const examples = ref(props.voca.examples)
const memo = ref(props.voca.memo)

watch(() => props.showUpdate, (newValue) => {
  if (!newValue) {
    isVisiable.value = false
  }
})

const deleteWord = function (id) {
  emit('deleteEvent', id)
}

const updateWord = function (id) {
  const payload = {
    word: word.value,
    word_mean: word_mean.value,
    examples: examples.value,
    memo: memo.value
  }
  emit('updateEvent', id, payload)
  isVisiable.value = false
}

const memorizedWord = function (id) {
  emit('checkEvent', id)
}

const toggleFormShow = function () {
  isVisiable.value = !isVisiable.value
}

const toggleMemoShow = function () {
  isMemoVisiable.value = !isMemoVisiable.value
}
</script>

<style scoped>
.voca-item {
  padding: 10px;
  margin: 8px 0;
  border-bottom: 1px solid rgba(40, 44, 52, 0.1);
}

.voca-header {
  display: flex;
  align-items: center;
  gap: 10px;
}

.word-content {
  flex: 1;
  cursor: pointer;
  font-size: 0.95rem;
  color: #282c34;
}

.word-content .word {
  font-weight: 600;
}

.memo-content {
  margin-top: 8px;
  padding: 8px;
  background: rgba(40, 44, 52, 0.03);
  border-radius: 8px;
  font-size: 0.85rem;
  color: #666;
}

.memo-content p {
  margin: 4px 0;
}

/* 체크박스 스타일 */
input[type="checkbox"] {
  width: 16px;
  height: 16px;
  cursor: pointer;
}

/* 수정 폼 스타일 */
.edit-form {
  margin-top: 10px;
  padding: 10px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 8px;
}

.edit-form .input-group {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.edit-form label {
  min-width: 50px;
  font-size: 0.9rem;
  color: #666;
  font-weight: normal;
}

.edit-form input,
.edit-form textarea {
  flex: 1;
  padding: 8px 12px;
  border: 1.5px solid rgba(40, 44, 52, 0.2);
  border-radius: 6px;
  font-size: 0.95rem;
  background: rgba(255, 255, 255, 0.95);
  transition: all 0.2s ease;
  height: 24px;
  line-height: 24px;
}

.edit-form input:focus,
.edit-form textarea:focus {
  outline: none;
  border-color: rgba(255, 103, 103, 0.8);
  box-shadow: 0 0 0 3px rgba(255, 103, 103, 0.15);
  transform: translateY(-1px);
}

.action-btn {
  background: transparent;
  border: none;
  padding: 6px;
  cursor: pointer;
  transition: all 0.3s ease;
  font-size: 0.9rem;
}

.delete-btn {
  color: rgba(255, 103, 103, 0.7);
}

.delete-btn:hover {
  color: rgba(255, 103, 103, 0.9);
  transform: scale(1.1);
}

.edit-btn {
  color: rgba(40, 44, 52, 0.5);
}

.edit-btn:hover {
  color: rgba(40, 44, 52, 0.8);
  transform: scale(1.1);
}

.edit-form textarea {
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