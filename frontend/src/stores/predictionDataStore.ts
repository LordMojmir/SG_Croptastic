import {defineStore} from "pinia";

export const predictionDataStore = defineStore('predictionParams', {
    state: () => ({ plantDepth: 0, plantDensity: 0, rowSpacing: 0, waterCapacity: 0, isIrrigated: false }),
    getters: {},
    actions: {},
})