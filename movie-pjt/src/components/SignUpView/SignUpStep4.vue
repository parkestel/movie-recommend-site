<template>
    <div>
        <h1>학습 레벨</h1>
        <p>학습 레벨을 선택하지 않으면 자동으로 초급 단계가 됩니다.</p>
        <form>
            <select id="studylevel" v-model="localForm.studylevel">
                <option v-for="level in levels" :key="level">{{ level }}</option>
            </select>
            <br>
            <button @click="goPrevious">Back</button>
            <button @click.prevent="submit">Submit</button>
        </form>
    </div>
</template>

<script setup>
import { ref } from 'vue';
import { reactive } from 'vue';
const props = defineProps(['formData']);
const emit = defineEmits(['submit','previous']);

const levels = ref(['A1','A2','B1','B2','C1','C2'])

const localForm = reactive({
    studylevel: props.formData.study_level
});

// 이전 단계로 이동
const goPrevious = () => {
    emit('previous');
};

// 데이터 제출
const submit = () => {
    props.formData.study_level = localForm.studylevel
    emit('submit', props.formData); // 최종 데이터 전달
};
</script>

<style scoped>

</style>