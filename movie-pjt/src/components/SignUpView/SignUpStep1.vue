<template>
    <div>
        <h1>아이디, 패스워드, 패스워드 확인</h1>
        <form>
            <input type="text" id="username" v-model="localForm.username" placeholder="ID">
            <br>
            <input type="password" id="password1" v-model="localForm.password1" placeholder="Password">
            <br>
            <input type="password" id="password2" v-model="localForm.password2" placeholder="Confirm Password">
            <br>
            <button @click="goNext">Next</button>
        </form>
    </div>
</template>

<script setup>
import { reactive, toRefs } from 'vue';


// 부모 컴포넌트에서 전달된 데이터
const props = defineProps(['formData']);
const emit = defineEmits(['update-data', 'next']);

// 로컬 상태로 데이터 복사
const localForm = reactive({
    username: props.formData.username,
    password1: props.formData.password1,
    password2: props.formData.password2,
});

// 다음 단계로 이동
const goNext = () => {
    emit('update-data', localForm); // 부모 컴포넌트로 데이터 전달
    emit('next'); // 다음 단계로 이동 이벤트
};
</script>

<style scoped>

</style>