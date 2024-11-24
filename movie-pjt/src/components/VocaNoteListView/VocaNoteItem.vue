<template>
  <div class="card">
    <div class="card-header">
      <div class="delete-button">
        <button v-if="showDelete" @click="deleteNote(note.movies[0].id)" class="emoji-button" >
          <font-awesome-icon :icon="['fas', 'trash-can']" /> 
        </button>
      </div>
      <div v-if="userProfile.username===store.logedinUsername">
        <button v-if="note.is_public" @click="togglePublic(note.movies[0].id)" class="emoji-button">
          <font-awesome-icon :icon="['fas', 'lock-open']" class="locker-icon"/>
        </button>
        <button v-else @click="togglePublic(note.movies[0].id)" class="emoji-button">
          <font-awesome-icon :icon="['fas', 'lock']" class="locker-icon" />
        </button>
      </div>
    </div>
    <h5>{{ note.movies[0].title }}</h5>
    <button @click="popUp(note.id)" class="btn">show my note</button>
  </div>
</template>

<script setup>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { useMovieStore } from '@/stores/movie';
import { storeToRefs } from 'pinia';
const store = useMovieStore()
const { userProfile } = storeToRefs(store)


defineProps({
  note:Object,
  showDelete:Boolean
})

const emit = defineEmits(['deleteEvent', 'toggleEvent'])

const popUp = function (noteId) {
  window.open(`/note/${noteId}?isPopup=true`, '__blank', 'width=400,height=650')
}

const deleteNote = function (movieId, userId = userProfile.value.id) {
  const result = window.confirm('Really????')
  if (result) {
    emit('deleteEvent', movieId, userId)
  } else {
    return null
  }
}

const togglePublic = function (movieId, userId = userProfile.value.id) {
  emit('toggleEvent', movieId, userId)
}
</script>

<style scoped>

.card-header {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 8px;

  /* 배경색 제거 */
  background-color: transparent;

  /* 테두리 제거 */
  border: none;
  box-shadow: none;
}

.card-header .delete-button,
.card-header .locker-icon {
  /* flexbox로 정렬 */
  display: flex;
  align-items: center;

  /* 동일한 높이와 간격 확보 */
  margin: 0 8px;
}

.card-header .locker-icon {
  color: rgb(173, 173, 173);
}

.delete-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
}

</style>