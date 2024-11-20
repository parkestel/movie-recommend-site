<template>
<div>
    <form class="d-flex" role="search">
        <input 
        class="form-control me-2" 
        type="search" 
        placeholder="movie title, actor, director, release year..." 
        aria-label="Search"
        @input="searchGroup($event)">
    </form>
    <!-- filter -->
    <div>
        <MovieCard 
        v-for="movie in searchedMovies" 
        :key="movie" 
        :movie="movie"
        />
    </div>
</div>
</template>

<script setup>
import MovieCard from "@/components/MovieListView/MovieCard.vue"
import { useMovieStore } from "@/stores/movie"
import { onMounted, ref } from "vue";

const store = useMovieStore()
const searchedMovies = ref([])

const searchGroup = function (event) {
    const query = event.target.value.toLowerCase(); // 대소문자 구분 없이 검색
    searchedMovies.value = store.movies.filter(movie => 
        movie.title.toLowerCase().includes(query) || 
        movie.release_date.includes(query) 
    )
}

onMounted(()=>{
    searchedMovies.value = store.movies
})
</script>

<style scoped>
</style>