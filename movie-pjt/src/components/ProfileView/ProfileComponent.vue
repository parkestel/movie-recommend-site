<template>
    <div class="profile-actions">
        <hr>
        <RouterLink class="category-link" :to="{name:'password'}">비밀 번호 수정</RouterLink>
        <RouterLink class="category-link" :to="{name:'userinfoupdate', params:{'username':profile.username}}">회원 정보 수정</RouterLink>
        <RouterLink class="category-link" :to="{name:'accountdelete'}">회원 탈퇴</RouterLink>
        <hr>
    </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()

defineProps({
    profile:Object
})
</script>

<style scoped>
.profile-actions {
    display: flex;
    flex-direction: column; /* 세로 정렬 */
    align-items: center;
    gap: 10px; /* 링크 간 간격 */
    margin: 20px 0;
    padding: 10px 0;
    border-top: 2px solid #ddd; /* 상단 보더 */
    border-bottom: 2px solid #ddd; /* 하단 보더 */
}

.category-link {
    text-decoration: none;
    color: rgb(85, 85, 85); /* 텍스트 색상 */
    font-size: 16px;
    padding: 8px 0; /* 위아래 간격 */
    width: 80%; /* 중앙 정렬을 위한 너비 */
    text-align: center; /* 텍스트 가운데 정렬 */
}

.category-link:hover {
    color: rgb(32, 32, 32); /* 호버 시 텍스트 색상 */
    border-bottom: 3px solid rgba(243, 94, 94, 0.8); /* 호버 시 하단 보더 색상 */
}

.router-link-active {
    color: rgb(32, 32, 32); /* 활성화된 링크 색상 */
    font-weight: bold; /* 활성화된 링크 굵기 */
    border-bottom: 3px solid rgba(243, 94, 94, 0.8); /* 활성화된 링크 하단 보더 */
}


</style>