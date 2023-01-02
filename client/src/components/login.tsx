import React, {useState} from "react";
import axiosInstance from '../axios';
import { useNavigate } from 'react-router-dom';

interface SignInProps {
    signIn: () => void
}

export default function SignIn({signIn}: SignInProps) {
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
            signIn()
            navigate('/')
        });
    };

    return (
        <div>
            <form>
                <div className="flex flex-col flex-nowrap text-sm">
                    <input 
                        className="mx-auto mt-4 bg-gray-200 outline-none rounded-full py-2 px-4"
                        onChange={handleChange} 
                        type="text" 
                        name='email' 
                        placeholder='Enter Email'/>

                    <input 
                        className="mx-auto mt-4 bg-gray-200 outline-none rounded-full py-2 px-4"
                        onChange={handleChange} 
                        type="password" 
                        name='password' 
                        placeholder='Enter Password'/>
                    <button 
                        className="mt-4 bg-zinc-600 rounded-full py-2 px-4 mx-auto w-1/2"
                        type="submit" 
                        onClick={handleSubmit}>Submit</button>
                </div>
            </form>
        </div>
    )
}
