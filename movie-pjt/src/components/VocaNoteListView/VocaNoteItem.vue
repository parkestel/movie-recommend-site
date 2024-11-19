<template>
  <div class="card">
    <h5>voca note: {{ note.movie }}</h5>
    <button @click="popUp(note.id)">show my note</button>
  </div>
</template>

<script setup>
defineProps({
  note:Object
})

const popUp = function (noteId) {
  window.open(`/note/${noteId}`, '__blank', 'width=400,height=650')
}
</script>

<style scoped>

</style>