<template>
  <div class="container">
    <header class="header">
      <h1>{{ userProfile.nickname }} 님의 학습 현황</h1>
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
  padding: 2rem;
  background: linear-gradient(to bottom,
    rgba(255, 255, 255, 0.4) 0%,
    rgba(255, 255, 255, 0.35) 50%,
    rgba(255, 255, 255, 0.3) 100%
  );
  box-shadow: 
    0 8px 32px rgba(255, 255, 255, 0.15),
    0 4px 16px rgba(255, 255, 255, 0.1);
  border-radius: 2rem;
  backdrop-filter: blur(8px);
}

.header h1 {
  color: #1a365d;
  font-size: 2rem;
  margin-bottom: 1.5rem;
  font-weight: 750;
  text-align: center;
}

.profile-section {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  background: linear-gradient(145deg,
    rgba(220, 242, 182, 0.25),
    rgba(220, 242, 182, 0.15)
  );
  backdrop-filter: blur(8px);
  padding: 1.5rem;
  border-radius: 1.5rem;
  margin-bottom: 2rem;
  border: 1px solid rgba(90, 90, 90, 0.226);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.level-graphic {
  display: flex;
  flex-direction: column;
  gap: 0.8rem;
  background: linear-gradient(145deg,
    rgba(176, 219, 247, 0.25),
    rgba(176, 219, 247, 0.15)
  );
  backdrop-filter: blur(8px);
  padding: 1.5rem;
  border-radius: 1.5rem;
  border: 1px solid rgba(90, 90, 90, 0.226);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
}

.progress-bar {
  width: 100%;
  height: 1.5rem;
  background-color: rgba(255, 255, 255, 0.8);
  border-radius: 1rem;
  overflow: hidden;
  margin: 1rem 0;
  border: 1px solid rgba(90, 90, 90, 0.226);
}

.progress {
  height: 100%;
  background: #1a365d;
  transition: width 0.3s ease;
}

.profile-section h4,
.profile-section p,
.profile-section strong {
  color: #2f5c1b;
  font-weight: 750;
}

.profile-section span {
  color: #447125;
  font-weight: 750;
}

.level-graphic h4 {
  color: #1a365d;
  font-size: 1.2rem;
  margin-bottom: 0.5rem;
  font-weight: 750;
}

.level-graphic p {
  color: #1a365d;
  margin: 0.5rem 0;
  font-weight: 750;
}
</style>