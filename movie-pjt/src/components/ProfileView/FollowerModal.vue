<template>
    <div class="modal-backdrop" @click.self="closeModal">
        <div class="modal-content">
            <h3>Followers List</h3>
            <button class="close-button" @click="closeModal">
                <font-awesome-icon :icon="['fas', 'times']" />
            </button>
            <hr>
            <div v-for="follower in userProfile.followers" :key="follower.id">
                <RouterLink :to="{name:'profile', params:{username:follower.username}}" @click.native="closeModal">
                    {{ follower.nickname }} | {{ follower.username }}
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
/* 모달 백드롭 (배경) */
.modal-backdrop {
    position: fixed;  /* absolute에서 fixed로 변경 */
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.3);  /* 어두운 배경 추가 */
    backdrop-filter: blur(4px);  /* 블러 효과 */
    display: flex;
    justify-content: center;
    align-items: center;
    z-index: 1000;
}

/* 모달 내용 */
.modal-content {
    background: rgba(255, 255, 255, 0.95);
    padding: 25px;
    width: 300px;
    max-height: 400px;
    border-radius: 25px;
    position: relative;
    box-shadow: 0 8px 32px rgba(255, 103, 103, 0.15);
    border: 1px solid rgba(255, 255, 255, 0.4);
    overflow-y: auto;
    animation: fadeIn 0.3s ease-out;
}

/* 스크롤바 스타일링 */
.modal-content::-webkit-scrollbar {
    width: 6px;
}

.modal-content::-webkit-scrollbar-track {
    background: rgba(255, 103, 103, 0.05);
    border-radius: 10px;
}

.modal-content::-webkit-scrollbar-thumb {
    background: rgba(255, 103, 103, 0.3);
    border-radius: 10px;
}

.modal-content h3 {
    color: #222324;
    font-size: 1.5rem;
    font-weight: 600;
    margin-bottom: 1.2rem;
    text-align: center;
}

.modal-content span {
    position: absolute;
    top: 15px;
    right: 15px;
    cursor: pointer;
    color: rgba(67, 64, 64, 0.8);
    font-size: 1.2rem;
    padding: 5px 10px;
    border-radius: 50%;
    transition: all 0.3s ease;
}

.modal-content span:hover {
    color: rgba(255, 103, 103, 0.8);
    transform: rotate(90deg);
}

.modal-content hr {
    border: none;
    height: 1px;
    background: linear-gradient(
        to right,
        transparent,
        rgba(255, 103, 103, 0.2),
        rgba(255, 103, 103, 0.3),
        rgba(255, 103, 103, 0.2),
        transparent
    );
    margin: 10px 0;
}

.modal-content a {
    display: block;
    padding: 12px 16px;
    color: #434040;
    text-decoration: none;
    transition: all 0.3s ease;
    border-radius: 15px;
    font-weight: 500;
    margin: 5px 0;
}

.modal-content a:hover {
    background: rgba(255, 103, 103, 0.1);
    color: rgba(255, 103, 103, 0.8);
    transform: translateX(5px);
}

/* 닫기 버튼 스타일 */
.close-button {
    position: absolute;
    top: 15px;
    right: 15px;
    width: 32px;
    height: 32px;
    border-radius: 50%;
    border: none;
    background: rgba(255, 255, 255, 0.9);
    color: rgba(67, 64, 64, 0.8);
    cursor: pointer;
    display: flex;
    align-items: center;
    justify-content: center;
    transition: all 0.3s ease;
    font-size: 1.1rem;
    padding: 0;
    box-shadow: 0 2px 8px rgba(255, 103, 103, 0.1);
}

.close-button:hover {
    background: rgba(255, 103, 103, 0.1);
    color: rgba(255, 103, 103, 0.8);
    transform: rotate(90deg);
    box-shadow: 0 4px 12px rgba(255, 103, 103, 0.15);
}

/* 애니메이션 */
@keyframes fadeIn {
    from {
        opacity: 0;
        transform: translateY(10px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}
</style>