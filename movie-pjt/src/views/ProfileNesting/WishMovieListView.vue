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
        <div>
            <WishMovieCard  
            v-for="wishMovie in filteredMovies"
            :key="wishMovie.id"
            :wish-movie="wishMovie"/>
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

</style>