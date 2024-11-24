<template>
<div class="main-container">
  <nav class="navbar navbar-expand-lg bg-body-tertiary rounded-custom">
    <div class="container-fluid">
      <RouterLink :to="{name:'movies'}" v-if="store.isLogin" class="navbar-brand">MoviENg</RouterLink>
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav ms-auto mb-2 mb-lg-0">
          <li class="nav-item mx-2">
            <RouterLink :to="{name:'login'}" v-if="!store.isLogin" class="nav-link active" aria-current="page">Log in</RouterLink>
          </li>
          <li class="nav-item mx-2">
            <RouterLink :to="{name:'signup'}" v-if="!store.isLogin" class="nav-link active" aria-current="page">Sign Up</RouterLink>
          </li>
          <li class="nav-item mx-2">
          </li>
          <li class="nav-item dropdown ms-auto" v-if="store.isLogin">
            <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
              안녕하세요! {{ store.logedinUsername }} 님!
            </a>
            <ul class="dropdown-menu" v-if="store.logedinUsername">
              <li><RouterLink :to="{name:'wishmovies', params:{username:store.logedinUsername}}" class="dropdown-item">Wish Movie</RouterLink></li>
              <li><RouterLink :to="{name:'mynotelist', params:{username:store.logedinUsername}}" class="dropdown-item">Voca Note</RouterLink></li>
              <li><hr class="dropdown-divider"></li>
              <li><RouterLink :to="{name:'profile', params:{username:store.logedinUsername}}" class="dropdown-item">My Page</RouterLink></li>
              <li><hr class="dropdown-divider"></li>
              <li><button @click="store.logOut" class="logout-btn">Log out</button></li>
            </ul>
          </li>
        </ul>
      </div>
    </div>
  </nav>
  <RouterView/>
  <chatBot />
  <footer>
    <div>
      <p>ⓒ 2024. </p>
    </div>
  </footer>
</div>
</template>

<script setup>
import { useMovieStore } from './stores/movie';
import chatBot from './components/chatBot.vue';

const store = useMovieStore()
</script>

<style scoped>
/* 전체 navbar에 둥근 모서리 적용 */
.navbar.rounded-custom {
  border-radius: 20px; /* 모서리 둥글게 */
  padding: 10px; /* 내부 여백 */
}

/* 드롭다운 메뉴도 둥글게 */
.navbar .dropdown-menu {
  border-radius: 10px; /* 드롭다운 둥근 모서리 */
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2); /* 드롭다운 그림자 */
}

/* 버튼에 약간의 둥근 효과 */
.navbar-toggler {
  border-radius: 5px;
}

.custom-toggler .navbar-toggler-icon {
    background-color: transparent;
    border: none; /* 커스터마이징된 스타일 */
    width: 30px;
    height: 30px;
  }

.logout-btn {
  background-color: white; /* 흰 바탕 */
  color: #ff6b6b; /* 컬러 글씨 */
  border: 2px solid #ff6b6b; /* 컬러 테두리 */
  border-radius: 15px; /* 둥근 모서리 */
  padding: 10px 15px; /* 버튼 크기 조정 */
  font-size: 16px; /* 텍스트 크기 */
  font-weight: bold; /* 강조된 글꼴 */
  cursor: pointer; /* 클릭 가능하게 표시 */
  transition: background-color 0.3s ease, color 0.3s ease, transform 0.2s ease; /* 부드러운 애니메이션 */
  margin-top: 10px; /* 버튼 위쪽 여백 */
  margin-bottom: 5px; /* 버튼 아래쪽 여백 */
  margin-left: 10px; /* 왼쪽 여백 */
  margin-right: 10px; /* 오른쪽 여백 */
  width: calc(100% - 20px); /* 드롭다운 너비에 맞도록 조정 */
}

/* Hover 효과 */
.logout-btn:hover {
  background-color: #ff6b6b; /* 컬러 배경 */
  color: white; /* 흰색 글씨 */
  transform: scale(1.05); /* 살짝 커지는 효과 */
}

/* Focus 스타일 */
.logout-btn:focus {
  outline: none; /* 기본 포커스 제거 */
  box-shadow: 0 0 5px 2px rgba(255, 107, 107, 0.5); /* 포커스 시 강조 그림자 */
}

@media (max-width: 992px) {
  .dropdown-menu {
    background-color:transparent; /* 배경색 흰색 */
    width: 100%; /* 메뉴 너비를 전체로 확장 */
    position: static; /* 고정 위치 해제 */
    border: none; /* 테두리 제거 */
    box-shadow: none; /* 그림자 제거 */
    padding: 0; /* 패딩 제거 */
  }

  .dropdown-menu .dropdown-item {
    display: block; /* 아이템을 블록 요소로 설정 */
    width: 100%; /* 아이템 너비 전체 확장 */
    text-align: center; /* 텍스트 중앙 정렬 */
    color: #363636; /* 텍스트 기본 색상 */
    padding: 10px 0; /* 내부 여백 조정 */
    background-color: transparent; /* 배경 투명 */
  }

  .dropdown-menu .dropdown-item:hover {
    background-color: #cfcece; /* Hover 시 배경 변경 */
    color: rgb(0, 0, 0); /* 텍스트 반전 */
  }
  .navbar-nav {
    width: 100%; /* navbar 전체 너비 사용 */
  }

  .nav-item {
    width: 100%; /* 각 항목이 전체 너비 차지 */
  }
}
</style>