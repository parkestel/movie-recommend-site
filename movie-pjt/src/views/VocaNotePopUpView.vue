<template>
    <div>
        <div v-if="userProfile.username===store.logedinUsername">
            <button v-if="note.is_public" @click="togglePublic(note.movies)">public</button>
            <button v-else @click="togglePublic(note.movies)">private</button>
        </div>
        <button v-if="userProfile.username===store.logedinUsername" @click="deleteNote(note.movies)">삭제</button>
        <h1 v-if="note">{{ note.movie }}'s vocanote</h1>
        <VocaCreate/>
        <button @click="toggleDeleteButtons">{{ showDeleteButton ? '취소' : '삭제' }}</button>
        <button @click="toggleUpdateButtons">{{ showUpdateButton ? '취소' : '수정' }}</button>
        <VocaListRead
        v-for="voca in vocaList"
        :key="voca.id"
        :voca="voca"
        :show-delete="showDeleteButton"
        :show-update="showUpdateButton"
        @delete-event="deleteWord"
        @update-event="updateWord"
        />
    </div>
</template>

<script setup>
import { useMovieStore } from "@/stores/movie";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import VocaCreate from "@/components/VocaNotePopUpView/VocaCreate.vue";
import VocaListRead from "@/components/VocaNotePopUpView/VocaListRead.vue";
import { storeToRefs } from "pinia";

const store = useMovieStore()
const route = useRoute()

const note = ref(null)
const vocaList = ref(null)
const showDeleteButton = ref(false)
const showUpdateButton = ref(false)
const { userProfile } = storeToRefs(store)

const emit = defineEmits(['deleteEvent', 'toggleEvent'])

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

const deleteWord = function (id) {
    const targetId = vocaList.value.findIndex((voca)=>voca.id===id)
    vocaList.value.splice(targetId, 1)
}

const updateWord = function (id) {
    // axios post 
}

const toggleDeleteButtons = function () {
    showDeleteButton.value = !showDeleteButton.value
}

const toggleUpdateButtons = function () {
    showUpdateButton.value = !showUpdateButton.value
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