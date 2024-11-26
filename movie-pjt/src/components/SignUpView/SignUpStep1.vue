<template>
    <div class="signup-container">
        <h1>회원가입</h1>
        <p>아이디, 패스워드를 입력해 주세요.</p>
        <form class="signup-form">
            <div class="form-group">
              <label for="username">ID</label>
              <input type="text" id="username" v-model="localForm.username" placeholder="ID">
              <br>
            </div>
            <div class="form-group">
              <label for="username">PASSWORD</label>
              <input type="password" id="password1" v-model="localForm.password1" placeholder="Password">
              <br>
            </div>
            <div class="form-group">
              <label for="username">CONFIRM PASSWORD</label>
              <input type="password" id="password2" v-model="localForm.password2" placeholder="Confirm Password">
              <br>
            </div>
            <div class="button-wrapper">
                <button class="submit-button" @click="goNext">Next</button>
            </div>
            <p class="login-text">
                이미 계정이 있으신가요? 
                <a @click="navigateToLogin" class="login-link">로그인</a>
            </p>
        </form>
    </div>
</template>

<script setup>
import { reactive, toRefs } from "vue";
import { useRouter } from 'vue-router';
import "@/assets/styles/signup.css";

const router = useRouter();
const props = defineProps(["formData"]);
const emit = defineEmits(["update-data", "next"]);

// 로그인 페이지로 이동
const navigateToLogin = () => {
    router.push('/login');
}

// 로컬 상태로 데이터 복사
const localForm = reactive({
  username: props.formData.username,
  password1: props.formData.password1,
  password2: props.formData.password2,
});

// 다음 단계로 이동
const goNext = () => {
  emit("update-data", localForm); // 부모 컴포넌트로 데이터 전달
  emit("next"); // 다음 단계로 이동 이벤트
};
</script>

<style scoped>
p {
    margin-bottom: 1.5rem;
    color: rgba(84, 83, 83, 0.8);
    font-family: 'NanumSquareRound';
}

input[type="text"],
input[type="password"],
input[type="email"],
input[type="date"] {
    width: 100%;
    padding: 0.8rem;
    border: none;
    background: #333;
    color: #fff;
    font-size: 1rem;
    border-radius: 2rem;
    /* 둥근 모서리 */
}

label {
    color: rgba(255, 255, 255, 0.6);
    margin: 0.3rem;
}

h1 {
  font-family: 'NanumSquareRoundEB', sans-serif !important;
}

.login-text {
    text-align: center;
    margin-top: 1rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: rgba(255, 255, 255, 0.7);
    font-family: 'NanumSquareRound';
}

.login-link {
    color: var(--point-peach);
    text-decoration: none;
    cursor: pointer;
    font-weight: 600;
    transition: color 0.3s ease;
}

.login-link:hover {
    color: var(--point-rose);
}

/* 반응형 디자인 */
@media (max-width: 768px) {
    .button-wrapper {
        margin-top: 1.5rem;
    }
    
    .login-text {
        font-size: 0.85rem;
        margin-top: 0.8rem;
        margin-bottom: 0.8rem;
    }
}

@media (min-width: 1440px) {
    .button-wrapper {
        margin-top: 2.5rem;
    }
    
    .login-text {
        font-size: 1rem;
        margin-top: 1.2rem;
        margin-bottom: 1.2rem;
    }
}

.form-group {
    margin-bottom: 1.2rem;
}

.button-wrapper {
    margin-top: 2rem;
    margin-bottom: 0.5rem;
}
</style>
