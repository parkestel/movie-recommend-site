<template>
    <div>
        <h1 v-if="note">{{ note.movie }}'s vocanote</h1>
    </div>
    <div>
        <VocaCreate/>
    </div>
    <div>
        <VocaListRead
        v-for="voca in vocaList"
        :key="voca.id"
        :voca="voca"
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