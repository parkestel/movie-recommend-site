<template>
  <div>
    <h5>My Voca Note Page</h5>
    <button @click="toggleDeleteButtons">{{ showDeleteButton ? '취소' : '삭제' }}</button>
    <VocaNoteItem
    v-for="note in vocaNoteList"
    :key="note.id"
    :note="note"
    :show-delete="showDeleteButton"
    @delete-event="store.deleteNote"/>
  </div>
</template>

<script setup>
import VocaNoteItem from '@/components/VocaNoteListView/VocaNoteItem.vue'
import { useMovieStore } from "@/stores/movie";
import { storeToRefs } from 'pinia'
import { onMounted, ref } from 'vue';

const store = useMovieStore()
const showDeleteButton = ref(false)
const { userProfile, vocaNoteList } = storeToRefs(store)

const toggleDeleteButtons = function () {
  showDeleteButton.value = !showDeleteButton.value
}

onMounted(()=>{
  store.getVocaNote(userProfile.value.id)
})
</script>

<style scoped>

</style>