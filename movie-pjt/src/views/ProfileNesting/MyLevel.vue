<template>
  <div class="container">
    <header class="header">
      <h2>{{ userProfile.nickname }} 님의 학습 현황</h2>
    </header>
    <div class="profile-section">
      <h4>내 정보</h4>
      <p><strong>포인트:</strong> <span>{{ userProfile.experience }}pt</span></p>
      <p><strong>레벨:</strong> <span>{{ levelEmoji }}</span></p>
      <p>{{ userProfile.nickname }}님의 레벨은 <strong>{{ levelStr }}</strong> 입니다!</p>
    </div>
    <div class="level-graphic">
      <h4>다음 레벨까지...</h4>
      <div class="progress-bar">
        <div class="progress" :style="{ width: userProfile.percent + '%' }"></div>
      </div>
      <p>현재 {{ userProfile.percent }}% 진행했습니다.</p>
      <p>다음 레벨까지 {{ 100 - userProfile.percent }}% 남았어요!</p>
    </div>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { computed, onMounted } from 'vue';
import { storeToRefs } from 'pinia';
import { useRoute } from 'vue-router';

const store = useMovieStore();
const { userProfile } = storeToRefs(store);
const route = useRoute();

// 반응형 데이터 계산
const levelStr = computed(() => {
  switch (userProfile.value.achievement_level) {
    case 1:
      return '풀';
    case 2:
      return '꽃';
    case 3:
      return '나무';
    case 4:
      return '숲';
    default:
      return '새싹';
  }
});

const levelEmoji = computed(() => {
  switch (userProfile.value.achievement_level) {
    case 1:
      return '🌿';
    case 2:
      return '🌼';
    case 3:
      return '🌳';
    case 4:
      return '🌲🌲';
    default:
      return '🌱';
  }
});

onMounted(() => {
  store.getUserProfile(route.params.username);
});
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
  background: linear-gradient(to right, #4c77af, #425875);
  transition: width 0.5s ease-in-out;
}
</style>