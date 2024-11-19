<template>
  <div>
    <h5>My Voca Note Page</h5>
    <VocaNoteItem
    v-for="note in vocaNoteList"
    :key="note.id"
    :note="note"/>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";
import VocaNoteItem from '@/components/VocaNoteView/VocaNoteItem.vue'

const router = useRouter()
const noteId = ref(null)

const vocaNoteList = ref([
  {id:1, movie: 'Toy Story', is_public: true}
])

</script>

<style scoped>

</style>