import React, {useState, useEffect} from 'react'
import axiosInstance from '../axios'
import { IThread } from '../model'


export function useThreads() {
    const [threads, setThreads] = useState<IThread[]>([])
    const [loading, setLoading] = useState(false)

    async function fetchThreads() {
        setLoading(true)
        const response = await axiosInstance.get<IThread[]>('threads/')
        setThreads(response.data)
        setLoading(false)
    }

    useEffect(() => {
        fetchThreads()
    }, [])

    return { threads, loading }
}

export function useCommunityThreads(id:any) {
    const [threads, setThreads] = useState<IThread[]>([])
    const [loading, setLoading] = useState(false)

    async function fetchCommunityThreads() {
        setLoading(true)
        const response = await axiosInstance.get<IThread[]>(`threads/community/${id}/threads`)
        setThreads(response.data)
        setLoading(false)
    }

    useEffect(() => {
        fetchCommunityThreads()
    }, [])

    return { threads, loading }
}