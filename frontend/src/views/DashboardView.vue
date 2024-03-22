<script setup lang="ts">

import CropGrowthComponent from "@/components/CropGrowthComponent.vue";
import SentinelPicDash from "@/components/SentinelPicDash.vue";
import GrowthPredictionGraph from "@/components/GrowthPredictionGraph.vue";
import HeaderComponent from "@/App.vue";
import OwnHeatMap from "@/components/OwnHeatMap.vue";
</script>
<template>
  <div class="main-class">
  <CropGrowthComponent></CropGrowthComponent>
  <SentinelPicDash></SentinelPicDash>
    <OwnHeatMap></OwnHeatMap>
  </div>
</template>
<style>
.main-class{
  width: 100vw;
}
</style>