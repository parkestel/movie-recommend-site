<template>
  <div class="card">
    <div class="card-header">
      <div class="delete-button">
        <button v-if="showDelete" @click="deleteNote(note.movies[0].id)" class="emoji-button" >
          <font-awesome-icon :icon="['fas', 'trash-can']" /> 
        </button>
      </div>
      <div v-if="userProfile.username===store.logedinUsername">
        <button v-if="note.is_public" @click="togglePublic(note.movies[0].id)" class="emoji-button">
          <font-awesome-icon :icon="['fas', 'lock-open']" class="locker-icon"/>
        </button>
        <button v-else @click="togglePublic(note.movies[0].id)" class="emoji-button">
          <font-awesome-icon :icon="['fas', 'lock']" class="locker-icon" />
        </button>
      </div>
    </div>
    <h5>{{ note.movies[0].title }}</h5>
    <button @click="popUp(note.id)" class="btn">show my note</button>
  </div>
</template>

<script setup>
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';
import { useMovieStore } from '@/stores/movie';
import { storeToRefs } from 'pinia';
const store = useMovieStore()
const { userProfile } = storeToRefs(store)


defineProps({
  note:Object,
  showDelete:Boolean
})

const emit = defineEmits(['deleteEvent', 'toggleEvent'])

const popUp = function (noteId) {
  window.open(`/note/${noteId}?isPopup=true`, '__blank', 'width=400,height=650')
}

const deleteNote = function (movieId, userId = userProfile.value.id) {
  const result = window.confirm('Really????')
  if (result) {
    emit('deleteEvent', movieId, userId)
  } else {
    return null
  }
}

const togglePublic = function (movieId, userId = userProfile.value.id) {
  emit('toggleEvent', movieId, userId)
}
</script>

<style scoped>
.card {
  background: rgba(255, 255, 255, 0.85);  /* 배경 투명도 조정 */
  border: 1px solid rgba(40, 44, 52, 0.2);
  border-radius: 15px;
  padding: 15px;
  margin: 15px 0;
  box-shadow: 0 4px 12px rgba(40, 44, 52, 0.15);
  backdrop-filter: blur(8px);  /* 블러 효과 추가 */
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-2px);
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 6px 20px rgba(40, 44, 52, 0.2);
}

.card-header {
  position: relative;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0 8px;
  margin-bottom: 10px;
  background-color: transparent;
  border: none;
}

h5 {
  font-size: 1.2rem;
  font-weight: 750;
  color: #282c34;
  margin: 8px 0;
  text-align: center;
}

.btn {
  width: 100%;
  padding: 10px;
  background: rgba(40, 44, 52, 0.1);
  color: #282c34;
  border: 1px solid rgba(40, 44, 52, 0.2);
  border-radius: 12px;
  font-weight: 600;
  backdrop-filter: blur(8px);
  transition: all 0.3s ease;
  margin-top: 8px;
}

.btn:hover {
  background: rgba(40, 44, 52, 0.15);
  transform: translateY(-1px);
  color: #1a1a1a;
}

.emoji-button {
  background: transparent;
  border: none;
  padding: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  color: rgba(40, 44, 52, 0.6);
}

.emoji-button:hover {
  color: #282c34;
  transform: scale(1.1);
}

.delete-button .emoji-button {
  color: rgba(255, 103, 103, 0.7);  /* 메인 코랄 색상 활용 */
}

.delete-button .emoji-button:hover {
  color: rgba(255, 103, 103, 0.9);
}

.card-header .delete-button,
.card-header .locker-icon {
  /* flexbox로 정렬 */
  display: flex;
  align-items: center;

  /* 동일한 높이와 간격 확보 */
  margin: 0 8px;
}

.card-header .locker-icon {
  color: rgb(173, 173, 173);
}

.delete-button {
  background-color: transparent;
  border: none;
  cursor: pointer;
}

</style>