<template>
    <div>
        <h1 v-if="note">{{ note.movie }}'s vocanote</h1>
        <VocaCreate/>
        <button @click="toggleDeleteButtons">{{ showDeleteButton ? '취소' : '삭제' }}</button>
        <VocaListRead
        v-for="voca in vocaList"
        :key="voca.id"
        :voca="voca"
        :show-delete="showDeleteButton"
        @delete-event="deleteWord"
        />
    </div>
</template>

<script setup>
import { useMovieStore } from "@/stores/movie";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import VocaCreate from "@/components/VocaNotePopUpView/VocaCreate.vue";
import VocaListRead from "@/components/VocaNotePopUpView/VocaListRead.vue";

const store = useMovieStore()
const route = useRoute()

const note = ref(null)
const vocaList = ref(null)
const showDeleteButton = ref(false)

const deleteWord = function (id) {
    const targetId = vocaList.value.findIndex((voca)=>voca.id===id)
    vocaList.value.splice(targetId, 1)
}

const toggleDeleteButtons = function () {
    showDeleteButton.value = !showDeleteButton.value
}

onMounted(()=>{
    const noteId = route.params.note_id
    console.log(noteId)
    note.value = store.getNote(noteId)
    vocaList.value = store.getVocas(noteId)
    console.log(vocaList)
})
</script>

<style scoped>

</style>