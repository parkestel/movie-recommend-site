<template>
    <div v-if="userProfile">
        <h1>{{ userProfile.nickname }} 님의 페이지 입니다.</h1>
        <hr>
        <h5>학습 레벨 변경하기</h5>
        <form>
            <select name="학습 레벨" id="studylevel" v-model="store.userProfile.study_level" @change.prevent="updateLevel($event.target.value)">
                <option v-for="level in store.difficulties" :key="level" :value="level">{{ level }}</option>
            </select>
        </form>
        <ProfileComponent :profile="userProfile" v-if="userProfile.username===store.logedinUsername"/>
        <ProfileFollow/>
        <hr>
        <RouterLink :to="{name:'profile', params:{username:userProfile.username}}" :profile="userProfile">User Level</RouterLink> | 
        <RouterLink :to="{name:'wishmovies', params:{username:userProfile.username}}" :profile="userProfile">Wish Movie</RouterLink> | 
        <RouterLink :to="{name:'mynotelist', params:{username:userProfile.username}}" :profile="userProfile">Voca Note</RouterLink> |
        <RouterLink :to="{name:'myreviews', params:{username:userProfile.username}}" :profile="userProfile"  v-if="userProfile.username===store.logedinUsername">My Reviews</RouterLink> | 
        <RouterLink :to="{name:'likedreviews', params:{username:userProfile.username}}" :profile="userProfile"  v-if="userProfile.username===store.logedinUsername">Liked Reviews</RouterLink>
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

const updateLevel = function (level, username=route.params.username) {
    const payload = {
        study_level: level
    }
    store.updateUserStudyLevel(payload, username)
}

onMounted(()=>{
    store.getUserProfile(route.params.username)
})

watch(() => route.params.username, (newUsername) => {
    store.getUserProfile(newUsername);
});
</script>

<style scoped>

</style>