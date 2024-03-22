import {defineStore, storeToRefs} from "pinia";
import api from '@/api/api';
import axios, {formToJSON} from "axios";
import {useFeatureStore} from "@/stores/boundingBox";

const baseURl = "http://localhost:5000/";
const featureStore = useFeatureStore();
const {geometry, coordinates, centre} = storeToRefs(featureStore);
export const useSynApiStore = defineStore('synStore', {
    state: () => ({
        potatorisk: [{'2024/01/01 00:00:00': 1},{'2024/01/02 00:00:00': 3}, {'2024/01/03 00:00:00': 2}, {'2024/01/04 00:00:00': 2}, {'2024/01/05 00:00:00': 0}, {'2024/01/06 00:00:00': 4}, {'2024/01/07 00:00:00': 1}, {'2024/01/08 00:00:00': 2}, {'2024/01/09 00:00:00': 2}]

    }),
    actions: {
        fetchPotatoDiseaseRisk() {
            const params = {
                long: centre.value[0],
                lat: centre.value[1],
                relative_humidity: 60, // TODO get from Tobi
                start_date: '2024-03-21',
                end_date: '2024-03-28',
            };
            axios.get(baseURl + 'get_potato_disease_risk', { params })
                .then(response => {
                    console.log("response data " + response.data)
                    this.potatorisk = response.data;
                    console.log("this.potatorisk data " + this.potatorisk)
                })
                .catch(error => {
                    errorMessage.value = error.response?.data?.error || 'An unknown error occurred';
                });
        }
    },
});