<script setup lang="ts">
import "@eox/map"
import "@eox/timecontrol"
import {computed, ref} from "vue";
import { predictionDataStore } from "@/stores/predictionDataStore"
import GrowthPredictionGraph from "@/components/GrowthPredictionGraph.vue";
import {useFeatureStore} from "@/stores/boundingBox"
import {storeToRefs} from "pinia";
import bioDataClient from "@/api/bioDataClient";

const parametersStore = predictionDataStore();
const refParameters = storeToRefs(parametersStore);

const geoDataStore = useFeatureStore();

let data;

const showPredictions = ref(false);

async function getData(){
  showPredictions.value = false;
  const response = await bioDataClient.get('/get_crop_development', {
    params: {
      long: "" + geoDataStore.centre[0],
      lat:  "" + geoDataStore.centre[1],
      depth_val: refParameters.plantDepth.value,
      density_val: refParameters.plantDensity.value,
      row_spacing_val: refParameters.rowSpacing.value,
      field_water_capacity_val: refParameters.waterCapacity.value,
    }
  });
  if(response.status == 200){
    data = response.data;
    showPredictions.value = true;
  }
}
</script>

<template>

  <div class="w-[100%] flex flex-growth p-3 gap-2">
    <div class="w-2/3 h-max">
      <eox-map :layers='[{"type":"Tile","source":{"type":"OSM"}}]' id="primary" class="h-80 w-full"></eox-map>
    </div>
    <div class="grid grid-cols-3 items-center gap-4 text-gray-100 w-1/3 justify-between mr-0 m-auto p-2 text-text-300 content-center">
      <label for="plantDepth">Plant Depth (cm)</label>
      <input type="range" min="1" max="9" v-model="refParameters.plantDepth.value" class="w-full fill-accent-500 rounded-full" name="plantDepth">
      <p>{{ refParameters.plantDepth.value }}cm</p>
      <label for="plantDensity">Plant Density (plants/m²)</label>
      <input type="range" min="4.0" max="14" step="0.1" v-model="refParameters.plantDensity.value" class="slider" name="plantDensity">
      <p>{{ refParameters.plantDensity.value }}cm</p>
      <label for="rowSpacing">Row Spacing (cm)</label>
      <input type="range" min="20" max="100" v-model="refParameters.rowSpacing.value" class="slider" name="rowSpacing">
      <p>{{ refParameters.rowSpacing.value }}cm</p>
      <label for="waterCapacity">Water Capacity (%)</label>
      <input type="range" min="1" max="100" v-model="refParameters.waterCapacity.value" class="slider" name="waterCapacity">
      <p>{{ refParameters.waterCapacity.value }}%</p>
      <div></div>
      <button class="bg-primary-700 rounded-xl shadow-md px-3 py-2 text-text-100"
       @click="getData"
      >Try it out!</button>
    </div>
  </div>
  <GrowthPredictionGraph v-if="showPredictions" :data="data" ></GrowthPredictionGraph>

</template>

<style scoped>

</style>