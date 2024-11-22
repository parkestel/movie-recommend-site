<template>
    <div v-if="vocaList && !isDeleted">
        <div v-if="userProfile.username===store.logedinUsername">
            <button v-if="vocaList.is_public" @click="togglePublic(vocaList.movies[0].id)">public</button>
            <button v-else @click="togglePublic(vocaList.movies[0].id)">private</button>
        </div>
        <button v-if="userProfile.username===store.logedinUsername" @click="deleteNote(vocaList.movies[0].id)">삭제</button>
        <h1>{{ vocaList.movies[0].title }}'s vocanote</h1>
        <VocaCreate :note="vocaList"/>
        <button @click="toggleDeleteButtons">{{ showDeleteButton ? '취소' : '삭제' }}</button>
        <button @click="toggleUpdateButtons">{{ showUpdateButton ? '취소' : '수정' }}</button>
        <VocaListRead
        v-for="voca in vocaList.vocas"
        :key="voca.id"
        :voca="voca"
        :show-delete="showDeleteButton"
        :show-update="showUpdateButton"
        @delete-event="deleteWord"
        @update-event="updateWord"
        />
    </div>
    <div v-if="isDeleted">
        <p>삭제 되었습니다.</p>
        <button @click="returnToMyNote()">내 Voca Note List 보러가기</button>
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

// const note = ref(null)
const showDeleteButton = ref(false)
const showUpdateButton = ref(false)
const { userProfile, vocaList } = storeToRefs(store)
const noteId = ref(null)

const emit = defineEmits(['deleteEvent', 'toggleEvent'])
const isDeleted = ref(false)

const deleteNote = function (movieId, userId = userProfile.value.id) {
    const result = window.confirm('Really????')
    if (result) {
        store.deleteNote(movieId,userId)
        isDeleted.value=true
    } else {
        return null
    }
}

const returnToMyNote = function(username=userProfile.value.username) {
    if (window.opener) {
        window.opener.location.reload(); // 부모 창 새로고침
    }
    window.close()
    
}

const togglePublic = function (movieId, userId = userProfile.value.id) {
    store.togglePublicVocaNote(movieId,userId)
    if (window.opener) {
        window.opener.location.reload(); // 부모 창 새로고침
    }
    // emit('toggleEvent', movieId, userId)
}

const deleteWord = function (id) {
    store.deleteVoca(id, noteId.value)
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
    noteId.value = route.params.note_id
    store.getVocas(noteId)
    isDeleted.value=false
})

</script>

<style scoped>

</style>