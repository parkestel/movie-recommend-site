<template>
  <div class="card">
    <button @click="deleteNote(note.id)">X</button>
    <h5>voca note: {{ note.movie }}</h5>
    <button @click="popUp(note.id)">show my note</button>
  </div>
</template>

<script setup>
defineProps({
  note:Object
})

const emit = defineEmits(['deleteEvent'])

const popUp = function (noteId) {
  window.open(`/note/${noteId}`, '__blank', 'width=400,height=650')
}

const deleteNote = function (noteId) {
  emit('deleteEvent', noteId)
}
</script>

<style scoped>

</style>