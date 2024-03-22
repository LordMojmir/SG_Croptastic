<script setup lang="ts">
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import {useFeatureStore} from "@/stores/boundingBox";
import {storeToRefs} from "pinia";
import {useSynApiStore} from "@/stores/SynblahApiStore";

const router = useRouter();
const {geometry, coordinates, centre} = storeToRefs(useFeatureStore());
const isClicked = ref(true); //TODO check if clicked (coordinates.value.length > 0


function navigateHome() {
  isClicked.value = true;
  setTimeout(() => {
    router.push('/');
    isClicked.value = false;
  }, 1000);
}

async function loadData(){
  const store = useSynApiStore();
  await store.fetchPotatoDiseaseRisk();

}
</script>

<template>
  <RouterLink v-if="isClicked" to="/dashboard"  @click="loadData">
    <button class="bg-primary-700 rounded-xl shadow-md px-3 py-2 text-text-100">Show graphs</button>
  </RouterLink>
</template>

<style scoped>
</style>




