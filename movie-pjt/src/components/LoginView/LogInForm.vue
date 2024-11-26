<template>
    <div class="login-container">
      <h1>로그인</h1>
      <p>다시 만나서 반가워요!</p>
      <form @submit.prevent="logIn" class="login-form">
        <div class="form-group">
          <label for="username">ID</label>
          <input
            type="text"
            id="username"
            v-model.trim="username"
            placeholder="username"
            required
          />
        </div>
        <div class="form-group">
          <label for="password">Password</label>
          <input
            type="password"
            id="password"
            v-model.trim="password"
            placeholder="••••••••"
            required
          />
        </div>
        <div class="options">
          <a href="#" class="forgot-password">Forgot Password</a>
        </div>
        <button type="submit" class="submit-button">Log in</button>
      </form>
    </div>
  </template>
  

<script setup>
import { ref } from 'vue';
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

const username = ref(null)
const password = ref(null)

const logIn = function () {
    const payload = {
        username: username.value,
        password: password.value
    }
    store.logIn(payload)
}
</script>

<style scoped>
.login-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100vh;
  font-family: Arial, sans-serif;
  background: transparent;
  padding-bottom: 400px;
}

h1 {
  font-family: 'NanumSquareRoundEB', sans-serif !important;
  /* font-size: 2rem; */
  margin-bottom: 0.5rem;
}

p {
  margin-bottom: 1.5rem;
  color: rgba(26, 25, 25, 0.8);
  font-family: 'NanumSquareRound';
}

.login-form {
  background: rgba(0, 0, 0, 0.7);
  padding: 2rem;
  border-radius: 10px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
  width: 90%;
  max-width: 400px;
  border-radius: 2rem; /* 둥근 모서리 */
}

.form-group {
  margin-bottom: 1rem;
}

label {
  display: block;
  font-size: 0.9rem;
  margin-bottom: 0.3rem;
  color: rgba(255, 255, 255, 0.8);
}

input[type="text"],
input[type="password"] {
  width: 100%;
  padding: 0.8rem;
  border: none;
  border-radius: 5px;
  background: #333;
  color: #fff;
  font-size: 1rem;border-radius: 2rem; /* 둥근 모서리 */
}

input[type="email"]::placeholder,
input[type="password"]::placeholder {
  color: rgba(255, 255, 255, 0.6);
}

.options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 1.5rem;
  font-size: 0.8rem;
}

.forgot-password {
  color: #ff8a80;
  text-decoration: none;
  margin-left: auto;
}

.forgot-password:hover {
  text-decoration: underline;
}

.submit-button {
  width: 100%;
  padding: 0.8rem;
  background: linear-gradient(to right, #ff8a80, #ff6e7f);
  border: none;
  border-radius: 5px;
  color: #fff;
  font-size: 1rem;
  cursor: pointer;
  transition: background 0.3s;
  border-radius: 2rem; /* 둥근 모서리 */
}

.submit-button:hover {
  background: linear-gradient(to right, #ff6e7f, #ff8a80);
}
</style>