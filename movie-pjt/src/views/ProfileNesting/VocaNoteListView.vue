<template>
  <div>
    <h5>My Voca Note Page</h5>
    <button @click="toggleDeleteButtons">{{ showDeleteButton ? '취소' : '삭제' }}</button>
    <VocaNoteItem
    v-for="note in store.vocaNoteList"
    :key="note.id"
    :note="note"
    :show-delete="showDeleteButton"
    @delete-event="store.deleteNote"/>
  </div>
</template>

<script setup>
import VocaNoteItem from '@/components/VocaNoteListView/VocaNoteItem.vue'
import { useMovieStore } from "@/stores/movie";
import { ref } from 'vue';

const store = useMovieStore()
const showDeleteButton = ref(false)

const toggleDeleteButtons = function () {
  showDeleteButton.value = !showDeleteButton.value
}
</script>

<style scoped>

</style>