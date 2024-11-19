<template>
    <div>
        <h1>학습 레벨</h1>
        <p>학습 레벨을 선택하지 않으면 자동으로 초급 단계가 됩니다.</p>
        <form>
            <select id="studylevel" v-model="localForm.studylevel">
                <option v-for="level in levels">{{ level }}</option>
            </select>
            <br>
            <button @click="goPrevious">Back</button>
            <button @click="submit">Submit</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { reactive } from 'vue';
const props = defineProps(['formData']);
const emit = defineEmits(['update-data','previous']);

const levels = ref(['Lv1','Lv2','Lv3','Lv4','Lv5','Lv6'])

const localForm = reactive({
    studylevel: props.formData.studylevel
});

// 이전 단계로 이동
const goPrevious = () => {
    emit('previous');
};

// 데이터 제출
const submit = () => {
    emit('update-data', localForm); // 최종 데이터 전달
    alert('mission completed!');
};
</script>

<style scoped>

</style>