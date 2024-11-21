<template>
    <div>
        <span>Following : {{ userProfile.followings.length }}</span> |
        <span>Follower : {{ userProfile.followers.length }}</span>
        <br>
        <div v-if="userProfile.username!==logedinUsername">
            <button v-if="isFollowing()">unFollow</button>
            <button v-else>Follow</button>
        </div>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';
import { storeToRefs } from 'pinia';

const store = useMovieStore()
const {userProfile, logedinUsername} = storeToRefs(store)
const isFollowing = function () {
    return userProfile.value.followers.some(person=>person.username===logedinUsername.value)
}


</script>

<style scoped>

</style>