import React, {useEffect} from 'react'
import axiosInstance from '../axios'
import { useNavigate } from 'react-router-dom'

export default function LogOut() {
    const navigate = useNavigate()
    
    useEffect(() => {
        axiosInstance.post('user/logout/', {
            refresh_token: localStorage.getItem('refresh_token'),
        })
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        axiosInstance.defaults.headers['Authorization'] = null;
        navigate('/login');
    })
    return <>Logout</>
}