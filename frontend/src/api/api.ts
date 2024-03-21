import axios from "axios";

const api = axios.create({
    baseURL: import.meta.env.VITE_BASE_URL,
    headers: {
        'Bearer': import.meta.env.VITE_AUTH_TOKEN
    }  
})

export default api;