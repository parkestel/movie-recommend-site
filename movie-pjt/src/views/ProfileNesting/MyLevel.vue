<template>
    <div v-if="userInfo">
        <h4>My Study Level</h4>
        <p>ex point : {{ userInfo.experience }}</p>
        <p>level : {{ userInfo.achievement_level }}</p>
        <p>Now studying : {{ userInfo.study_level }}</p>
    </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { onMounted, ref } from 'vue';
const store = useMovieStore()
const userInfo = ref(null)

onMounted(()=>{
    userInfo.value = store.userProfile
})
</script>

<style scoped>

</style>