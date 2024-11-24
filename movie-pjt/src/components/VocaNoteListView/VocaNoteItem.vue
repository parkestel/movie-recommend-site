<template>
  <div class="card">
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

.card {
  position: relative;
  border-radius: 8px;
  padding: 16px;
  margin: 16px 0;
}

.card-header {
  position: absolute;
  top: 8px;
  right: 8px;
}

.delete-button {
  background-color: transparent;
  border: none;
  font-size: 16px;
  color: red;
  cursor: pointer;
  font-weight: bold;
}


.delete-button {
  background-color: transparent;
  border: none;
  font-size: 16px;
  color: rgb(65, 65, 65);
  cursor: pointer;
  font-weight: bold;
  position: absolute;
  top: 8px;
  right: 8px;
}

.locker-icon{
  color: rgb(173, 173, 173);
} 
</style>