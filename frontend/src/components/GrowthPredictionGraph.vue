
<script setup lang="ts">
import { useSynApiStore } from '@/stores/SynblahApiStore';
import { storeToRefs } from 'pinia';
import {useFeatureStore} from "@/stores/boundingBox";
import * as d3 from 'd3';
import {defineComponent, onMounted, ref} from 'vue'
import { Chart, Grid, Line } from 'vue3-charts'
import { CalendarHeatmap } from 'vue3-calendar-heatmap'
const store = useSynApiStore();
const storeRef = storeToRefs(store)
const parsedData = storeRef.potatorisk.value.map((item: any) => {
  let [date, value] = Object.entries(item)[0];
  let splits = date.split(" ")[0].replace("/", "-").replace("/", "-") //.split("/")
  //date = splits[2] + "/" + splits[1]
  return {date: splits, count: value}
})
console.log(parsedData)


/*export default defineComponent({
  name: 'LineChart',
  components: { Chart, Grid, Line , CalendarHeatmap},
  setup() {*/
   /* const storeRef = storeToRefs(store)
      let parsedData = storeRef.potatorisk.value.map((item: any) => {
        let [date, value] = Object.entries(item)[0];
        let splits = date.split(" ")[0] //.split("/")
        //date = splits[2] + "/" + splits[1]
        return {date: splits, value: value}
      })*/
   /*   console.log(parsedData)
      const direction = ref('horizontal')
      const margin = ref({
        left: 0,
        top: 20,
        right: 20,
        bottom: 0
      })*/

    // return { parsedData, direction, margin }
/*    <Chart
  :size="{ width: 500, height: 400 }"
  :data="parsedData"
  :margin="margin"
  :direction="direction"
    id="chart"
    >

    <template #layers>
    <Grid strokeDasharray="2,2" />
        <Line :dataKeys="['date', 'value']" />
        </template>

        </Chart>*/
/*
}
});
*/

</script>
<template>
  <div class="box" style="min-width: 600px; min-height: 600px">
    <calendar-heatmap :values="[{ date: '2018-9-22', count: 6 },{ date: '2018-9-23', count: 6 },{ date: '2018-9-24', count: 6 }]" :end-date="2018-9-24" />
  </div>
</template>
<style scoped>.d3-chart {
  overflow: visible;
}

Grid{
  stroke: #000;
  stroke-opacity: 0.2;
  color: white;
}
.chart{
  color: white;
  border: 1px solid red;
  padding: 1rem;
  margin: 1rem;
  border-radius: 1rem;
  overflow: visible;
}
</style>
