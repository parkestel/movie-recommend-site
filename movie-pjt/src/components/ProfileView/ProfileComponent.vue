<template>
    <div>
        <h1>{{ profile.nickname }} 님의 페이지 입니다.</h1>
        <hr>
        <RouterLink :to="{name:'password'}">비밀 번호 수정</RouterLink> | 
        <RouterLink :to="{name:'userinfoupdate'}">회원 정보 수정</RouterLink> | 
        <RouterLink :to="{name:'accountdelete'}">회원 탈퇴</RouterLink>
        <hr>
        <ProfileFollow :follow-info="{followers:profile.followers, followings:profile.followings}"/>
    </div>
</template>

<script setup>
import ProfileFollow from './ProfileFollow.vue';
import { RouterLink } from 'vue-router';

defineProps({
    profile:Object
})
</script>

<style scoped>

</style>