<template>
    <div class="modal-backdrop">
        <div class="modal-content">
            <h3>follower List</h3>
            <span @click="closeModal">X</span>
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
.modal-backdrop {
    background: #ffffff;
    border: 1px solid rgba(90, 90, 90, 0.226);
    box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
    padding: 20px;
    position: absolute;
    z-index: 10;
    width: 300px;
    max-height: 400px;
    border-radius: 1.2rem;
    top: 20%;
    left: 50%;
    transform: translateX(-50%);
    overflow-y: auto;
}

.modal-content {
    position: relative;
}

.modal-content h3 {
    color: #1a365d;
    font-size: 1.5rem;
    font-weight: 750;
    margin-bottom: 1rem;
    text-align: center;
}

.modal-content span {
    position: absolute;
    top: -10px;
    right: -10px;
    cursor: pointer;
    color: #434040;
    font-size: 1.2rem;
    padding: 5px 10px;
    border-radius: 50%;
    transition: all 0.3s ease;
}

.modal-content span:hover {
    color: #1a365d;
}

.modal-content hr {
    border: none;
    height: 1px;
    background: linear-gradient(
        to right,
        transparent,
        rgba(90, 90, 90, 0.2),
        rgba(90, 90, 90, 0.3),
        rgba(90, 90, 90, 0.2),
        transparent
    );
    margin: 10px 0;
}

.modal-content a {
    display: block;
    padding: 10px;
    color: #434040;
    text-decoration: none;
    transition: all 0.3s ease;
    border-radius: 8px;
    font-weight: 600;
}

.modal-content a:hover {
    background: rgba(26, 54, 93, 0.1);
    color: #1a365d;
}
</style>