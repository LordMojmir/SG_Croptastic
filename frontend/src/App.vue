<script setup lang="ts">
  import BoundingBoxMap from "@/components/BoundingBoxMap.vue";
  import HeaderComponent from "@/components/HeaderComponent.vue";
</script>

<template>
  <HeaderComponent></HeaderComponent>
  <BoundingBoxMap></BoundingBoxMap>
  <RouterLink to="/playground">
    <button class="bg-primary-700 rounded-xl shadow-md px-3 py-2 text-text-100">Go to playground</button>
  </RouterLink>
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

