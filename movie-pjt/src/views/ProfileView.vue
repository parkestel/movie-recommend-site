<template>
    <div>
        <ProfileComponent/>
        <hr>
        <RouterLink :to="{name:'profile', params:{username:store.logedinUsername}}">My Level</RouterLink> | 
        <RouterLink :to="{name:'wishmovies', params:{username:store.logedinUsername}}">Wish Movie</RouterLink> | 
        <RouterLink :to="{name:'mynotelist', params:{username:store.logedinUsername}}">My Voca Note</RouterLink> |
        <RouterLink :to="{name:'myreviews', params:{username:store.logedinUsername}}">My Reviews</RouterLink> | 
        <RouterLink :to="{name:'likedreviews', params:{username:store.logedinUsername}}">Liked Reviews</RouterLink>
        <hr>
        <RouterView/>
    </div>
</template>

<script setup>
import ProfileComponent from '@/components/ProfileView/ProfileComponent.vue';
import { useMovieStore } from '@/stores/movie';
const store = useMovieStore()
</script>

<style scoped>

</style>