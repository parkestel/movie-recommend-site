<template>
    <div>
        <h1>내가 쓴 리뷰들</h1>
        <div class="review-container">
            <MyReviewList :my-reviews="myReviews" class="review-box"/>
        </div>
    </div>
</template>

<script setup>
import MyReviewList from '@/components/MyReviewView/MyReviewList.vue'
import { useMovieStore } from '@/stores/movie';
import { onMounted } from 'vue';
import { storeToRefs } from 'pinia';

const store = useMovieStore()
const {myReviews} = storeToRefs(store)

onMounted(()=>{
    store.getMyReviews()
})
</script>

<style scoped>
.review-container {
    max-width: 800px; /* 적당한 너비 */
    margin: 0 auto; /* 중앙 정렬 */
    padding: 20px;
    background-color: transparent /* 부드러운 배경색 */

}
.review-box {
    display: flex;
    flex-direction: column; /* 세로 정렬 */
    gap: 15px; /* 아이템 간격 */
}

</style>