<template>
  <div class="update-container">
    <h1>비밀번호 변경</h1>
    <p>새로운 비밀번호를 입력해주세요.</p>
    <form class="update-form" @submit.prevent="changePW">
      <div class="form-group">
        <label for="password1">New Password</label>
        <input type="password" id="password1" v-model.trim="password1">
      </div>
      <div class="form-group">
        <label for="password2">Confirm Password</label>
        <input type="password" id="password2" v-model.trim="password2">
      </div>
      <button type="submit" class="submit-button">비밀번호 변경하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie';

const store = useMovieStore()
const password1 = ref(null)
const password2 = ref(null)

const changePW = function(){
  const payload = {
    new_password1:password1.value,
    new_password2:password2.value,
  }
  store.changePassword(payload)
}
</script>

<style scoped>
.update-container {
  max-width: 500px;
  margin: 3rem auto;
  padding: 2.5rem;
  background: rgba(255, 255, 255, 0.85);
  border-radius: 25px;
  box-shadow: 0 8px 32px rgba(255, 103, 103, 0.1);
  backdrop-filter: blur(4px);
  border: 1px solid rgba(255, 255, 255, 0.4);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.update-container:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 36px rgba(255, 103, 103, 0.15);
}

h1 {
  color: rgba(34, 35, 36, 0.9);
  font-size: 1.8rem;
  font-weight: 600;
  margin-bottom: 1.2rem;
  text-align: center;
  letter-spacing: 0.5px;
}

p {
  text-align: center;
  color: rgba(84, 83, 83, 0.7);
  margin-bottom: 2rem;
  font-size: 0.95rem;
  line-height: 1.5;
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.6rem;
  margin-bottom: 1.2rem;
}

label {
  color: rgba(67, 64, 64, 0.8);
  font-weight: 500;
  font-size: 0.9rem;
  margin-left: 0.3rem;
}

input {
  width: 100%;
  padding: 0.9rem 1.2rem;
  border: 1px solid rgba(255, 103, 103, 0.2);
  border-radius: 15px;
  font-size: 0.95rem;
  background: rgba(255, 255, 255, 0.9);
  transition: all 0.3s ease;
}

input:focus {
  outline: none;
  border-color: rgba(255, 103, 103, 0.5);
  box-shadow: 0 0 0 3px rgba(255, 103, 103, 0.1);
  background: white;
}

.submit-button {
  width: 100%;
  background: rgba(255, 103, 103, 0.7);
  color: white;
  padding: 0.9rem;
  border: none;
  border-radius: 15px;
  font-size: 0.95rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 1rem;
  backdrop-filter: blur(4px);
}

.submit-button:hover {
  background: rgba(255, 103, 103, 0.85);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 103, 103, 0.2);
}

.delete-button {
  width: 100%;
  background: rgba(255, 103, 103, 0.7);
  color: white;
  padding: 0.9rem;
  border: none;
  border-radius: 15px;
  font-size: 0.95rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.3s ease;
  margin-top: 1.5rem;
  backdrop-filter: blur(4px);
}

.delete-button:hover {
  background: rgba(255, 103, 103, 0.85);
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(255, 103, 103, 0.2);
}

.warning-message {
  background: rgba(255, 103, 103, 0.08);
  padding: 1.2rem;
  border-radius: 15px;
  margin: 1.5rem 0;
  border: 1px solid rgba(255, 103, 103, 0.15);
}

.warning-message p {
  color: rgba(255, 103, 103, 0.8);
  margin: 0.5rem 0;
  font-size: 0.9rem;
  text-align: left;
  line-height: 1.6;
}

/* 애니메이션 효과 */
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.update-container {
  animation: fadeIn 0.6s ease-out;
}
</style>