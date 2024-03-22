<script setup lang="ts">
import "@eox/map"
import {onMounted, ref} from "vue";
import api from "@/api/bioDataClient"
import Chart from "chart.js/auto"

const coverPercentages = ref();
const showChart = ref(false);

onMounted(async () =>{
  const response = await api.get("/get_land_cover_percentages")
  if(response.status != 200){
    return
  }

  coverPercentages.value = response.data
  showChart.value = true;

  console.log(coverPercentages.value)
  console.log(Object.keys(coverPercentages.value))
  console.log(Object.values(coverPercentages.value))

  const colors = [
    'rgb(255, 184, 2)',    // Beaches and dunes (#ffb802)
    'rgb(255, 85, 0)',     // Corn (#ff5500)
    'rgb(255, 0, 255)',    // Dense built-up area (#ff00ff)
    'rgb(255, 85, 255)',   // Diffuse built-up area (#ff55ff)
    'rgb(170, 170, 0)',    // Grasslands (#aaaa00)
    'rgb(0, 156, 0)',      // Hardwood forest (#009c00)
    'rgb(255, 170, 255)',  // Industrial and commercial areas (#ffaaff)
    'rgb(170, 255, 0)',    // Natural grasslands and pastures (#aaff00)
    'rgb(255, 255, 0)',    // Oilseeds (Rapeseed) (#ffff00)
    'rgb(170, 170, 255)',  // Orchards and fruit growing (#aaaaff)
    'rgb(161, 214, 0)',    // Protein crops (Beans / Peas) (#a1d600)
    'rgb(0, 255, 255)',    // Roads (#00ffff)
    'rgb(0, 50, 0)',       // Softwood forest (#003200)
    'rgb(255, 171, 68)',   // Soy (#ffab44)
    'rgb(208, 255, 0)',    // Straw cereals (Wheat, Triticale, Barley) (#d0ff00)
    'rgb(214, 214, 0)',    // Sunflower (#d6d600)
    'rgb(170, 170, 97)',   // Tubers/roots (#aaaa61)
    'rgb(85, 0, 0)',       // Vineyards (#550000)
    'rgb(0, 0, 255)',      // Water (#0000ff)
    'rgb(85, 170, 127)'    // Woody moorlands (#55aa7f)
  ];

  console.log(colors);


  console.log(colors);



  new Chart(
      document.getElementById('landcoverChart'),
      {
        type: 'pie',
        data: {
          labels: Object.keys(coverPercentages.value),
          datasets: [
            {
              id: 'prediction',
              backgroundColor: colors,
              data: Object.values(coverPercentages.value),
              hoverOffset: 4,
            }
          ]
        },
        options: {
          plugins: {
            legend: {
              position: 'bottom',
              color: 'rgb(112,153,102)',
            }
          }
        },
        plugins: {
          title: 'Land usage'
        }
      }
  );

})

</script>

<template>
  <div class="w-[100%]">
    <div class="w-1/2">

    </div>
    <div class="w-1/2">
        <canvas style="width: 100%;" id="landcoverChart"></canvas>
    </div>
  </div>
</template>

<style scoped>

</style>