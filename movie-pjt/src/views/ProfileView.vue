<template>
  <div v-if="userProfile" class="profile-page">
    <div class="user-container">
      <div class="user-header">
        <h1>{{ userProfile.nickname }}</h1>
        <ProfileFollow class="profile-follow" />
      </div>
      <hr class="divider" />
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
      <hr class="divider" />
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
        :to="{ name: 'profile', params: { username: userProfile.username } }"
        :class="{
            // active: $route.name === 'profile' && $route.matched.length === 1,
            deactive: isDeactive('profile'),
        }"
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
      <hr />
      <RouterView :key="$route.fullpath" />
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
  background: #f9f9f9;
  border-radius: 2rem;
  flex: 1; /* 왼쪽 영역 */
  max-width: 30%; /* 너비 제한 */
  padding: 1.5rem;
  min-height: 100vh; /* 최소 높이를 화면 전체로 설정 */
}

.user-router-container {
  background: #f9f9f9;
  border-radius: 2rem;
  flex: 1; /* 오른쪽 영역 */
  max-width: 70%; /* 너비 제한 */
  padding: 1.5rem;
  min-height: 100vh; /* 최소 높이를 화면 전체로 설정 */
}

/* 헤더 스타일 */
.user-header {
  display: flex;
  flex-direction: column; /* 세로 방향 정렬 */
  align-items: flex-start; /* 왼쪽 정렬 */
  margin-bottom: 15px;
  gap: 10px; /* h1과 profile-follow 사이의 간격 */
}

.user-header h1 {
  margin: 0; /* 불필요한 여백 제거 */
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.profile-follow {
  align-self: stretch; /* 버튼이 부모의 너비에 맞게 확장되도록 설정 */
  text-align: center; /* 버튼 안의 텍스트 가운데 정렬 */
}

hr.divider {
  border: none;
  border-top: 1px solid #e0e0e0;
  margin: 20px 0;
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
    font-size: clamp(1rem, 4vw, 1.5rem); /* 작은 화면에 맞게 폰트 크기 축소 */
  }

  .user-header {
    flex-direction: column; /* 세로 방향 정렬 */
    align-items: flex-start; /* 왼쪽 정렬 */
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
}

select {
  width: 100%; /* 선택 박스가 부모의 너비를 채우도록 설정 */
  padding: 10px; /* 내부 여백 */
  font-size: 1rem; /* 글자 크기 */
  border: 1px solid #ccc; /* 테두리 */
  border-radius: 10px; /* 둥근 모서리 */
  background-color: #f9f9f9; /* 밝은 배경색 */
  color: #333; /* 글자 색상 */
  appearance: none; /* 기본 화살표 스타일 제거 */
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Cpath d='M7 10l5 5 5-5z' fill='%23333'/%3E%3C/svg%3E"); /* 화살표 아이콘 추가 */
  background-repeat: no-repeat;
  background-position: right 10px center;
  background-size: 15px;
  cursor: pointer; /* 포인터 모양 변경 */
}
/* select 박스 포커스 스타일 */
select:focus {
  outline: none; /* 기본 포커스 테두리 제거 */
  border-color: #007bff; /* 포커스 시 테두리 색상 변경 */
  box-shadow: 0 0 5px rgba(0, 123, 255, 0.5); /* 포커스 시 그림자 효과 */
}

/* option 스타일 */
option {
  padding: 10px; /* 선택 항목 내부 여백 */
  background-color: #ffffff; /* 옵션 배경색 */
  color: #333; /* 글자 색상 */
  font-size: 1rem; /* 글자 크기 */
}

/* option 선택 시 스타일 */
option:checked {
  background-color: #007bff; /* 선택된 항목 배경색 */
  color: #fff; /* 선택된 항목 글자 색상 */
}

hr {
  border: none;
  border-top: 1px solid #ccc;
  margin: 1rem 0;
}

.user-router-container {
  display: flex;
  flex-direction: column;
}

.links-container {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px; /* 링크 간의 간격 */
  margin-bottom: 10px; /* RouterView와의 간격 */
}

.links-container a {
  text-decoration: none;
  color: rgb(44, 44, 44);
  padding: 5px 10px;
  border-radius: 5px;
  transition: background-color 0.3s, color 0.3s;
}

.links-container a:hover {
  background-color: #f0f0f0;
}

.router-link-active {
  background-color: #007bff;
  color: white;
  font-weight: bold;
}

.router-link-deactive {
text-decoration: none;
  color: rgb(44, 44, 44);
  padding: 5px 10px;
  border-radius: 5px;
  transition: background-color 0.3s, color 0.3s;
}
</style>
