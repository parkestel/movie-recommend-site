<template>
    <div class="container">
        <h1>Movie WishList</h1>
        <div v-if="userProfile.username===store.logedinUsername" class="filter-container">
            <span class="filter-label">단어장이 있는 영화만 보기</span>
            <button 
                @click="toggleFilter" 
                class="toggle-btn"
                :class="{ active: showOnlyWithNote }"
            >
                <span class="toggle-circle"></span>
            </button>
        </div>
        <div v-if="userProfile.username===store.logedinUsername" class="wish-card-container">
            <WishMovieCard  
            v-for="wishMovie in filteredMovies"
            :key="wishMovie.id"
            :wish-movie="wishMovie"
            class="movie-card"/>
        </div>
        <div v-else class="wish-card-container">
            <WishMovieCard  
            v-for="wishMovie in userProfile.wish_movies"
            :key="wishMovie.id"
            :wish-movie="wishMovie"
            class="movie-card"/>
        </div>
    </div>
</template>

<script setup>
import { computed, onMounted, ref } from 'vue';
import { useMovieStore } from '@/stores/movie'
import WishMovieCard from '@/components/WishMovieListView/WishMovieCard.vue'
import { storeToRefs } from 'pinia'

const store = useMovieStore()
const { userProfile, wishMovies, vocaNoteList } = storeToRefs(store)
const withNoteMovie = ref(null)
const showOnlyWithNote = ref(false)

const toggleFilter = () => {
    showOnlyWithNote.value = !showOnlyWithNote.value
}

onMounted(() => {
    store.getWishMovies()
})

const filteredMovies = computed(() => {
    if (!wishMovies.value) return []
    
    if (showOnlyWithNote.value) {
        return wishMovies.value.filter(movie => 
            vocaNoteList.value?.some(note => note.movies[0].id === movie.id)
        )
    } else {
        return wishMovies.value
    }
})
</script>

<style scoped>
.container {
    max-width: 100%;
    margin: 0 auto;
    padding: 20px;
    background-color: #ffffff83;
    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    border-radius: 10px;
  }

.wish-card-container {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 3rem; /* 카드 간의 간격 */
  margin-top: 1rem;
}
/* 영화 카드 */
.movie-card {
  width: 250px;
  overflow: hidden; /* 부모 요소에서 넘치는 부분 숨김 */
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  background: transparent;
  box-shadow: none;
  padding: 10px;
}

.container select {
  width: auto; /* 선택 박스 크기 자동 조절 */
  padding: 4px 8px; /* 내부 여백 조정 */
  font-size: 14px; /* 글자 크기 축소 */
  border: 1px solid #ddd; /* 테두리 추가 */
  border-radius: 4px; /* 둥근 모서리 */
  background-color: #f9f9f9; /* 배경색 */
  box-shadow: 0px 1px 2px rgba(0, 0, 0, 0.1); /* 약간의 그림자 */
  transition: border-color 0.3s ease;
  cursor: pointer; /* 커서 포인터로 변경 */
}

.container select:focus {
  border-color: #007bff; /* 포커스 시 테두리 강조 */
  outline: none;
}

.container select option {
  padding: 4px; /* 옵션 항목의 여백 */
  font-size: 14px; /* 옵션 글자 크기 */
}


/* 호버 효과 - 이미지에만 확대 적용 */
.movie-card:hover .card-img {
  transform: scale(1.05); /* 이미지 확대 */
  box-shadow: 0 3px 8px rgba(0, 0, 0, 0.2); /* 그림자 효과 추가 */
}


  @media (max-width:800px) {
    .wish-card-container {
      grid-template-columns: repeat(3, 1fr); /* 가로 3개 */
    }
  }
  
  @media (max-width: 700px) {
    .wish-card-container {
      grid-template-columns: repeat(1, 1fr); /* 가로1개 */
    }
  }
  
.container h1 {
  color: #1a365d;
  font-size: 2rem;
  margin-bottom: 1.5rem;
  font-weight: 750;
  text-align: center;  /* 중앙 정렬 추가 */
}

/* VocaNoteListView.vue, LikedReviews.vue, MyReview.vue에 추가 */
.container h1 {
  color: #222324;
  font-size: 2rem;
  margin-bottom: 1.5rem;
  font-weight: 750;
  text-align: center;
}

@media (max-width: 1200px) {
  .container h1 {
    font-size: 1.8rem;
  }
}

/* 필터 컨테이너 스타일 */
.filter-container {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 12px;
    margin-bottom: 20px;
}

.filter-label {
    font-size: 14px;
    color: #434040;
    font-weight: 600;
}

/* 토글 버튼 스타일 */
.toggle-btn {
    width: 30px;
    height: 10px;
    background-color: #f0f0f0;
    border-radius: 25px;
    padding: 0;
    position: relative;
    cursor: pointer;
    transition: background-color 0.3s ease;
    border: none;
}

.toggle-circle {
    width: 13px;
    height: 13px;
    background-color: #ffffff;
    border-radius: 50%;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
    position: absolute;
    top: -1.5px;
    left: 2px;
    transition: transform 0.3s ease;
}

/* 활성화 상태 스타일 */
.toggle-btn.active {
    background-color: rgba(255, 103, 103, 0.7);  /* 코랄 색상 */
}

.toggle-btn.active .toggle-circle {
    transform: translateX(15px);
}
</style>