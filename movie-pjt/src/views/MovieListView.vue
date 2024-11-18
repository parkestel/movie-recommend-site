<template>
<div>
    <form class="d-flex" role="search">
        <input class="form-control me-2" type="search" placeholder="Search" aria-label="Search">
        <button class="btn btn-outline-success" type="submit">Search</button>
    </form>
    <!-- filter -->
    <div>
        <MovieCard v-for="movie in store.movies" :key="movie" :movie="movie"/>
    </div>
</div>
</template>

<script setup>
import MovieCard from "@/components/MovieCard.vue"
import { useMovieStore } from "@/stores/movie"

const store = useMovieStore()
</script>

<style scoped>

</style>