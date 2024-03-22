<script setup lang="ts">
import {onMounted} from "vue";
import Chart from 'chart.js/auto'

const props = defineProps({
  data: []
});

onMounted(() => {

  const data = props.data || []
  if(data.length == 0){
    return
  }
  const cleanData = data.filter(row => row[0] != 'E')
  let labels = [];
  for(let i = 0; i < cleanData[cleanData.length - 1][1]; i++){
    labels.push(i);
  }
  const filledData = [];
  let previousLevel = data[0][0];
  for (let day = 0; day <= cleanData[cleanData.length - 1][1]; day++) {
    let value = previousLevel;
    for (let i = 0; i < cleanData.length; i++) {
      if (cleanData[i][1] === day) {
        value = cleanData[i][0];
      }
    }
    filledData.push([value, day]);
    previousLevel = value;
  }

  console.log(labels)

  new Chart(
      document.getElementById('growthPredictionGraph'),
      {
        type: 'line',
        data: {
          labels: filledData.map(row => row[1]),
          datasets: [
            {
              id: 'prediction',
              data: filledData.map(row => row[0]),
              borderColor: '#8bac86'
            }
          ]
        },
        options: {
          plugins: {
            legend: {
              display: false
            }
          },
          scales:{
            x: {
              border: {
                color: '#537974'
              },
              title: {
                text: 'Days predicted'
              },
            },
            y: {
              border: {
                color: '#537974'
              },
              ticks: {
                min: 0,
                max: 12
              }
            }
          }
        }
      }
  );


})
</script>

<template>
  <div style="width: 50vw; height: 50vh;">
    <canvas id="growthPredictionGraph"></canvas>
  </div>

</template>