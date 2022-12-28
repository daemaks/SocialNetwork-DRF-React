import {useState, useEffect} from 'react'
import axiosInstance from '../axios'
import { ICommunity } from '../model'

export function useCommunities() {
    const [communities, setCommunities] = useState<ICommunity[]>([])

    async function fetchCommunities() {
        const response = await axiosInstance.get<ICommunity[]>('threads/community/')
        setCommunities(response.data)
    }

    useEffect(() => {
        fetchCommunities()
    }, [])

    return { communities }
}

export function useTagCommunities(id:any) {
    const [communities, setCommunities] = useState<ICommunity[]>([])
    
    async function fetchCommunities() {
        const response = await axiosInstance.get<ICommunity[]>(`threads/tag/${id}`)
        setCommunities(response.data)
    }

    useEffect(() => {
        fetchCommunities()
    }, [])

    return { communities }
}

export function useCommunity(id:any) {
    const [community, setCommunity] = useState<ICommunity | null>(null)

    
    useEffect(() => {
        fetchCommunity()
    }, [])
    
    async function fetchCommunity() {
        const response = await axiosInstance.get<ICommunity>(`threads/community/${id}`)
        setCommunity(response.data)
    }

    return { community }
}
