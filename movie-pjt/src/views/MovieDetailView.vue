<template>
    <div v-if="movie">
        <MovieDetailBaner :movie-info="movie"/>
        <MovieDetailBestReviewList/>
        <MovieDetailReviewCreate/>
        <MovieDetailReviewList/>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import { onMounted, ref } from 'vue';
import MovieDetailBaner from '@/components/MovieDetailView/MovieDetailBaner.vue';
import MovieDetailBestReviewList from '@/components/MovieDetailView/MovieDetailBestReviewList.vue';
import MovieDetailReviewCreate from '@/components/MovieDetailView/MovieDetailReviewCreate.vue';
import MovieDetailReviewList from '@/components/MovieDetailView/MovieDetailReviewList.vue';

const route = useRoute()
const store = useMovieStore()

const movieId = route.params.movieid
const movie = ref(null)

onMounted(()=>{
    movie.value = store.getMovie(movieId);
})
</script>

<style scoped>

</style>