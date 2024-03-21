<script setup lang="ts">
import {useFeatureStore} from "@/stores/boundingBox";
import "@eox/map"
import {storeToRefs} from "pinia";
const featureStore = useFeatureStore();
const {geometry, coordinates, centre} = storeToRefs(featureStore);
import "@eox/map/dist/eox-map-advanced-layers-and-sources.js"
import "@eox/map/dist/eox-map.js"
/*  <eox-map-compare
      :layers='[{"type":"Tile","source":{"type":"TileWMS","url":"https://creodias.sentinel-hub.com/ogc/wms/afdf0697-ed64-430a-91c3-74b1749cf1f1","params":{"LAYERS":"AWS_VIS_WIND_V_10M"}}}]'
      >
    <eox-map slot="first" id="compareA"></eox-map>
    <eox-map slot="second" sync="eox-map#compareA"></eox-map>
    </eox-map-compare>*/
</script>
<template>
  <eox-map
      :zoom="12"
      :center="centre"
      :layers="[
        { type: 'Tile', properties: { id: 'NATURAL-COLOR' }, source: { type: 'TileWMS', url: 'https://services.sentinel-hub.com/ogc/wms/afdf0697-ed64-430a-91c3-74b1749cf1f1', params: { LAYERS: 'TRUE-COLOR-S2L2A', TIME: '2024-01-20/2024-01-21', WIDTH:'50', HEIGHT: '50', MAXCC: '20' } } }
      ]"
      class="map"
   style="width: 400px; height: 300px;"

  ></eox-map>


</template>

<style>
#primary {
  width: 50vw;
  height: 70vh;
  padding: 0.5rem;
}

 .map{
   width: 400px;
   height: 400px;
   padding: 0.5rem;
 }
</style>
