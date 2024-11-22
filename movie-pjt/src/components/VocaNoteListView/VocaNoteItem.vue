<template>
  <div class="card">
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

const emit = defineEmits(['deleteEvent'])

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
</script>

<style scoped>

</style>