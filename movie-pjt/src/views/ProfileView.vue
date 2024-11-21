<template>
    <div>
        <ProfileComponent/>
        <hr>
        <RouterLink :to="{name:'profile', params:{username:user}}">My Level</RouterLink> | 
        <RouterLink :to="{name:'wishmovies', params:{username:user}}">Wish Movie</RouterLink> | 
        <RouterLink :to="{name:'mynotelist', params:{username:user}}">My Voca Note</RouterLink> |
        <RouterLink :to="{name:'myreviews', params:{username:user}}">My Reviews</RouterLink> | 
        <RouterLink :to="{name:'likedreviews', params:{username:user}}">Liked Reviews</RouterLink>
        <hr>
        <RouterView/>
    </div>
</template>

<script setup>
import ProfileComponent from '@/components/ProfileView/ProfileComponent.vue';
import { useMovieStore } from '@/stores/movie';
import { onMounted } from 'vue';
import { useRoute } from 'vue-router';

const store = useMovieStore()
const user = store.logedinUsername
const route = useRoute()

onMounted(()=>{
    store.getUserProfile(route.params.username)
    console.log(store.userProflie)
})
</script>

<style scoped>

</style>