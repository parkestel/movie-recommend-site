<template>
    <div>
        <h1>My Page</h1>
        <h3>username 님의 페이지임</h3>
        <hr>
        <RouterLink :to="{name:'userinfoupdate'}">회원 정보 수정</RouterLink> | 
        <RouterLink :to="{name:'accountdelete'}">회원 탈퇴</RouterLink>
        <hr>
        <ProfileFollow/>
    </div>
</template>

<script setup>
import ProfileFollow from './ProfileFollow.vue';
import { RouterLink } from 'vue-router';
</script>

<style scoped>

</style>