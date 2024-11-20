<template>
    <div>
        <ProfileComponent/>
        <hr>
        <RouterLink :to="{name:'profile'}">My Level</RouterLink> | 
        <RouterLink :to="{name:'wishmovies'}">Wish Movie</RouterLink> | 
        <RouterLink :to="{name:'mynotelist'}">My Voca Note</RouterLink> |
        <RouterLink :to="{name:'myreviews'}">My Reviews</RouterLink>
        <hr>
        <RouterView/>
    </div>
</template>

<script setup>
import ProfileComponent from '@/components/ProfileView/ProfileComponent.vue';
</script>

<style scoped>

</style>