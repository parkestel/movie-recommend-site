<template>
    <div>
        <div class="follow-container">
            <span @click="openFollowingsModal" class="modal-parent" id="following">Following : {{ userProfile.followings.length }}</span>
            <span @click="openFollowersModal" class="modal-parent" id="follower">Follower : {{ userProfile.followers.length }}</span>
        </div>
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
  border: 1px solid #92bef8;
  cursor: pointer;
  font-style: bold;
  color: #92bef8;
  background-color: #cee3fd65
  ;
}

#following{
    border-top-left-radius: 1.3rem;
    border-bottom-left-radius: 1.3rem;
    padding-left: 20px;
    padding-right: 20px;
}

#follower{
    border-top-right-radius: 1.3rem;
    border-bottom-right-radius: 1.3rem;
    padding-right: 25px;
    padding-left: 25px
}

.follow-container{
    margin-top: 30px;
}

@media (max-width: 900px) {
    #following{
        border-radius: 1.3rem;
    }
    #follower{
        border-radius: 1.3rem;
    }
}
</style>