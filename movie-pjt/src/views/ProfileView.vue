<template>
    <div>
        <ProfileComponent/>
    </div>
    <hr>
    <div>
        <RouterLink :to="{name:'profile'}">My Level</RouterLink> | 
        <RouterLink :to="{name:'wishmovies'}">Wish Movie</RouterLink> | 
        <RouterLink :to="{name:'mynotelist'}">My Voca Note</RouterLink>
    </div>
    <hr>
    <div>
        <RouterView/>
    </div>
</template>

<script setup>
import ProfileComponent from '@/components/ProfileView/ProfileComponent.vue';
import { RouterLink, RouterView } from 'vue-router';

import VocaNoteListView from './ProfileNesting/VocaNoteListView.vue';
import WishMovieListView from './ProfileNesting/WishMovieListView.vue';
</script>

<style scoped>

</style>