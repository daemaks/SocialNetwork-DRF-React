import React from 'react'
import { ICommunity } from '../model'

interface CommunityProp {
    community:ICommunity
}

export function Community({ community }:CommunityProp) {
    return (
        <div className='w-full mb-4'>
            <div className='h-36 bg-cover w-full' style={{ backgroundImage: "url(https://www.wallpapers.net/data-programming-codes-hd-wallpaper/download/3840x2160.jpg)" }}>
            </div>
            <div className='bg-white'>
                <div className="mx-auto max-w-[984px] relative flex">
                    <div className='overflow-hidden relative -top-5 rounded-full border-4 border-whit bg-white'>
                        <img className='h-16 w-16' src={community?.image}/>
                    </div>
                    <div className='pt-2 pl-4'>
                        <h1 className='text-3xl font-bold'>{community?.title}</h1>
                        <h5 className='text-sm text-gray-400 font-medium'>c/{community?.title}</h5>
                    </div>
                </div>
            </div>
        </div>
    )
}