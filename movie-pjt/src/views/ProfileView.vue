<template>
  <div v-if="userProfile" class="profile-page">
    <div class="user-container">
      <div class="user-header">
        <h1>{{ userProfile.nickname }}</h1>
        <ProfileFollow class="profile-follow" />
      </div>
      <div
        v-if="userProfile.username === store.logedinUsername"
        class="study-level-section"
      >
        <h5>학습 레벨 변경하기</h5>
        <form>
          <select
            name="학습 레벨"
            id="studylevel"
            v-model="store.userProfile.study_level"
            @change.prevent="updateLevel($event.target.value)"
          >
            <option
              v-for="level in store.difficulties"
              :key="level"
              :value="level"
            >
              {{ level }}
            </option>
          </select>
        </form>
      </div>
      <div class="profile-component-section">
        <ProfileComponent
          :profile="userProfile"
          v-if="userProfile.username === store.logedinUsername"
        />
      </div>
    </div>
    <div class="user-router-container">
  <div class="links-container">
    <RouterLink
      :to="{ name: 'userlevel', params: { username: userProfile.username } }"
      :class="{ active: isActive('userlevel') }"
    >
      User Level
    </RouterLink>
    <RouterLink
      :to="{
        name: 'wishmovies',
        params: { username: userProfile.username },
      }"
      :profile="userProfile"
      :class="{ active: isActive('wishmovies') }"
      >Wish Movie</RouterLink
    >
    <RouterLink
      :to="{
        name: 'mynotelist',
        params: { username: userProfile.username },
      }"
      :profile="userProfile"
      :class="{ active: isActive('mynotelist') }"
      >Voca Note</RouterLink
    >
    <RouterLink
      :to="{
        name: 'myreviews',
        params: { username: userProfile.username },
      }"
      :profile="userProfile"
      v-if="userProfile.username === store.logedinUsername"
      :class="{ active: isActive('myreviews') }"
      >My Reviews</RouterLink
    >
    <RouterLink
      :to="{
        name: 'likedreviews',
        params: { username: userProfile.username },
      }"
      :profile="userProfile"
      v-if="userProfile.username === store.logedinUsername"
      :class="{ active: isActive('likedreviews') }"
      >Liked Reviews</RouterLink
    >
  </div>
  <div class="view-container">
    <RouterView :key="$route.fullpath" />
  </div>
</div>

  </div>
</template>

<script setup>
import ProfileComponent from "@/components/ProfileView/ProfileComponent.vue";
import ProfileFollow from "@/components/ProfileView/ProfileFollow.vue";
import { useMovieStore } from "@/stores/movie";
import { ref, onMounted, watch } from "vue";
import { useRoute } from "vue-router";
import { storeToRefs } from "pinia";
const store = useMovieStore();
const route = useRoute();
const { userProfile } = storeToRefs(store);

// 드롭다운 상태 관리
const isDropdownOpen = ref(false);

const chosenLevel = ref('A1')

// 드롭다운 열기/닫기
const toggleDropdown = () => {
    isDropdownOpen.value = !isDropdownOpen.value;
};

const updateLevel = function (level, username = route.params.username) {
  const payload = {
    study_level: level,
  };
  store.updateUserStudyLevel(payload, username);
};

// 현재 라우트가 일치하는지 확인하는 함수
const isActive = (routeName) => {
  return route.name === routeName;
};


const isDeactive = function (parentName) {
  return (
    route.matched.length > 1 && // 부모-자식 관계가 있는지 확인
    route.matched[0].name === parentName // 첫 번째 라우터가 해당 부모 라우터인지 확인
  );
};


onMounted(() => {
  store.getUserProfile(route.params.username);
});

watch(
  () => route.params.username,
  (newUsername) => {
    store.getUserProfile(newUsername);
  }
);
</script>

<style scoped>
.profile-page {
  display: flex;
  justify-content: space-between; /* 왼쪽과 오른쪽을 간격 띄우기 */
  align-items: flex-start; /* 위쪽 정렬 */
  gap: 20px; /* 두 컨테이너 사이 간격 */
  margin-top: 20px;
}

.user-container {
  background: rgba(255, 255, 255, 0.6);
  border-radius: 2rem;
  flex: 1; /* 왼쪽 영역 */
  max-width: 30%; /* 너비 제한 */
  padding: 1.5rem;
  min-height: 100vh; /* 최소 높이를 화면 전체로 설정 */
}

.user-router-container {
    display: flex;
    flex-direction: column;
    background:rgba(255, 255, 255, 0.6);
    border-radius: 2rem;
    flex: 1;
    max-width: 70%;
    padding: 1.5rem;
    min-height: 100vh;
}

/* 헤더 스타일 */
.view-container {
  flex-grow: 1;
  overflow-y: auto;
  padding: 10px;
  background-color: transparent;
}

.user-header {
  display: flex;
  flex-direction: column; /* 세로 방향 정렬 */
  align-items: center; /* 왼쪽 정렬 */
  margin-bottom: 15px;
  gap: 10px; /* h1과 profile-follow 사이의 간격 */
}

.user-header h1 {
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
  margin-top: 20px;
}

.profile-follow {
  align-self: stretch; /* 버튼이 부모의 너비에 맞게 확장되도록 설정 */
  text-align: center; /* 버튼 안의 텍스트 가운데 정렬 */
}

/* 학습 레벨 섹션 */
.study-level-section {
  margin-bottom: 20px;
}

.study-level-section h5 {
  font-size: clamp(0.9rem, 4vw, 1.2rem); /* 반응형 폰트 크기 */
  color: #555;
  margin-bottom: 10px;
}

.study-level-section select {
  width: 100%;
  padding: 10px;
  font-size: 1rem;
  border: 1px solid #ccc;
  border-radius: 10px;
  background-color: #fff;
  appearance: none;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  cursor: pointer;
  transition: all 0.3s ease;  /* 부드러운 전환 효과 추가 */
}

/* 포커스 효과 추가 */
.study-level-section select:focus {
  outline: none;
  border-color: rgba(243, 94, 94, 0.8);
  box-shadow: 0 0 0 3px rgba(243, 94, 94, 0.15);
}

/* hover 효과도 추가 */
.study-level-section select:hover {
  border-color: rgba(243, 94, 94, 0.5);
}

/* 프로필 컴포넌트 섹션 */
.profile-component-section {
  margin-top: 20px;
}

/* 반응형 레이아웃 */
@media (max-width: 1200px) {
  .user-container {
    padding: 15px;
  }

  .user-header h1 {
    margin-top: 20px;
    font-size: clamp(1rem, 4vw, 1.5rem); /* 작은 화면에 맞게 폰트 크기 축소 */
  }

  .user-header {
    flex-direction: column; /* 세로 방향 정렬 */
    align-items: center; /* 왼쪽 정렬 */
    gap: 10px; /* 제목과 Follow 버튼 사이 간격 */
  }

  .profile-follow {
    align-self: stretch; /* Follow 버튼이 부모 너비에 맞게 확장되도록 설정 */
    text-align: center; /* 텍스트 가운데 정렬 */
  }

  .study-level-section h5 {
    font-size: clamp(0.8rem, 3vw, 1rem); /* 작은 화면에 맞게 폰트 크기 축소 */
  }

  select {
    font-size: 0.9rem; /* 선택 박스 폰트 크기 조정 */
  }

  .links-container a {
    font-size: 14px; /* 글씨 크기를 줄임 */
    text-align: center; /* 중앙 정렬 */
  }
}

hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 1rem 0;
}

.links-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
  margin-bottom: 10px;
}

.links-container a {
  text-decoration: none;
  color: rgb(85, 85, 85);
  padding: 5px 10px;
  transition: background-color 0.3s, color 0.3s;
}

.links-container a:hover {
  background-color: #f0f0f0;
}

.router-link-active {
  background-color: transparent;
  color: rgb(32, 32, 32);
  border-bottom: rgba(243, 94, 94, 0.8) 3px solid;
  font-weight: bold;
}

/* 모든 h1 태그에 대한 공통 스타일 */
h1 {
  color: #222324;
  font-size: 2rem;
  font-weight: 750;
  margin-bottom: 1.5rem;
  text-align: center;
}

/* user-header의 h1은 더 크게 */
.user-header h1 {
  font-size: 2.2rem;
  margin-top: 20px;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

@media (max-width: 1200px) {
  h1 {
    font-size: 1.8rem;
  }
  
  .user-header h1 {
    font-size: 2rem;
  }
}

</style>
