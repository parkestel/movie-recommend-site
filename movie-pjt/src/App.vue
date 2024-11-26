<template>
  <div>
    <!-- 네비게이션바와 메인 컨테이너가 필요없는 페이지들 -->
    <template v-if="isPublicPage">
      <HomeView v-if="$route.name === 'home'"/>
      <RouterView v-else/>
    </template>
    
    <!-- 네비게이션바와 메인 컨테이너가 필요한 페이지들 -->
    <AppChild v-else/>
  </div>
</template>

<script setup>
import { useMovieStore } from './stores/movie';
import { useRoute, useRouter } from 'vue-router';
import { computed, watch } from 'vue';
import AppChild from '@/views/AppChild.vue'
import HomeView from '@/views/HomeView.vue'

const store = useMovieStore()
const route = useRoute()
const router = useRouter()

// 네비게이션바와 메인 컨테이너가 필요없는 페이지들
const publicPages = ['home', 'login', 'signup']

const isPublicPage = computed(() => {
  return !store.isLogin || publicPages.includes(route.name)
})

// 로그인 상태 변화 감지
watch(() => store.isLogin, (newValue) => {
  if (!newValue) {
    // 로그아웃 시 홈페이지로 리다이렉트
    router.push({ name: 'home' })
  }
})
</script>

<style>
/* 전역 스타일 유지 */
</style>