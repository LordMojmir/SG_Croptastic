<script lang="ts" setup>
import {useFeatureStore} from "@/stores/boundingBox";
import "@eox/map"
import "@eox/drawtools"
import {storeToRefs} from "pinia";


/*async function updateCoordinates(newCoordinates :any) {
  try {
    console.log("POLYGON");
    console.log(newCoordinates);
    // TODO when the API is ready, replace the URL with the correct one
    const response = await axios.post('https://somerandomapi', { coordinates: newCoordinates });
    console.log(response.data);
    geoJsonStore.updateGeoJsonPolygon(newCoordinates);
  } catch (error) {
    console.error(error);
  }
}*/

const featureStore = useFeatureStore();
const {geometry, coordinates, centre} = storeToRefs(featureStore);

const handleDrawUpdate = ($event) => {
  const details = $event.detail;
  if (details.length > 0 && details[0].values_.geometry) {
    const newGeometry = details[0].values_.geometry;
    featureStore.updateGeometry(newGeometry);
  }
};

</script>
<template>
  <div class="box">
    <h1>Choose bounding box</h1>
    <eox-map id="primary" :center="centre"
             :layers='[{"type":"Tile","source":{"type":"OSM"}}]'></eox-map>

    <eox-drawtools
        for="eox-map#primary"
        type="Polygon"
        @drawupdate="handleDrawUpdate">

    </eox-drawtools>
  </div>
</template>

<style scoped>
.box {
  justify-content: center;
  margin-right: 10vw;
  margin-left: 10vw;
  margin-top: 100px;

#primary {
  width: 80vw;
  height: 300px;
  padding: 0.5rem;
}
</style>
