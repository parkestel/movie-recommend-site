<template>
  <div>
      <h1>회원 정보 변경</h1>
      <form @submit.prevent="updateInfo(userInfo)">
          <input type="text" id="lastname" v-model="userInfo.last_name" placeholder="Last Name">
          <br>
          <input type="text" id="firstname" v-model="userInfo.first_name" placeholder="First Name">
          <br>
          <input type="email" id="email" v-model="userInfo.email" placeholder="Email">
          <br>
          <input type="date" id="birth" v-model="userInfo.birth">
          <br>
          <input type="text" id="nickname" v-model="userInfo.nickname" placeholder="Nickname">
          <br>
          <input type="submit" value="확인">
      </form>
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie';
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { storeToRefs } from 'pinia';

const store = useMovieStore()
const route = useRoute()
const { userInfo } = storeToRefs(store)

const updateInfo = function(payload, username=route.params.username) {
  store.updateUserInfo(payload, username)
}

onMounted(()=>{
  store.getUserInfoForUpdate()
})
</script>

<style scoped>

</style>