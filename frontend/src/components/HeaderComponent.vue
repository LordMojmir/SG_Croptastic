<script setup lang="ts">

</script>

<template>
  <header class="header">
    <h1 class="title">Croptastic</h1>
    <img src="../assets/logo.png" alt="Croptastic logo" class="w-24 h-24">
  </header>
</template>

<style scoped>
.header {
  display: flex;
  padding: 1rem
  align-items: center;
  background-color: var(--background-700);
  justify-content: space-between;
  color: #fff;
}

.logo {
  display: flex;
  flex: 1;
}

.logo img {
  height: 7rem;
  text-align: right;
  margin-right: 0;
}

.title {
  flex: 2;
  text-align: left;
  font-size: 2rem;
  font-weight: bold;
  text-transform: uppercase;
  letter-spacing: 0.15rem;
  padding-left: 2rem;
}
</style>