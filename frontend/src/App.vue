<script setup lang="ts">
  import BoundingBoxMap from "@/components/BoundingBoxMap.vue";
  import HeaderComponent from "@/components/HeaderComponent.vue";
  import CropGrowthComponent from "@/components/CropGrowthComponent.vue";
  import HomeView from "@/views/HomeView.vue";
</script>

<template>
  <HeaderComponent></HeaderComponent>
  <RouterView />
</template>

<style>
  body {
    font-family: "JetBrains Mono", sans-serif;
    margin: 0;
    padding: 0;
    background-color: var(--background-950);
  }
  h1 {
    background-color: transparent;
    color: #fff;
  }
</style>

