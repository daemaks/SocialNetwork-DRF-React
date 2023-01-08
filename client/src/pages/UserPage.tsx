import React from 'react'
import { useParams } from 'react-router-dom'
import { useUser } from '../hooks/userLoader'

export default function UserPage() {

    const { id } = useParams()
    const { user } =  useUser(id)

    return(
        <div className="flex max-w-full mt-12 ml-60">
            <div className="flex flex-row justify-center mx-auto py-5 px-6">
                <div className="w-[640px]">
                    threads
                </div>
                <div className='bg-white border border-gray-300 rounded block w-[320px] ml-6'>
                    <div className='rounded-t h-20 bg-cover w-full' style={{ backgroundImage: "url(http://getwallpapers.com/wallpaper/full/a/b/e/667524.jpg)" }}></div>
                    <div className='w-full p-2'>
                        <div className='flex content-center mx-auto h-16 w-16 overflow-hidden rounded-full border-2 bg-white'>
                            <img src={user?.avatar}/>
                        </div>
                        <div className='text-lg pt-2 text-center capitalize font-semibold'>
                            <h1>{user?.username}</h1>
                        </div>
                        <div className='text-center text-sm text-gray-400 font-medium pb-2'>
                            <span>u/{user?.username}</span>
                        </div>
                        <hr />
                        <div className='pt-2 leading-5 text-sm'>
                            <p>{user?.about}</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}