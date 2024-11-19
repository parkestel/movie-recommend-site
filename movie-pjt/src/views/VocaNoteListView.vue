<template>
  <div>
    <h5>My Voca Note Page</h5>
    <VocaNoteItem
    v-for="note in store.vocaNoteList"
    :key="note.id"
    :note="note"/>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import VocaNoteItem from '@/components/VocaNoteView/VocaNoteItem.vue'
import { useMovieStore } from "@/stores/movie";

const router = useRouter()
const store = useMovieStore()

</script>

<style scoped>

</style>