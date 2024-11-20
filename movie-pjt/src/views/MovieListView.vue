<template>
<div>
    <form class="d-flex" role="search">
        <input 
        class="form-control me-2" 
        type="search" 
        placeholder="movie title, actor, director, release year..." 
        aria-label="Search"
        @input="updateFilters($event)">
    </form>
    <!-- filter -->
    <select class="form-select" @change="updateFilters($event, 'genre')">
        <option value="">All Genres</option>
        <option 
            v-for="genre in store.genres" 
            :key="genre.id" 
            :value="genre.name">
            {{ genre.name }}
        </option>
    </select>
    <div>
        <MovieCard 
        v-for="movie in filteredMovies" 
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

const searchQuery = ref(""); // 검색어 상태
const selectedGenre = ref(""); // 선택된 장르 상태
const filteredMovies = ref(null); // 필터링된 영화 목록

// 검색 및 필터 업데이트 함수
const updateFilters = function (event, type = 'search') {
    if (type === 'search') {
        searchQuery.value = event.target.value.toLowerCase();
    } else if (type === 'genre') {
        selectedGenre.value = event.target.value;
    }
    applyFilters(); // 필터링 로직 호출

    // console.log("선택된 장르:", selectedGenre.value);
    // console.log("필터링된 영화:", filteredMovies.value);
};

// 필터링 로직
const applyFilters = function () {
    filteredMovies.value = store.movies.filter(movie => {

        const matchesSearch = 
            movie.title?.toLowerCase().includes(searchQuery.value) || 
            movie.release_date?.includes(searchQuery.value);

        const matchesGenre = 
            selectedGenre.value === "" || 
            movie.genre?.includes(selectedGenre.value)

        return matchesSearch && matchesGenre;
    });
};

onMounted(()=>{
    filteredMovies.value = store.movies
    console.log(filteredMovies.value)
})
</script>

<style scoped>
</style>