<script setup lang="ts">
import "@eox/map"
import "@eox/timecontrol"
import {useFeatureStore} from "@/stores/boundingBox";

var geoJsonStore = useFeatureStore();
</script>

<template>
    <eox-map
        :zoom="6"
        :center="geoJsonStore.centre"
        :layers="[
        { type: 'Tile', properties: { id: 'Methane' }, source: { type: 'TileWMS', url: 'https://creodias.sentinel-hub.com/ogc/wms/afdf0697-ed64-430a-91c3-74b1749cf1f1', params: { LAYERS: 'METHANE', TIME: '2022-12-05' } } },
        { type: 'Tile', properties: { id: 'OSM' }, source: { type: 'OSM' } }
      ]"
        id="slider" style="width: 400px; height: 300px;"
    ></eox-map>
    <eox-timecontrol
        :for="'eox-map#slider'"
        :layer="'Methane'"
        :controlProperty="'TIME'"
        :controlValues='["2022-12-05", "2022-12-12", "2022-12-19", "2022-12-26", "2023-01-16", "2023-01-23", "2023-01-30", "2023-02-06", "2023-02-13", "2023-02-27", "2023-03-06", "2023-03-13", "2023-03-20", "2023-03-27", "2023-04-03", "2023-04-10", "2023-04-17", "2023-04-24"]'
        :slider="true"
    ></eox-timecontrol>
</template>


<style scoped>
.box {
  justify-content: center;
  background-color: #2b2a33;
  margin-right: 10vw;
  margin-left: 10vw;
  margin-top: 100px;
}
#slider {
  width: 400px;
  height: 400px;
  padding: 0.5rem;
}
</style>