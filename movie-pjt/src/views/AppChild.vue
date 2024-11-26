<template>
  <div class="main-container">
    <nav class="navbar navbar-expand-lg bg-body-tertiary rounded-custom" v-if="!isPopup">
      <div class="container-fluid">
        <!-- 왼쪽 사용자 정보 영역 -->
        <div class="nav-item" id="welcome" v-if="store.isLogin && store.logedinUsername">
          <div class="welcome-link">
            <span class="welcome-text">안녕하세요!</span>
            <span class="username">{{ store.logedinUsername }} 님</span>
          </div>
        </div>
        
        <!-- 중앙 로고 -->
        <div class="navbar-center">
          <RouterLink v-if="store.isLogin" :to="{name:'movies'}" class="navbar-brand">
            <img :src="logo" alt="MoviENg Logo" class="logo" />
          </RouterLink>
          <RouterLink v-if="!store.isLogin" class="navbar-brand" :to="{name:'login'}">
            <img :src="logo" alt="MoviENg Logo" class="logo" />
          </RouterLink>
        </div>
        
        <!-- 네비게이션 버튼 -->
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
            <!-- Log in -->
            <li class="nav-item mx-2" v-if="!store.isLogin">
              <RouterLink :to="{name:'login'}" class="styled-button">Log in</RouterLink>
            </li>
            <!-- Sign Up -->
            <li class="nav-item mx-2" v-if="!store.isLogin">
              <RouterLink :to="{name:'signup'}" class="styled-button">Sign Up</RouterLink>
            </li>
            <!-- Wish Movie -->
            <li class="nav-item mx-2" v-if="store.isLogin && store.logedinUsername">
              <RouterLink :to="{name:'wishmovies', params:{username:store.logedinUsername}}" class="styled-button">Wish Movie</RouterLink>
            </li>
            <!-- Voca Note -->
            <li class="nav-item mx-2" v-if="store.isLogin && store.logedinUsername">
              <RouterLink :to="{name:'mynotelist', params:{username:store.logedinUsername}}" class="styled-button">Voca Note</RouterLink>
            </li>
            <!-- My Page -->
            <li class="nav-item mx-2" v-if="store.isLogin && store.logedinUsername">
              <RouterLink :to="{name:'profile', params:{username:store.logedinUsername}}" class="styled-button">My Page</RouterLink>
            </li>
            <!-- Log out -->
            <li class="nav-item mx-2" v-if="store.isLogin">
              <button @click="store.logOut" class="styled-button logout">Log out</button>
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <RouterView />
    <chatBot v-if="!route.meta.isPopup && store.isLogin" />
    <footer>
      <p>&copy; 2024 MoviENg. All rights reserved.</p>
    </footer>
  </div>
</template>

    
  <script setup>
    import { useMovieStore } from '@/stores/movie';
    import chatBot from '@/components/chatBot.vue';
    import { computed } from 'vue';
    import { useRoute } from 'vue-router';
    import logo from '@/assets/MoviENg.svg'
  
  const store = useMovieStore()
  
  const route = useRoute();
  
  // 팝업 여부를 라우트의 meta 정보로 확인
  const isPopup = computed(()=>route.meta.isPopup || false)
  </script>
    
  <style scoped>
  /* navbar의 중앙 정렬을 위한 스타일 */
.navbar {
  display: flex;
  justify-content: center; /* 중앙 정렬 */
}

.navbar-center {
  position: absolute;  /* 절대 위치로 변경 */
  left: 50%;          /* 왼쪽에서 50% 위치 */
  transform: translateX(-50%);  /* 중앙 정렬을 위한 이동 */
}

.navbar-brand {
  flex: 0 1 auto; /* 로고가 중앙에 위치하도록 설정 */
  margin: 0; /* 여백 없애기 */
}
  
  /* 버튼 스타일 */
  .styled-button {
  display: inline-block;
  align-items: center;
  justify-content: center;
  padding: 14px 20px; /* 세로를 더 통통하게 */
  font-size: 14px;
  font-weight: 750;
  color: #434040;
  background: rgba(255, 255, 255, 0.15); /* 살짝 투명한 배경 */
  backdrop-filter: blur(8px); /* 유리효과 */
  border-radius: 20px; /* 둥근 모서리 */
  border: 1px solid rgba(90, 90, 90, 0.226); /* 연한 테두리 */
  cursor: pointer;
  gap: 8px; /* 아이콘과 텍스트 간격 */
  transition: background 0.3s ease, transform 0.2s ease; /* 부드러운 효과 */
  text-decoration: none;
  box-shadow:0 4px 10px rgba(0, 0, 0, 0.1);
  }

.styled-button:hover{
  background: rgba(145, 145, 145, 0.25); /* 조금 더 진한 빨간 배경 */
  transform: translateY(-1px); /* 살짝 올라가는 효과 */
  color: #292828; /* 텍스트를 더 진하게 */
}

  /* Log-out 버튼 스타일 */
.styled-button.logout {
  background: rgba(255, 102, 102, 0.15); /* 연한 빨간 계열 배경 */
  color: #ff6666; /* 텍스트를 빨간 계열로 */
  border: 1px solid rgba(255, 102, 102, 0.4); /* 연한 빨간 테두리 */
  transition: background 0.3s ease, transform 0.2s ease; /* 부드러운 전환 */
}

/* Log-out 버튼 호버 효과 */
.styled-button.logout:hover {
  background: rgba(255, 102, 102, 0.25); /* 조금 더 진한 빨간 배경 */
  transform: translateY(-1px); /* 살짝 올라가는 효과 */
  color: #ff4d4d; /* 텍스트를 더 진하게 */
}

.styled-button #welcome{
  display: inline-block; /* 텍스트와 버튼을 인라인으로 */
  padding: 14px 20px;
  font-size: 14px;
  font-weight: 700;
  color: #434040;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(8px);
  border-radius: 20px;
  border: 1px solid rgba(90, 90, 90, 0.226);
  cursor: pointer;
  transition: background 0.3s ease, transform 0.2s ease;
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  text-align: left; /* 텍스트 왼쪽 정렬 */
}

.user-level {
  margin: 5px 0 0 0; /* 상단 여백 추가 */
  font-size: 12px;
  color: #555;
}

footer {
    color: #ffffff; /* 텍스트를 흰색으로 */
    text-align: center; /* 중앙 정렬 */
    padding: 10px 0; /* 위아래 패딩 */
    font-size: 14px; /* 적당한 글씨 크기 */
    font-family: 'Arial', sans-serif; /* 깔끔한 글꼴 */
}

.logo {
  height: 40px;  /* 로고 크기 지정 */
  width: auto;   /* 비율 유지 */
  margin: 8px 0; /* 상하 여백 추가 */
  filter: brightness(0) invert(15%);  /* 진한 차콜 그레이로 변경 */
}

/* Welcome 버튼 스타일 재정의 */
#welcome {
  position: relative;
  display: inline-block;
}

.welcome-link {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  padding: 12px 20px;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(8px);
  border-radius: 20px;
  border: 1px solid rgba(90, 90, 90, 0.226);
  box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
  cursor: default;
}

.welcome-link:hover {
  background: rgba(255, 255, 255, 0.15);
  transform: none;
}

.welcome-text {
  font-size: 12px;
  color: #666;
  margin-bottom: 2px;
}

.username {
  font-size: 14px;
  font-weight: 750;
  color: #292828;
}

/* RouterLink 스타일 초기화 */
.welcome-link:hover .welcome-text {
  color: #434040;
}

.welcome-link:hover .username {
  color: #1a1a1a;
}
</style>