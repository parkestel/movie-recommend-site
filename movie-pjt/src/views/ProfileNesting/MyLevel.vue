<template>
    <div>
        <h4>My Study Level</h4>
        <p>ex point : {{ expoint }}</p>
        <p>level : {{ level }}</p>
        <p>Now studying : {{ study }}</p>
    </div>
</template>

<script setup>

import { useMovieStore } from '@/stores/movie';
import { ref } from 'vue';
const store = useMovieStore()

const level = ref(store.userProfile.achievement_level)
const expoint = ref(store.userProfile.experience)
const study = ref(store.userProfile.study_level)
</script>

<style scoped>

</style>