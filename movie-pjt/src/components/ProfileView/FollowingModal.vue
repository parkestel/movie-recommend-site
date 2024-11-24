<template>
    <div class="modal-backdrop">
        <div class="modal-content">
            <h3>Following List</h3>
            <span @click="closeModal">X</span>
            <hr>
            <div v-for="following in userProfile.followings" :key="following.id">
                <RouterLink :to="{name:'profile', params:{username:following.username}}" @click.native="closeModal">
                    {{ following.nickname }} | {{ following.username }}
                </RouterLink>
                <hr>
            </div>
        </div>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/movie';
import { storeToRefs } from 'pinia';

const store = useMovieStore()
const { userProfile } = storeToRefs(store)
const emit = defineEmits(['close'])

const closeModal = function () {
    emit('close')
}
</script>

<style scoped>
.modal-backdrop {
    background: white;
    border: 1px solid #ccc;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    padding: 10px;
    position: absolute;
    margin-left: auto;
    z-index: 10;
    width: 300px;
    height: 400px;
    border-radius: 1.2rem;
     /* 위치 조정 */
     top: 20%; /* 화면 상단에서 약간 아래로 */
    left: 50%; /* 화면의 가운데로 이동 */
    transform: translateX(-50%); /* 수평 가운데 정렬 */
}
.modal-content {
    background: white;
    padding: 20px;
    border-radius: 5px;
    position: relative; /* 상대적인 위치로 자식 요소 배치 */
}

.modal-content h3 {
    margin: 0;
    padding: 0;
    text-align: left; /* 제목을 왼쪽 정렬 */
}

.modal-content span {
    position: absolute;
    top: 10px;
    right: 10px;
    cursor: pointer; /* 마우스 포인터 표시 */
    font-weight: bold;
    font-size: 1.2rem;
}
</style>