<template>
    <div>
        <span>{{ review.content }}</span>
        <p><RouterLink :to="{name:'movie-detail',params:{movieid:review.movies[0].id}}">{{ review.movies[0].title }}</RouterLink></p> 
        <hr>
    </div>
</template>

<script setup>
const props = defineProps({
  review:Object
})
</script>

<style scoped>

</style>