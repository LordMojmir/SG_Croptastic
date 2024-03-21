<script setup lang="ts">
import "@eox/map"
import "@eox/drawtools"
import { ref, watch } from "vue";
import axios from "axios"; // Make sure to install axios for API calls

let coordinates = ref([]);
let drawnFeatures = ref([]);

async function updateCoordinates(newCoordinates :any) {
  try {
    console.log("POLYGON")
    console.log(newCoordinates)
    // TODO when the API is ready, replace the URL with the correct one
    const response = await axios.post('https://somerandomapi', { coordinates: newCoordinates });
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

watch(drawnFeatures, (newVal, oldVal) => {
  coordinates.value = newVal;
  updateCoordinates(newVal);
}, { deep: true });
</script>

<template>
  <div class="box">
    <h1 class="text-text-200">Choose bounding box</h1>
    <eox-map :layers='[{"type":"Tile","source":{"type":"OSM"}}]' id="primary" class="shadow-2xl"></eox-map>

    <eox-drawtools
        type="Polygon"
        for="eox-map#primary"
        @drawupdate="drawnFeatures = $event.detail"
        v-model:coordinates="coordinates">
    </eox-drawtools>
  </div>
</template>

<style scoped>
.box {
  justify-content: center;
  margin-right: 10vw;
  margin-left: 10vw;
  margin-top: 100px;
}
#primary {
  width: 80vw;
  height: 300px;
  padding: 0.5rem;
}
</style>
