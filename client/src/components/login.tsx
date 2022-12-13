import React, {useState} from "react";
import axiosInstance from '../axios';
import { useNavigate } from 'react-router-dom';

export default function SignIn() {
    const navigate = useNavigate();
    const initialFormData = Object.freeze({
        email: '',
        password:'',
    });

    const [formData, updateFormData] = useState(initialFormData)

    const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
        updateFormData({
            ...formData,
            [event.target.name]: event.target.value.trim(),
        });
    };
    const handleSubmit = (event: React.MouseEvent<HTMLButtonElement>) => {
        event.preventDefault();

    axiosInstance
        .post(`token/`, {
            email: formData.email,
            password: formData.password,
        })
        .then((res) => {
            localStorage.setItem('access_token', res.data.access);
            localStorage.setItem('refresh_token', res.data.refresh);
            axiosInstance.defaults.headers['Authorization'] =
                'Bearer ' + localStorage.getItem('access_token');
            navigate('/')
            console.log(res.data)
        });
    };

    return (
        <form>
            <input onChange={handleChange} type="text" name='email' placeholder='Enter Email'/>
            <input onChange={handleChange} type="password" name='password' placeholder='Enter Password'/>
            <button type="submit" onClick={handleSubmit}>Submit</button>
        </form>
    )
}
