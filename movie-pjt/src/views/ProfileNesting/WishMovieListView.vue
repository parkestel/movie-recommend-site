<template>
    <div>
        <h1>Movie WishList</h1>
        <div>
            <WishMovieCard  
            v-for="wishMovie in userProfile.wish_movies"
            :key="wishMovie.id"
            :wish-movie="wishMovie"/>
        </div>
    </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import WishMovieCard from '@/components/WishMovieListView/WishMovieCard.vue'
import { storeToRefs } from 'pinia'
const store = useMovieStore()
// storeToRefs로 userProfile을 리액티브한 참조로 가져오기
const { userProfile } = storeToRefs(store)
</script>

<style scoped>

</style>