import React, {useEffect} from 'react'
import axiosInstance from '../axios'

export default function LogOut() {
    
    useEffect(() => {
        axiosInstance.post('user/logout/', {
            refresh_token: localStorage.getItem('refresh_token'),
        })
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        localStorage.removeItem('user')
        axiosInstance.defaults.headers['Authorization'] = null;
        // window.location.reload()
    })
    return <>Logout</>
}