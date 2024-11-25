<template>
  <div class="container">
    <h2>My Voca Note Page</h2>
    <div class="select-wrapper" v-if="store.logedinUsername===userProfile.username">
      <span>{{ showDeleteButton ? '취소' : '삭제' }}</span>
      <button id="toggle-button" 
              class="toggle-btn" 
              :class="{ active: showDeleteButton }" 
              @click="toggleDeleteButtons">
        <span class="toggle-circle"></span>
      </button>
    </div>
    <br>
    <form v-if="store.logedinUsername===userProfile.username">
      <select id="movieForVocaNote" @change="createNewNote($event.target.value)">
        <option selected>단어장 만들 영화를 선택하세요</option>
        <option v-for="movie in wishMoviesWithOutNote" :key="movie.id" :value="movie.id">{{ movie.title }}</option>
      </select>
    </form>
    <div class="note-card-container">
      <VocaNoteItem
      v-for="note in vocaNoteList"
      :key="note.id"
      :note="note"
      :show-delete="showDeleteButton"
      @delete-event="store.deleteNote"
      @toggle-event="store.togglePublicVocaNote"
      class="note-card"/>
    </div>
  </div>
</template>

<script setup>
import VocaNoteItem from '@/components/VocaNoteListView/VocaNoteItem.vue'
import { useMovieStore } from "@/stores/movie";
import { storeToRefs } from 'pinia'
import { onMounted, ref } from 'vue';

const store = useMovieStore()
const showDeleteButton = ref(false)
const showSelectMovie = ref(false)
const { userProfile, vocaNoteList, wishMoviesWithOutNote } = storeToRefs(store)

const toggleDeleteButtons = function () {
  showDeleteButton.value = !showDeleteButton.value
}

const togglecreateNewNote = function () {
  showSelectMovie.value = !showSelectMovie.value
}
const createNewNote = function (movieId, userId = userProfile.value.id) {
  store.createVocaNote(movieId,userId)
  showSelectMovie.value = !showSelectMovie.value
}

onMounted(()=>{
  store.getVocaNote(userProfile.value.id)
  store.getWishMovieWithOutNote()
})
</script>

<style scoped>
.container {
    max-width: 100%;
    margin: 0 auto;
    padding: 20px;
    background-color: #ffffff83;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    text-align: center;
    position: relative;
  }

.select-wrapper {
  position: absolute;
  top: 16px;
  right: 16px;
  display: flex;
  align-items: center;
  gap: 8px; /* 버튼과 텍스트 간격 */
}

.select-wrapper span {
  font-size: 12px;
  font-weight: bold;
  color: #6d6d6d;
}

.note-card-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1rem; /* 카드 간의 간격 */
  margin-top: 1rem;
}

.note-card {
  width: 100%;
  overflow: hidden; /* 부모 요소에서 넘치는 부분 숨김 */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background: #fff;
  border: 1px solid #ddd;
  box-shadow: none;
  padding: 10px;
}

@media (max-width: 600px) {
  .note-card-container {
    grid-template-columns: 1fr; /* 한 줄로 배치 */
  }
}

#toggle-button {
  position: relative;
}

#toggle-button .toggle-circle {
  position: absolute;
  transition: transform 0.3s ease;
}

form {
  margin-top: 60px;
  display: flex;
  justify-content: center;
}

form select {
  width: 100%;
  max-width: 400px;
  padding: 8px 12px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0px 2px 4px rgba(0, 0, 0, 0.1);
  transition: border-color 0.3s ease;
}

form select:focus {
  border-color: #007bff;
  outline: none;
}

</style>