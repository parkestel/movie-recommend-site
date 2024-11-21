<template>
    <div>
        <h4>My Study Level</h4>
        <p>ex point : {{ userProfile.experience }}</p>
        <p>level : {{ userProfile.achievement_level }}</p>
        <p>Now studying : {{ userProfile.study_level }}</p>
    </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { onMounted, ref } from 'vue';
import { storeToRefs } from 'pinia';
const store = useMovieStore()
const { userProfile } = storeToRefs(store)
</script>

<style scoped>

</style>