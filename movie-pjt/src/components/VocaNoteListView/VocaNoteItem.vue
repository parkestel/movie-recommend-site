<template>
  <div class="card">
    <div v-if="userProfile.username===store.logedinUsername">
      <button v-if="note.is_public" @click="togglePublic(note.movies)">public</button>
      <button v-else @click="togglePublic(note.movies)">private</button>
    </div>
    <button v-if="showDelete" @click="deleteNote(note.movies)">X</button>
    <h5>{{ note.movies }}</h5>
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
  window.open(`/note/${noteId}`, '__blank', 'width=400,height=650')
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