<template>
    <div>
        <span @click="openFollowingsModal" class="modal-parent">Following : {{ userProfile.followings.length }}</span>
        <span @click="openFollowersModal" class="modal-parent">Follower : {{ userProfile.followers.length }}</span>
        <br>
        <FollowingModal v-if="isFollowingsModal" @close="closeFollowingsModal"/>
        <FollowerModal v-if="isFollowersModal" @close="closeFollowersModal"/>
        <div v-if="userProfile.username!==logedinUsername">
            <button v-if="isFollowing()" @click="store.toggleFollowerbutton(userProfile.id, userProfile.username)">unFollow</button>
            <button v-else @click="store.toggleFollowerbutton(userProfile.id, userProfile.username)">Follow</button>
        </div>
    </div>
</template>

<script setup>
import { ref, watch } from 'vue';
import { useMovieStore } from '@/stores/movie';
import { storeToRefs } from 'pinia';
import FollowingModal from './FollowingModal.vue';
import FollowerModal from './FollowerModal.vue';

const store = useMovieStore()
const {userProfile, logedinUsername} = storeToRefs(store)
const isFollowingsModal = ref(false)
const isFollowersModal = ref(false)
const isFollowing = function () {
    return userProfile.value.followers.some(person=>person.username===logedinUsername.value)
}

const openFollowingsModal = function () {
    isFollowingsModal.value = true
}

const closeFollowingsModal = function () {
    isFollowingsModal.value = false
}

const openFollowersModal = function () {
    isFollowersModal.value = true
}

const closeFollowersModal = function () {
    isFollowersModal.value = false
}
</script>

<style scoped>
.modal-parent {
  position: relative; /* 부모의 상대적 위치를 기준으로 자식 위치 설정 */
  display: inline-block;
  padding: 10px;
  border: 1px solid #ccc;
  cursor: pointer;
}
</style>