<template>
    <div>
        <hr>
        <RouterLink :to="{name:'password'}">비밀 번호 수정</RouterLink> | 
        <RouterLink :to="{name:'userinfoupdate', params:{'username':profile.username}}">회원 정보 수정</RouterLink> | 
        <RouterLink :to="{name:'accountdelete'}">회원 탈퇴</RouterLink>
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

</style>