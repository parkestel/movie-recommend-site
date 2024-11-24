<template>
    <div>
        <h1>Movie WishList</h1>
        <div v-if="userProfile.username===store.logedinUsername">
            <select v-model="filter" >
                <option value="all">전체보기</option>
                <option value="withoutNote">단어장 없는 영화</option>
                <option value="withNote">단어장 있는 영화</option>
            </select>
        </div>
        <div v-if="userProfile.username===store.logedinUsername" class="wish-card-container">
            <WishMovieCard  
            v-for="wishMovie in filteredMovies"
            :key="wishMovie.id"
            :wish-movie="wishMovie"
            class="movie-card"/>
        </div>
        <div v-else class="wish-card-container">
            <WishMovieCard  
            v-for="wishMovie in userProfile.wish_movies"
            :key="wishMovie.id"
            :wish-movie="wishMovie"
            class="movie-card"/>
        </div>
    </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue';
import { useMovieStore } from '@/stores/movie'
import WishMovieCard from '@/components/WishMovieListView/WishMovieCard.vue'
import { storeToRefs } from 'pinia'
const store = useMovieStore()
const { userProfile, wishMovies, wishMoviesWithOutNote, vocaNoteList } = storeToRefs(store)
const withNoteMovie = ref(null)

const filter = ref('all')
const filteredMovies = computed(()=>{
    if (filter.value==='withoutNote') {
        return wishMoviesWithOutNote.value
    } else if (filter.value==="withNote") {
        // vocaNoteList에서 영화 id가 일치하는 영화들만 필터링
        withNoteMovie.value = wishMovies.value.filter(movie => 
            vocaNoteList.value.some(note => note.movies[0].id === movie.id)
        )
        return withNoteMovie.value
    } else {
        return wishMovies.value
    }
})
</script>

<style scoped>
.wish-card-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 3rem; /* 카드 간의 간격 */
  margin-top: 1rem;
}
/* 영화 카드 */
.movie-card {
  width: 250px;
  overflow: hidden; /* 부모 요소에서 넘치는 부분 숨김 */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background: transparent;
  box-shadow: none;
  padding: 10px;

}

/* 호버 효과 - 이미지에만 확대 적용 */
.movie-card:hover .card-img {
  transform: scale(1.05); /* 이미지 확대 */
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2); /* 그림자 효과 추가 */
}


  @media (max-width:900px) {
    .wish-card-container {
      grid-template-columns: repeat(3, 1fr); /* 가로 3개 */
    }
  }
  
  @media (max-width: 700px) {
    .wish-card-container {
      grid-template-columns: repeat(1, 1fr); /* 가로1개 */
    }
  }
  
</style>