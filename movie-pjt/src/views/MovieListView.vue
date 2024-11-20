<template>
<div>
    <form class="d-flex" role="search">
        <input 
        class="form-control me-2" 
        type="search" 
        placeholder="movie title, actor, director, release year..." 
        aria-label="Search"
        v-model="searchQuery"
        @input="updateFilter($event, 'search')">
    </form>
    <!-- filter -->
    <button  
    v-for="genre in genresList" 
    :key="genre.id"
    :class="{ active: selectedGenres.includes(genre) }"
    @click="updateFilter($event, 'genre', genre)"
    >{{ genre.name }}</button>
    <div>
        <MovieCard 
        v-for="movie in filteredMovies" 
        :key="movie.id" 
        :movie="movie"
        />
        <p v-if="!filteredMovies">영화가 없습니다.</p>
    </div>
</div>
</template>

<script setup>
import MovieCard from "@/components/MovieListView/MovieCard.vue"
import { useMovieStore } from "@/stores/movie"
import { onMounted, ref, watch } from "vue";

const store = useMovieStore()

const searchQuery = ref(""); // 검색어 상태
const genresList = store.genres // 장르 목록
const selectedGenres = ref([]) // 선택된 장르 목록
const filteredMovies = ref(null); // 필터링된 영화 목록

const updateFilter = function(event, type='search', genre=null){
    if (type === 'search') {
        searchQuery.value = event.target.value.toLowerCase()
    } else if (type === 'genre') {
        if (genre) {
            if (selectedGenres.value.includes(genre)) {
                selectedGenres.value = selectedGenres.value.filter(g => g.id !== genre.id) // 선택 해제
            } else {
                selectedGenres.value.push(genre) // 선택 추가
            }
        }
    }
    applyFilters()
}

// 필터링 로직
const applyFilters = () => {
    filteredMovies.value = store.movies.filter((movie) => {
    // 검색 조건
        const matchesSearch =
        //영화 제목, 배우, 감독 이름, 배우 이름, 나라, 제작사, 개봉 연도 검색 가능
        movie.title?.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        movie.director?.some(director => director.name.toLowerCase().includes(searchQuery.value.toLowerCase())) ||
        movie.stars?.some(star => star.name.toLowerCase().includes(searchQuery.value.toLowerCase()))||
        movie.production?.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        movie.country?.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        movie.release_date?.includes(searchQuery.value);

        // 장르 필터 조건 (모든 선택된 장르 중 하나라도 존재하면 true)
        const matchesGenres =
        selectedGenres.value.length === 0 || // 선택된 장르가 없으면 true
        selectedGenres.value.every((selectedGenre) =>
            movie.genres?.some((genre) => genre.name === selectedGenre.name)
        );

        return matchesSearch && matchesGenres;
    });
};


onMounted(()=>{
    filteredMovies.value = store.movies
    console.log(filteredMovies.value[1])
})
</script>

<style scoped>
button.active {
  background-color: blue; /* 배경색을 파란색으로 변경 */
  color: white; /* 글자색을 흰색으로 변경 */
  font-weight: bold; /* 글자 강조 */
}
</style>