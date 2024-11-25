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
.follow-container {
    margin-top: 20px;
    display: flex;
    justify-content: center;
}

.modal-parent {
    position: relative;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 12px 20px;
    font-size: 14px;
    font-weight: 750;
    color: #434040;
    background: rgba(40, 44, 52, 0.1);
    backdrop-filter: blur(8px);
    border: 1px solid rgba(40, 44, 52, 0.2);
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.modal-parent:hover {
    background: rgba(40, 44, 52, 0.15);
    transform: translateY(-1px);
    color: #282c34;
}

#following {
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
    border-right: none;
}

#follower {
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
    border-left: none;
}

/* Follow/Unfollow 버튼 스타일 */
button {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 14px 25px;
    margin-top: 15px;
    font-size: 14px;
    font-weight: 750;
    color: #434040;
    background: rgba(40, 44, 52, 0.1);
    backdrop-filter: blur(8px);
    border-radius: 20px;
    border: 1px solid rgba(40, 44, 52, 0.2);
    cursor: pointer;
    transition: all 0.3s ease;
    box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

button:hover {
    background: rgba(40, 44, 52, 0.15);
    transform: translateY(-1px);
    color: #282c34;
}

@media (max-width: 900px) {
    .follow-container {
        flex-direction: column;
        gap: 10px;
    }

    #following, #follower {
        border-radius: 20px;
        border: 1px solid rgba(90, 90, 90, 0.226);
    }
}
</style>