<template>
    <div>
        <component :is="currentStep" 
        @next="goToNextStep" 
        @previous="goToPreviousStep"
        @updateData="updateFormData"
        :form-data="formData"/>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import SignUpStep1 from '@/components/SignUpView/SignUpStep1.vue';
import SignUpStep2 from '@/components/SignUpView/SignUpStep2.vue';
import SignUpStep3 from '@/components/SignUpView/SignUpStep3.vue';
import SignUpStep4 from '@/components/SignUpView/SignUpStep4.vue';

const steps = [SignUpStep1, SignUpStep2, SignUpStep3, SignUpStep4]
const currentStepIndex = ref(0)

// 단계별 입력 데이터 저장
const formData = ref({
    username:'',
    password1:'',
    password2:'',
    email:'',
    lastname:'',
    firstname:'',
    birth:'',
    nickname:'',
    studylevel:''
})

// 현재 컴포넌트
const currentStep = computed(() => steps[currentStepIndex.value])

// 다음 단계 이동
const goToNextStep = function (){
    if (currentStepIndex.value < steps.length -1){
        currentStepIndex.value++
    }
}

// 이전 단계로 이동
const goToPreviousStep = function () {
    if (currentStepIndex.value > 0) {
        currentStepIndex.value--
    }
}

// 데이터 업데이트
const updateFormData = function (newData) {
    formData.value = {...formData.value, ...newData}
}
</script>

<style scoped>

</style>