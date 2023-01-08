import {useState, useEffect} from 'react'
import axiosInstance from '../axios'
import { IUser } from '../model'

export function useUser(id:any) {
    const [user , setUser] = useState<IUser | null>(null)

    useEffect(() => {
        fetchUser()
    }, [])

    async function fetchUser() {
        const response = await axiosInstance.get<IUser>(`/user/${id}`)
        setUser(response.data)
    }

    return { user }
}