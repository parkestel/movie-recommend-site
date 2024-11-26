<template>
<div>
    <MovieRecommendBaner :random-movies="todayRandomMovie"/>
    <!-- filter -->
    <div class="mt-3">
    <div class="d-flex justify-content-center align-items-center mt-2">
        <button @click="handelClearFilters" class="btn custom-btn">Clear</button>
        <button @click="toggleGenreFilter()" class="btn custom-btn">Genres</button>
        <button @click="toggleOttFilter()" class="btn custom-btn">Otts</button>
        <button @click="toggleLevelFilter()" class="btn custom-btn">Level</button>
    </div>
    <div>
        <div v-if="genreFilter" class="d-flex flex-wrap justify-content-center align-items-center mt-2">
            <button  
                v-for="genre in genresList" 
                :key="genre.id"
                :class="{ 'filter-btn-active' : selectedGenres.includes(genre), 'filter-btn-inactive': !selectedGenres.includes(genre) }"
                class="custom-filter-btn"
                @click="updateFilter($event, 'genre', genre)"
            >{{ genre.name }}</button>
        </div>
        <div v-if="ottFilter" class="d-flex flex-wrap justify-content-center align-items-center mt-2">
            <button  
                v-for="ott in ottList" 
                :key="ott.id"
                :class="{ 'filter-btn-active' : selectedOtts.includes(ott), 'filter-btn-inactive': !selectedOtts.includes(ott) }"
                class="custom-filter-btn"
                @click="updateFilter($event, 'ott', ott)"
            >{{ ott.name }}</button>
        </div>
        <div v-if="levelFilter" class="d-flex justify-content-center align-items-center mt-2">
            <button  
                v-for="level in levelList" 
                :key="level.id"
                :class="{ 'filter-btn-active' : selectedLevel.includes(level), 'filter-btn-inactive': !selectedLevel.includes(level) }"
                class="custom-filter-btn"
                @click="updateFilter($event, 'level', level)"
            >{{ level }}</button>
        </div>
    </div>
    <div class="d-flex justify-content-center mt-3">
        <form class="d-flex custom-search-form" style="width: 800px;" role="search">
            <input 
                class="form-control custom-search-input" 
                type="search" 
                placeholder="movie title, actor, director, release year..." 
                aria-label="Search"
                v-model="searchQuery"
                @input="updateFilter($event, 'search')"
            >
        </form>
        <select id="sorting" class="form-select custom-select-box" style="width: 200px;" v-model="selectedSortOption">
            <option value="" selected disabled>정렬 기준</option>
            <option value="평점 높은 순"> 평점 높은 순 </option>
            <option value="평점 낮은 순"> 평점 낮은 순 </option>
            <option value="알파벳 오름차순 (A~Z)">알파벳 오름차순 (A~Z)</option>
            <option value="알파벳 내림차순 (Z~A)">알파벳 내림차순 (Z~A)</option>
            <option value="제목 한글 오름차순 (ㄱ~ㅎ)">제목 한글 오름차순 (ㄱ~ㅎ)</option>
            <option value="제목 한글 내림차순 (ㅎ~ㄱ)">제목 한글 내림차순 (ㅎ~ㄱ)</option>
            <option value="개봉 날짜 오름차순 (과거순)">개봉 날짜 오름차순 (과거순)</option>
            <option value="개봉 날짜 내림차순 (최신순)">개봉 날짜 내림차순 (최신순)</option>
        </select>
    </div>
</div>

    <div>
        <div v-if="store.isLoading" class="d-flex justify-content-center mt-5">
            <div class="spinner-border" role="status">
            <span class="visually-hidden">Loading...</span>
        </div>
        <span>Loading</span>
        </div>
        <div v-else-if="sortedMovies && !store.isLoading" class="card-container">
            <MovieCard 
            v-for="movie in sortedMovies" 
            :key="movie.id" 
            :movie="movie"
            class="movie-card"
            />
        </div>
    </div>
</div>
</template>

<script setup>
import MovieCard from "@/components/MovieListView/MovieCard.vue"
import MovieRecommendBaner from "@/components/MovieListView/MovieRecommendBaner.vue";
import { useMovieStore } from "@/stores/movie"
import { onMounted, ref, watch, computed } from "vue";
import { storeToRefs } from "pinia";

const store = useMovieStore()

const searchQuery = ref(""); // 검색어 상태
const selectedGenres = ref([]) // 선택된 장르 목록
const selectedOtts = ref([]) //선택된 ott
const selectedLevel = ref([]) //선택된 난이도

const selectedSortOption = ref('') // 정렬 디폴트

const { movies, genres, otts, difficulties, todayRandomMovie } = storeToRefs(store)
const filteredMovies = ref([])
const genresList = ref([])
const ottList = ref([])
const levelList = ref(null)

const genreFilter = ref(false)
const ottFilter = ref(false)
const levelFilter = ref(false)


const toggleGenreFilter = function () {
    genreFilter.value = !genreFilter.value
    ottFilter.value=false
    levelFilter.value=false
}

const toggleOttFilter = function () {
    ottFilter.value = !ottFilter.value
    genreFilter.value=false
    levelFilter.value=false
}

const toggleLevelFilter = function () {
    levelFilter.value = !levelFilter.value
    genreFilter.value=false
    ottFilter.value=false
}

const clearAllFilters = function () {
    selectedGenres.value = []
    selectedLevel.value = []
    selectedOtts.value = []
    genreFilter.value=false
    levelFilter.value=false
    ottFilter.value=false
    selectedSortOption.value=''
    searchQuery.value=''
    applyFilters()
}

const handelClearFilters = function (event) {
    clearAllFilters()
    event.target.blur()
}

// 정렬된 영화 목록 계산 속성
const sortedMovies = computed(() => {
  const moviesToSort = filteredMovies.value; // 필터된 영화 목록 사용
    switch (selectedSortOption.value) {
        case '알파벳 오름차순 (A~Z)':
        return [...moviesToSort].sort((a, b) => a.title.localeCompare(b.title));
        case '알파벳 내림차순 (Z~A)':
        return [...moviesToSort].sort((a, b) => b.title.localeCompare(a.title));
        case '제목 한글 오름차순 (ㄱ~ㅎ)':
        return [...moviesToSort].sort((a, b) => a.title_kr.localeCompare(b.title_kr));
        case '제목 한글 내림차순 (ㅎ~ㄱ)':
        return [...moviesToSort].sort((a, b) => b.title_kr.localeCompare(a.title_kr));
        case '개봉 날짜 오름차순 (과거순)':
        return [...moviesToSort].sort((a, b) => new Date(a.release_date) - new Date(b.release_date));
        case '개봉 날짜 내림차순 (최신순)':
        return [...moviesToSort].sort((a, b) => new Date(b.release_date) - new Date(a.release_date));
        case '평점 높은 순':
        return [...moviesToSort].sort((a, b) => b.rank - a.rank);
        case '평점 낮은 순':
        return [...moviesToSort].sort((a, b) => a.rank - b.rank);
        default:
        return moviesToSort;
    }
});

const updateFilter = function(event, type='search', target=null){
    if (type === 'search') {
        searchQuery.value = event.target.value.toLowerCase()
    } else if (type === 'genre') {
        const index = selectedGenres.value.indexOf(target)
        if (target) {
            if (index===-1) {
                selectedGenres.value.push(target) // 선택 추가
            } else {
                selectedGenres.value.splice(index,1) // 선택 해제
            }
        }
    } else if (type === 'ott') {
        const index = selectedOtts.value.indexOf(target)
        if (target) {
            if (index===-1) {
                selectedOtts.value.push(target) // 선택 추가
            } else {
                selectedOtts.value.splice(index,1) // 선택 해제
            }
        }
    } else if (type === 'level') {
        const index = selectedLevel.value.indexOf(target)
        if (target) {
            if (index===-1) {
                selectedLevel.value.push(target) // 선택 추가
            } else {
                selectedLevel.value.splice(index,1) // 선택 해제
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
        movie.stars?.some(star => star.name_kr.toLowerCase().includes(searchQuery.value.toLowerCase()))||
        movie.production?.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        movie.country?.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
        movie.release_date?.includes(searchQuery.value) ||
        movie.title_kr?.includes(searchQuery.value);

        // 장르 필터 조건 (모든 선택된 장르 중 하나라도 존재하면 true)
        const matchesGenres =
        selectedGenres.value.length === 0 || // 선택된 장르가 없으면 true
        selectedGenres.value.every((selectedGenre) =>
            movie.genres?.some((genre) => genre.tmdb_id === selectedGenre.tmdb_id)
        );

        // ott 필터 조건 (모든 선택된 ott 중 하나라도 존재하면 true)
        const matchesOtts =
        selectedOtts.value.length === 0 || // 선택된 ott가 없으면 true
        selectedOtts.value.every((selectedOtt) =>
            movie.otts?.some((ott) => ott.tmdb_id === selectedOtt.tmdb_id)
        );

        // level 필터 조건 (모든 선택된 level 중 하나라도 존재하면 true)
        const matcheslevels =
        selectedLevel.value.length === 0 || // 선택된 level가 없으면 true
        selectedLevel.value.some((level) =>movie.difficulty === level)

        return matchesSearch && matchesGenres && matchesOtts && matcheslevels;
    });
};

watch([movies, genres, otts, difficulties], () => {
    filteredMovies.value = movies.value
    genresList.value = genres.value
    ottList.value = otts.value
    levelList.value = difficulties.value
})

onMounted(()=>{
    store.getMovies()
    store.getGenres()
    store.getOtts()
    store.getRandomMovies()
    store.getMyLevel()
    filteredMovies.value = store.movies
    genresList.value = store.genres 
    ottList.value = store.otts
    levelList.value = store.difficulties
})
</script>

<style scoped>
/* 버튼 스타일 */
.custom-btn {
    margin: 0 5px;
    padding: 8px 16px;
    font-size: 14px;
    border: 1px solid #ccc;
    background-color: #f8f9fa;
    color: #555;
    border-radius: 15px;
    transition: all 0.3s ease;
}

.custom-btn:hover {
    background-color: #e9ecef;
    color: #333;
}

/* 필터 버튼 스타일 */
.custom-filter-btn {
    margin: 5px;
    padding: 8px 12px;
    border-radius: 6px;
    font-size: 14px;
    border: 1px solid #ccc;
    background-color: #f8f9fa;
    color: #555;
    transition: all 0.3s ease;
}

.filter-btn-active {
    background-color: #d2d2d3;
    color: #333;
    border: 1px solid #adb5bd;
}

.filter-btn-inactive {
    background-color: #f8f9fa;
    color: #555;
    border: 1px solid #ccc;
}

.custom-filter-btn:hover {
    background-color: #e9ecef;
    color: #333;
}

/* 검색창 스타일 */
.custom-search-input {
    border-radius: 6px;
    padding: 10px 15px;
    font-size: 14px;
    border: 1px solid #ccc;
    background-color: #f8f9fa;
    color: #333;
}

/* 정렬 선택 상자 스타일 */
.custom-select-box {
    margin-left: 10px;
    border-radius: 6px;
    font-size: 14px;
    padding: 8px 12px;
    border: 1px solid #ccc;
    background-color: #f8f9fa;
    color: #555;
}

.card-container {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  padding: 20px;
  justify-items: center; /* 카드들을 가운데 정렬 */
  margin: 0 auto; /* 컨테이너 자체를 가운데 정렬 */
  max-width: 1200px; /* 최대 너비 설정 */
}

.movie-card {
  width: 100%; /* 카드의 너비를 그리드 셀에 맞춤 */
  max-width: 250px; /* 카드의 최대 너비 설정 */
}
</style>