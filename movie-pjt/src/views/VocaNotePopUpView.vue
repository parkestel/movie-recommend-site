<template>
    <div class="popup-container">
        <div class="voca-container" v-if="vocaList && !isDeleted">
            <div class="button-container" v-if="userProfile.username===store.logedinUsername">
                <button class="emoji-button" v-if="vocaList.is_public" @click="togglePublic(vocaList.movies[0].id)">
                    <font-awesome-icon :icon="['fas', 'lock-open']" class="locker-icon"/>
                </button>
                <button class="emoji-button" v-else @click="togglePublic(vocaList.movies[0].id)">
                    <font-awesome-icon :icon="['fas', 'lock']" class="locker-icon"/>
                </button>
                <button class="emoji-button delete-btn" @click="deleteNote(vocaList.movies[0].id)">
                    <font-awesome-icon :icon="['fas', 'trash-can']"/>
                </button>
            </div>
            <h1>{{ vocaList.movies[0].title }}'s vocanote</h1>
            <VocaCreate :note="vocaList"/>
            <div class="mode-buttons">
                <div class="toggle-container">
                    <span>삭제</span>
                    <button class="toggle-btn" :class="{ active: showDeleteButton }" @click="toggleDeleteButtons">
                        <div class="toggle-circle"></div>
                    </button>
                </div>
                <div class="toggle-container">
                    <span>수정</span>
                    <button class="toggle-btn" :class="{ active: showUpdateButton }" @click="toggleUpdateButtons">
                        <div class="toggle-circle"></div>
                    </button>
                </div>
            </div>
            <VocaListRead
            v-for="voca in vocaList.vocas"
            :key="voca.id"
            :voca="voca"
            :show-delete="showDeleteButton"
            :show-update="showUpdateButton"
            @delete-event="deleteWord"
            @update-event="updateWord"
            @check-event="toggleMemorized"
            />
        </div>
        <div v-if="isDeleted" class="deleted-message">
            <p>삭제 되었습니다.</p>
            <button @click="returnToMyNote()">내 Voca Note List 보러가기</button>
        </div>
    </div>
</template>

<script setup>
import { useMovieStore } from "@/stores/movie";
import { ref, onMounted } from "vue";
import { useRoute } from "vue-router";
import VocaCreate from "@/components/VocaNotePopUpView/VocaCreate.vue";
import VocaListRead from "@/components/VocaNotePopUpView/VocaListRead.vue";
import { storeToRefs } from "pinia";
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

const store = useMovieStore()
const route = useRoute()

// const note = ref(null)
const showDeleteButton = ref(false)
const showUpdateButton = ref(false)
const { userProfile, vocaList } = storeToRefs(store)
const noteId = ref(null)

const emit = defineEmits(['deleteEvent', 'toggleEvent'])
const isDeleted = ref(false)

const deleteNote = function (movieId, userId = userProfile.value.id) {
    const result = window.confirm('Really????')
    if (result) {
        store.deleteNote(movieId,userId)
        isDeleted.value=true
    } else {
        return null
    }
}

const returnToMyNote = function(username=userProfile.value.username) {
    if (window.opener) {
        window.opener.location.reload(); // 부모 창 새로고침
    }
    window.close()
    
}

const togglePublic = function (movieId, userId = userProfile.value.id) {
    store.togglePublicVocaNote(movieId,userId)
    if (window.opener) {
        window.opener.location.reload(); // 부모 창 새로고침
    }
    // emit('toggleEvent', movieId, userId)
}

const deleteWord = function (id) {
    store.deleteVoca(id, noteId.value)
}

const updateWord = function (id, payload) {
    // axios put
    store.updateVoca(id, noteId.value, payload)
    showUpdateButton.value = false
}

const toggleMemorized = function(id) {
    // axios post
    store.memorizedVoca(id,noteId.value)
}

const toggleDeleteButtons = function () {
    showDeleteButton.value = !showDeleteButton.value
}

const toggleUpdateButtons = function () {
    showUpdateButton.value = !showUpdateButton.value
    
    // 수정 토글이 꺼질 때 모든 수정 폼을 닫음
    if (!showUpdateButton.value) {
        // VocaListRead 컴포넌트에 이벤트 전달
        emit('closeAllEditForms')
    }
}

onMounted(()=>{
    noteId.value = route.params.note_id
    store.getVocas(noteId.value)
    isDeleted.value=false
})

</script>

<style scoped>
.popup-container {
  background: rgba(255, 255, 255, 0.95);  /* 선명한 흰색 배경 */
  border-radius: 20px;
  box-shadow: 0 4px 15px rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(90, 90, 90, 0.15);
  margin: 15px;
  min-height: calc(100vh - 30px);  /* 여백 제외한 전체 높이 */
  display: flex;
  flex-direction: column;
}

.voca-container {
  padding: 25px;
  max-width: 400px;
  margin: 0 auto;
  width: 100%;
  flex: 1;
}

h1 {
  font-size: 1.8rem;
  font-weight: 800;
  color: #282c34;
  text-align: center;
  margin: 10px 0 20px 0;
  padding-bottom: 15px;
  border-bottom: 2px solid rgba(40, 44, 52, 0.1);
}

/* 상단 버튼 컨테이너 */
.button-container {
  display: flex;
  justify-content: flex-end;  /* 오른쪽 정렬 */
  gap: 15px;
  margin-bottom: 15px;
  padding: 0 5px;
}

/* 아이콘 버튼 스타일 */
.emoji-button {
  background: transparent;
  border: none;
  padding: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  color: rgba(40, 44, 52, 0.6);
  font-size: 1.1rem;  /* 아이콘 크기 조정 */
}

.emoji-button:hover {
  color: #282c34;
  transform: scale(1.1);
}

/* 삭제 버튼 특별 스타일 */
.delete-btn {
  color: rgba(255, 103, 103, 0.7);  /* 메인 코랄 색상 */
}

.delete-btn:hover {
  color: rgba(255, 103, 103, 0.9);
}

/* 잠금 아이콘 스타일 */
.locker-icon {
  color: rgb(173, 173, 173);
}

.locker-icon:hover {
  color: #666;
}

/* 수정/삭제 모드 토글 버튼 */
.mode-toggle {
  padding: 8px 15px;
  font-size: 13px;
  margin: 0 5px;
}

.mode-buttons {
  display: flex;
  justify-content: flex-end;
  gap: 15px;
  margin: 15px 0;
  padding: 0 5px;
}

.toggle-container {
  display: flex;
  align-items: center;
  gap: 8px;
}

.toggle-container span {
  font-size: 0.85rem;
  color: #666;
  font-weight: 600;
}

/* main.css에서 가져온 토글 버튼 스타일 */
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

.toggle-btn.active {
  background-color: rgba(255, 103, 103, 0.7);  /* 메인 코랄 색상으로 변경 */
}

.toggle-btn.active .toggle-circle {
  transform: translateX(15px);
}

</style>