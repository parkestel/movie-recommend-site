<template>
    <div>
        <h1>Movie WishList</h1>
        <div v-if="wishMovies">
            <WishMovieCard  
            v-for="wishMovie in wishMovies"
            :key="wishMovie.id"
            :wish-movie="wishMovie"/>
        </div>
    </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { onMounted, ref } from 'vue';
import WishMovieCard from '@/components/WishMovieListView/WishMovieCard.vue';

const store = useMovieStore()
const wishMovies = ref(null)

onMounted(()=>{
    wishMovies.value = store.getWishMovies()
    console.log(wishMovies)
})
</script>

<style scoped>

</style>