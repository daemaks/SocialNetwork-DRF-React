import React from 'react'
import { IThread } from '../model'

interface ThreadProps {
    thread:IThread
}

const getTime = ( thread: IThread) => {
    const dateNow = new Date()
    const dateThread = new Date(thread.updated_at)
    const timeDifference  = (dateNow.getTime() - dateThread.getTime())
    const hourDifference = timeDifference / (1000 * 3600)
    if (hourDifference > 23) {
        const dayDifference = timeDifference / (1000 * 3600 * 24)
        return `${Math.round(dayDifference)} days`
    } else {
        return `${Math.round(hourDifference)} hours`
    }
}

export function Thread({ thread }:ThreadProps) {
    return (
        <div className='border border-gray-300 flex bg-white rounded mb-6 ml-72 w-4/6'>
            <div className='bg-slate-100 w-9 rounded-l'></div>
            <div className='block px-1.5 w-full '>
                <div className='flex h-4 text-xs'>
                    <span className='mr-0.5 font-bold'>c/{thread.community} </span>
                    <span className='text-slate-500'> • Posted by u/{thread.username} {getTime(thread)} ago</span>
                </div>
                <div className='pt-1'>
                    <span className='antialiased text-lg font-medium'>{thread.title}</span>
                </div>
                <div className='flex justify-center'>
                    <img className='max-h-[600px]' src={thread.image}/>
                </div>
                <div className='pt-1'>
                    <p className='antialiased text-sm'>{thread.content}</p>
                </div>
                <div className='mt-0.5'>
                    <span>Likes</span>
                    <span>Comments</span>
                </div>
            </div>
        </div>
    )
}