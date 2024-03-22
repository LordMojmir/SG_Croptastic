<script setup lang="ts">

import CropGrowthComponent from "@/components/MethaneDetectionomp.vue";
import SentinelPicDash from "@/components/SentinelPicDash.vue";
import GrowthPredictionGraph from "@/components/GrowthPredictionGraph.vue";
import HeaderComponent from "@/App.vue";
import OwnHeatMap from "@/components/OwnHeatMap.vue";
import ClimateImpact from "@/components/ClimateImpact.vue";
import MoisturizerComp from "@/components/MoisturizerComp.vue";
</script>
<template>
  <div class="main-class">
  <CropGrowthComponent></CropGrowthComponent>
  <SentinelPicDash></SentinelPicDash>
    <OwnHeatMap></OwnHeatMap>
    <ClimateImpact></ClimateImpact>
    <MoisturizerComp></MoisturizerComp>
  </div>
</template>
<style>
.main-class{
  width: 100vw;
}
</style>