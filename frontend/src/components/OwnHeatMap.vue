<template>
    <div class="grid-layout">
      <div class="grid-item">
      <div class="grid-sub" id="red">
        <h2 class="header">3</h2>
      </div>
        <h3>22.03</h3>
      </div>
      <div class="grid-item">
      <div class="grid-sub bg-lime-900" id="orange">
        <h2 class="header">2</h2>
      </div>
        <h3>23.03</h3>
      </div>
      <div class="grid-item">
      <div class="grid-sub" id="yellow">
        <h2 class="header">1</h2>
      </div>
        <h3>24.03</h3>
      </div>
      <div class="grid-item">
      <div class="grid-sub" id="green">
        <h2 class="header">0</h2>
      </div>
        <h3>25.03</h3>
      </div>
      <div class="grid-item">
      <div class="grid-sub" id="green">
        <h2 class="header">0</h2>
      </div>
        <h3>26.03</h3>
      </div>
    </div>
</template>
<script setup lang="ts">
import {GridLayout} from "vue3-grid-layout-next";

</script>
<style scoped>
h3 {
  margin-top: 5px;
}
.grid-item{
  color: white;
  flex-direction: column;
  display: flex;
  align-items: center;
}
.grid-layout{
  display: flex;
  flex-direction: row;
  margin: 0;
}
#green{
  background-color: #64a464;
}
#yellow{
  background-color: #efc63a;
}
#orange{
  background-color: #f5bd1e;
}
#red{
  background-color: #A84242;
}
.grid-sub {
  background-color: #f0f0f0;
  border: 3px solid #ffffff;
  padding: 10px;
  text-align: center;
  width: 120px;
  height: 120px;
  align-items: center;
  font-size: 2.0rem;
  display: flex;
  flex-direction: column;
}
.header{
  margin-top: 27%;
  text-align: center;
}
</style>
