import axios from "axios";

const baseURl = 'http://127.0.0.1:8000/api';

const axiosInstance = axios.create({
    baseURL: baseURl,
    timeout: 5000,
    headers: {
        Authorization: localStorage.getItem('access_token')
            ? 'Bearer ' + localStorage.getItem('access_token')
            : null,
    },
});

export default axiosInstance;