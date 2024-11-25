<template>
    <div class="container">
      <header class="header">
        <h2>{{userProfile.nickname}} 님의 학습 현황</h2>
        <p>내 학습 현황을 확인해보세요!</p>
      </header>
      <div class="profile-section">
        <h4>내 정보</h4>
        <p><strong>포인트:</strong> <span>{{ points }}pt</span></p>
        <p><strong>레벨:</strong> <span>{{ level }}</span></p>
      </div>
      <div class="level-graphic">
        <h4>레벨 진행도</h4>
        <div class="progress-bar">
          <div class="progress" :style="{ width: progress + '%' }"></div>
        </div>
        <p>{{ progress }}% 달성</p>
      </div>
    </div>
  </template>
  
  <script setup>
import { useMovieStore } from '@/stores/movie';
import { onMounted, ref } from 'vue';
import { storeToRefs } from 'pinia';
import { useRoute } from 'vue-router';

const store = useMovieStore()
const { userProfile } = storeToRefs(store)
const route = useRoute()
  
  // 데이터 추출
  const points = ref(userProfile.value.experience);
  const level = ref(userProfile.value.achievement_level);
  const progress = ref(userProfile.value.percents); // 진행도 퍼센트

onMounted(()=>{
  store.getUserProfile(route.params.username)
})
  </script>
  
  <style>
.container {
    max-width: 100%;
    margin: 0 auto;
    padding: 20px;
    background-color: #ffffff83;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
    text-align: center;
  }
  
  .header {
    margin-bottom: 20px;
  }
  
  .header h2 {
    color: #4c77af;
    font-size: 2rem;
    margin: 0;
  }
  
  .header p {
    font-size: 1rem;
    color: #666;
  }
  
  .profile-section {
    background-color: #f1f8e9;
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
  }
  
  .profile-section h2 {
    margin-bottom: 10px;
  }
  
  .level-graphic {
    padding: 15px;
    background-color: #e3f2fd;
    border-radius: 10px;
  }
  
  .progress-bar {
    width: 100%;
    height: 20px;
    background-color: #eeeeee;
    border-radius: 10px;
    overflow: hidden;
    margin: 10px 0;
  }
  
  .progress {
    height: 100%;
    background-color: #4c6baf;
    transition: width 0.5s ease-in-out;
  }
  </style>
  