import {defineStore} from 'pinia';
import {fromLonLat} from 'ol/proj';
import Point from 'ol/geom/Point';


export const useFeatureStore = defineStore('feature', {
    state: () => ({
        geometry: null,
        coordinates: [],
        centre: [17.06667, 47.93333]
    }),
    actions: {
        updateGeometry(newGeometry) {
            this.geometry = newGeometry;
            this.coordinates = newGeometry.flatCoordinates;
            this.centre = findPolygonCenter(this.coordinates);
        },
    },
});

function calculatePolygonCenter(coordsArray: number[]): [number, number] {
    let centroid = [0, 0];
    let numPoints = coordsArray.length / 2; // Since the array is flat

    for (let i = 0; i < coordsArray.length; i += 2) {
        centroid[0] += coordsArray[i];     // Longitude
        centroid[1] += coordsArray[i + 1]; // Latitude
    }

    centroid[0] /= numPoints;
    centroid[1] /= numPoints;

    return [centroid[0], centroid[1]]; // Returns [longitude, latitude]
}

function findPolygonCenter(coordsArray: number[]): Point {
    return calculatePolygonCenter(coordsArray);
}


