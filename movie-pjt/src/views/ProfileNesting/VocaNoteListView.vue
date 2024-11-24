<template>
  <div>
    <h5>My Voca Note Page</h5>
    <button @click="togglecreateNewNote" v-if="store.logedinUsername===userProfile.username">
      {{ showSelectMovie ? '취소' : '단어장 생성' }}
    </button>
    <button @click="toggleDeleteButtons" v-if="store.logedinUsername===userProfile.username">
      {{ showDeleteButton ? '취소' : '삭제' }}
    </button>
    <br>
    <form>
      <select id="movieForVocaNote" v-if="showSelectMovie" @change="createNewNote($event.target.value)">
        <option selected>--영화를 선택하세요--</option>
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
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
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
.note-card-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 3rem; /* 카드 간의 간격 */
  margin-top: 1rem;
}

.note-card {
  width: 250px;
  overflow: hidden; /* 부모 요소에서 넘치는 부분 숨김 */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background: transparent;
  box-shadow: none;
  padding: 10px;
}

</style>