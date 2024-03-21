<template>

  <BoundingBoxMap></BoundingBoxMap>
  <RouterLink to="/playground">
    <button class="bg-primary-700 rounded-xl shadow-md px-3 py-2 text-text-100">Go to playground</button>
  </RouterLink>

</template>
<script setup lang="ts">
import BoundingBoxMap from "@/components/BoundingBoxMap.vue";
</script>