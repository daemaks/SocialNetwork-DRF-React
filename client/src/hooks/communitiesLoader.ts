import React, {useState, useEffect} from 'react'
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

export function useTagCommunities(id:number) {
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
    const [community, setCommunity] = useState<ICommunity[]>([])

    async function fetchCommunities() {
        const response = await axiosInstance.get<ICommunity[]>(`threads/community/${id}`)
        setCommunity(response.data)

    }

    useEffect(() => {
        fetchCommunities()
    }, [])

    return { community }
}
