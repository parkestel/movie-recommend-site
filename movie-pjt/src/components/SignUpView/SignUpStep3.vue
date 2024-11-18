<template>
    <div>
        <h1>닉네임</h1>
        <form>
            <input type="text" id="nickname" v-model="localForm.nickname" placeholder="Nickname">
            <br>
            <button @click="goPrevious">Back</button>
            <button @click="goNext">Next</button>
        </form>
    </div>
</template>

<script setup>
import { reactive } from 'vue';
const props = defineProps(['formData']);
const emit = defineEmits(['update-data','next', 'previous']);

const localForm = reactive({
    nickname: props.formData.nickname
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