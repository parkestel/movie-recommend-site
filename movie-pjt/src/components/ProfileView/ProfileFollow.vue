<template>
    <div>
        <span>Following : {{ followInfo.followings }}</span>|
        <span>Follower : {{ followInfo.followers }}</span>
        <br>
        <button  v-if="$route.params.username===store.logedinUsername">(un)Follow</button>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()
defineProps({
    followInfo:Object
})
</script>

<style scoped>

</style>