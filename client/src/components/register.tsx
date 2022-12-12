import React, {useState} from "react";
import axiosInstance from '../axios';
import { useNavigate } from 'react-router-dom';

export default function SignUp() {
    const navigate = useNavigate();
    const initialFormData = Object.freeze({
        email: '',
        username: '',
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
        console.log(formData);

        axiosInstance
            .post(`user/register/`, {
                email: formData.email,
                username: formData.username,
                password: formData.password,
            })
            .then((res) => {
                navigate('/')
                console.log(res.status)
            })
    };
    return (
        <form action="">
            <input onChange={handleChange} type="text" name='email' placeholder='Enter Email'/>
            <input onChange={handleChange} type="text" name='username' placeholder='Enter username'/>
            <input onChange={handleChange} type="password" name='password' placeholder='Enter Password'/>
            <button type="submit" onClick={handleSubmit}>Submit</button>
        </form>
    )
}