<script setup lang="ts">
import "@eox/map"
import "@eox/timecontrol"
import {computed, ref} from "vue";

const plantDepth = ref(10);
const plantDensity = ref(1);
const rowSpacing = ref(23);
const waterCapacity = ref(89);
const isIrrigated = ref(false);

</script>

<template>

  <div class="w-[100%] flex flex-growth p-3 gap-2">
    <div class="w-2/3 h-max">
      <eox-map :layers='[{"type":"Tile","source":{"type":"OSM"}}]' id="primary" class="h-80 w-full"></eox-map>
    </div>
    <div class="grid grid-cols-3 items-center gap-4 text-gray-100 w-1/3 justify-between mr-0 m-auto p-2 text-text-300 content-center">
      <label for="plantDepth">Plant Depth</label>
      <input type="range" min="1" max="100" v-model="plantDepth" class="w-full fill-accent-500 rounded-full" name="plantDepth">
      <p>{{ plantDepth }}</p>
      <label for="plantDensity">Plant Density</label>
      <input type="range" min="1" max="100" v-model="plantDensity" class="slider" name="plantDensity">
      <p>{{plantDensity}}</p>
      <label for="rowSpacing">Row Spacing</label>
      <input type="range" min="1" max="100" v-model="rowSpacing" class="slider" name="rowSpacing">
      <p>{{ rowSpacing }}</p>
      <label for="waterCapacity">Water Capacity</label>
      <input type="range" min="1" max="100" v-model="waterCapacity" class="slider" name="waterCapacity">
      <p>{{ waterCapacity }}</p>
      <label for="isIrrigated">Water crops: </label>
      <input type="checkbox" name="isIrrigated" v-model="isIrrigated" class="rounded-2xl">
      <div></div>
      <button class="bg-primary-700 rounded-xl shadow-md px-3 py-2 text-text-100">Try it out!</button>
    </div>

  </div>

</template>

<style scoped>

</style>