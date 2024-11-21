<template>
    <div>
        <span>Following : {{ followInfo.followings }}</span>|
        <span>Follower : {{ followInfo.followers }}</span>
        <br>
        <button>(un)Follow</button>
    </div>
</template>

<script setup>
import { ref } from 'vue';
defineProps({
    followInfo:Object
})
</script>

<style scoped>

</style>