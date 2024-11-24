<template>
  <div class="card">
    <div v-if="userProfile.username===store.logedinUsername">
      <button v-if="note.is_public" @click="togglePublic(note.movies[0].id)">public</button>
      <button v-else @click="togglePublic(note.movies[0].id)">private</button>
    </div>
    <button v-if="showDelete" @click="deleteNote(note.movies[0].id)">X</button>
    <h5>{{ note.movies[0].title }}</h5>
    <button @click="popUp(note.id)">show my note</button>
  </div>
</template>

<script setup>
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

</style>