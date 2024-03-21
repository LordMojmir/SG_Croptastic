<script lang="ts" setup>
import {useFeatureStore} from "@/stores/boundingBox";
import "@eox/map"
import "@eox/drawtools"
import {storeToRefs} from "pinia";
import ButtonComponent from "@/components/ButtonComponent.vue";


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

const handleDrawUpdate = ($event :any) => {
  const details = $event.detail;
  if (details.length > 0 && details[0].values_.geometry) {
    const newGeometry = details[0].values_.geometry;
    featureStore.updateGeometry(newGeometry);
  }
};

</script>
<template>
  <div class="box">
    <div class="flex">
      <h1>Choose your bounding box</h1>
#        <ButtonComponent />
      <eox-drawtools
          for="eox-map#primary"
          class="text-4xl"
          type="Polygon"
          style="font-size: 10rem !important;"
          @drawupdate="handleDrawUpdate"
          id="drawtools"
          ref="vacRef"
      >

      </eox-drawtools>
    </div>
    <eox-map id="primary" :center="centre"
             :layers='[{"type":"Tile","source":{"type":"OSM"}}]'></eox-map>
    </div>
</template>

<style scoped>

.box {
  justify-content: center;
  margin-right: 5vw;
  margin-left: 5vw;
  margin-top: 100px;
  display: flex;
  width: 90vw;
}
#primary {
  width: 50vw;
  height: 70vh;
  padding: 0.5rem;
}
h1 {
  background-color: transparent;
  color: #fff;
    flex: 2;
    text-align: left;
    font-size: 3rem;
    font-weight: bold;
    text-transform: uppercase;
    letter-spacing: 0.15rem;
  align-content: center;
  align-self: center;

}
.flex{
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100%; /* This will make the container take the full height of the viewport */
  text-align: center;
  margin-top: 15%;
  margin-left: 4rem;
  margin-right: 5vw;

}
 .icon{
   width: 40px !important;
   min-width: 40px !important;
   font-size: 32px !important;
 }
/* #drawtools{
    width: 100% !important;
    min-width: 300px !important;
    font-size: 32px !important;
 }

#drawtools button.discard:before {
   min-width: 25px !important;
    width: 40px !important;
  font-size: 14rem !important;
  color: black;
 }
eox-drawtools {
  --button-size: 20px; !* Example custom property, adjust based on actual API *!
  --button-padding: 10px 20px; !* Assuming the component supports these *!
}
button {
  width: 40px !important;
  min-width: 40px !important;
}*/
</style>
