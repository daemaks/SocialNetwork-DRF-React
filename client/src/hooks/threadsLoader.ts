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