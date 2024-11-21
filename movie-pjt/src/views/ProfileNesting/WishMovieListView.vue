<template>
    <div>
        <h1>Movie WishList</h1>
        <div v-if="userInfo">
            <WishMovieCard  
            v-for="wishMovie in userInfo.wish_movies"
            :key="wishMovie.id"
            :wish-movie="wishMovie"/>
        </div>
    </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import WishMovieCard from '@/components/WishMovieListView/WishMovieCard.vue';
import { onMounted, ref } from 'vue';

const store = useMovieStore()
const userInfo = ref(null)

onMounted(()=>{
    userInfo.value = store.userProfile
})
</script>

<style scoped>

</style>