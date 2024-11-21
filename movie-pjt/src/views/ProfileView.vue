<template>
    <div v-if="store.userProfile">
        <ProfileComponent :profile="store.userProfile"/>
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
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
const store = useMovieStore()
const route = useRoute()

onMounted(()=>{
    store.getUserProfile(route.params.username)
})
</script>

<style scoped>

</style>