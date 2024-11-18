<template>
    <div>
        <h1>성, 이름, 이메일, 생년월일</h1>
        <form>
            <input type="text" id="lastname" v-model="localForm.lastname" placeholder="Last Name">
            <br>
            <input type="text" id="firstname" v-model="localForm.firstname" placeholder="First Name">
            <br>
            <input type="email" id="email" v-model="localForm.email" placeholder="Email">
            <br>
            <input type="date" id="birth" v-model="localForm.birth">
            <br>
            <button @click="goPrevious">Back</button>
            <button @click="goNext">Next</button>
        </form>
    </div>
</template>

<script setup>
import { reactive } from 'vue';
const props = defineProps(['formData']);
const emit = defineEmits(['update-data', 'previous']);

const localForm = reactive({
  email: props.formData.email,
  firstname: props.formData.firstname,
  lastname: props.formData.lastname,
  brith: props.formData.birth
});

const goPrevious = () => {
  emit('previous');
};

// 다음 단계로 이동
const goNext = () => {
    emit('update-data', localForm); // 부모 컴포넌트로 데이터 전달
    emit('next'); // 다음 단계로 이동 이벤트
};
</script>

<style scoped>

</style>