<template>
    <div>
        <h1 v-if="note">{{ note.movie }}'s vocanote</h1>
    </div>
</template>

<script setup>
import { useMovieStore } from "@/stores/movie";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";

const store = useMovieStore()
const route = useRoute()

const note = ref(null)

onMounted(()=>{
    const noteId = route.params.note_id
    console.log(noteId)
    note.value = store.getNote(noteId)
})
</script>

<style scoped>

</style>