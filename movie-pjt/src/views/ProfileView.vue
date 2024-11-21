<template>
    <div v-if="userProfile">
        <h1>{{ userProfile.nickname }} 님의 페이지 입니다.</h1>
        <ProfileComponent :profile="userProfile" v-if="userProfile.username===store.logedinUsername"/>
        <ProfileFollow :follow-info="{followers:userProfile.followers, followings:userProfile.followings}"/>
        <hr>
        <RouterLink :to="{name:'profile', params:{username:userProfile.username}}" :profile="store.userProfile">User Level</RouterLink> | 
        <RouterLink :to="{name:'wishmovies', params:{username:userProfile.username}}" :profile="store.userProfile">Wish Movie</RouterLink> | 
        <RouterLink :to="{name:'mynotelist', params:{username:userProfile.username}}" :profile="store.userProfile">User's Voca Note</RouterLink> |
        <RouterLink :to="{name:'myreviews', params:{username:userProfile.username}}" :profile="store.userProfile"  v-if="userProfile.username===store.logedinUsername">My Reviews</RouterLink> | 
        <RouterLink :to="{name:'likedreviews', params:{username:userProfile.username}}" :profile="store.userProfile"  v-if="userProfile.username===store.logedinUsername">Liked Reviews</RouterLink>
        <hr>
        <RouterView :key="$route.fullpath"/>
    </div>
</template>

<script setup>
import ProfileComponent from '@/components/ProfileView/ProfileComponent.vue';
import ProfileFollow from '@/components/ProfileView/ProfileFollow.vue';
import { useMovieStore } from '@/stores/movie';
import { ref, onMounted, watch } from 'vue';
import { useRoute } from 'vue-router';
import { storeToRefs } from 'pinia';
const store = useMovieStore()
const route = useRoute()
const { userProfile } = storeToRefs(store)

onMounted(()=>{
    store.getUserProfile(route.params.username)
    console.log(userProfile.value)
})

watch(() => route.params.username, (newUsername) => {
    store.getUserProfile(newUsername);
});
</script>

<style scoped>

</style>