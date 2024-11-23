<template>
    <div>
    <div>
      <img :src="store.getImgUrl(movie.poster_path,200)" alt="">
    </div>
    <h4>{{ movie.title_kr }}</h4>
    <h5>{{ movie.title }}</h5>
    </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()
defineProps({
    movie:Object
})
</script>

<style scoped>

</style>