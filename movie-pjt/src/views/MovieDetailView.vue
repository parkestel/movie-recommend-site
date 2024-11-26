<template>
    <div v-if="isLoading" class="loading-container">
        <div class="loading-spinner">
            <font-awesome-icon :icon="['fas', 'spinner']" spin size="2x" />
            <p>영화 정보를 불러오는 중...</p>
        </div>
    </div>
    <div v-else-if="movie">
        <MovieDetailBaner :movie-info="movie"/>
        <MovieDetailBestReviewList/>
        <MovieDetailReviewCreate @comment-create-event="createComment"/>
        <MovieDetailReviewList :reviews="moviecomments"/>
    </div>
    <div v-else class="error-container">
        <p>영화 정보를 불러올 수 없습니다.</p>
    </div>
</template>

<script setup>
import { useRoute } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import { onMounted, ref } from 'vue';
import { storeToRefs } from 'pinia';
import MovieDetailBaner from '@/components/MovieDetailView/MovieDetailBaner.vue';
import MovieDetailBestReviewList from '@/components/MovieDetailView/MovieDetailBestReviewList.vue';
import MovieDetailReviewCreate from '@/components/MovieDetailView/MovieDetailReviewCreate.vue';
import MovieDetailReviewList from '@/components/MovieDetailView/MovieDetailReviewList.vue';

const route = useRoute()
const store = useMovieStore()

const movieId = route.params.movieid
const movie = ref(null)
const { moviecomments } = storeToRefs(store)

const isLoading = ref(true)

const createComment = function(payload) {
    store.createComment(movieId, payload)
}

onMounted(async () => {
    try {
        isLoading.value = true
        movie.value = await store.getMovie(movieId)
        await Promise.all([
            store.getMovieComments(movieId),
            store.getBestComments(movieId)
        ])
    } catch (error) {
        console.error('영화 정보 로딩 실패:', error)
    } finally {
        isLoading.value = false
    }
})
</script>

<style scoped>
.loading-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 60vh;
}

.loading-spinner {
    text-align: center;
    color: var(--point-peach);
}

.loading-spinner p {
    margin-top: 1rem;
    font-size: 1.1rem;
    color: #666;
}

.error-container {
    text-align: center;
    padding: 2rem;
    color: #666;
}

@keyframes fadeIn {
    from {
        opacity: 0;
    }
    to {
        opacity: 1;
    }
}

.loading-container, .error-container {
    animation: fadeIn 0.3s ease-in;
}
</style>