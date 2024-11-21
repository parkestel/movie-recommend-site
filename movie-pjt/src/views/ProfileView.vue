<template>
    <div v-if="store.userProfile">
        <ProfileComponent :profile="store.userProfile"/>
        <hr>
        <RouterLink :to="{name:'profile', params:{username:store.logedinUsername}}" :profile="store.userProfile">My Level</RouterLink> | 
        <RouterLink :to="{name:'wishmovies', params:{username:store.logedinUsername}}" :profile="store.userProfile">Wish Movie</RouterLink> | 
        <RouterLink :to="{name:'mynotelist', params:{username:store.logedinUsername}}" :profile="store.userProfile">My Voca Note</RouterLink> |
        <RouterLink :to="{name:'myreviews', params:{username:store.logedinUsername}}" :profile="store.userProfile">My Reviews</RouterLink> | 
        <RouterLink :to="{name:'likedreviews', params:{username:store.logedinUsername}}" :profile="store.userProfile">Liked Reviews</RouterLink>
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