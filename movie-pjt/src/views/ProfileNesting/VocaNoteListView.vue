<template>
  <div>
    <h5>My Voca Note Page</h5>
    <VocaNoteItem
    v-for="note in store.vocaNoteList"
    :key="note.id"
    :note="note"
    @delete-event="store.deleteNote"/>
  </div>
</template>

<script setup>
import VocaNoteItem from '@/components/VocaNoteListView/VocaNoteItem.vue'
import { useMovieStore } from "@/stores/movie";

const store = useMovieStore()
</script>

<style scoped>

</style>