<template>
    <div v-if="store.userProfile">
        <ProfileComponent :profile="store.userProfile"/>
        <hr>
        <RouterLink :to="{name:'profile', params:{username:store.logedinUsername}}" :profile="store.userProfile">My Level</RouterLink> | 
        <RouterLink :to="{name:'wishmovies', params:{username:store.logedinUsername}}" :profile="store.userProfile">Wish Movie</RouterLink> | 
        <RouterLink :to="{name:'mynotelist', params:{username:store.logedinUsername}}" :profile="store.userProfile">My Voca Note</RouterLink> |
        <RouterLink :to="{name:'myreviews', params:{username:store.logedinUsername}}" :profile="store.userProfile"  v-if="route.params.username===store.logedinUsername">My Reviews</RouterLink> | 
        <RouterLink :to="{name:'likedreviews', params:{username:store.logedinUsername}}" :profile="store.userProfile"  v-if="route.params.username===store.logedinUsername">Liked Reviews</RouterLink>
        <hr>
        <RouterView :key="$route.fullpath"/>
    </div>
</template>

<script setup>
import ProfileComponent from '@/components/ProfileView/ProfileComponent.vue';
import { useMovieStore } from '@/stores/movie';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { storeToRefs } from 'pinia';
const store = useMovieStore()
const route = useRoute()
const { userProfile } = storeToRefs(store)

console.log(userProfile.value)
onMounted(()=>{
    store.getUserProfile(route.params.username)
})
</script>

<style scoped>

</style>