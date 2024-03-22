import {defineStore} from "pinia";

export const predictionDataStore = defineStore('predictionParams', {
    state: () => ({ plantDepth: 1, plantDensity: 4, rowSpacing: 20, waterCapacity: 1, isIrrigated: false }),
    getters: {},
    actions: {},
})