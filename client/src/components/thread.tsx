import { Link } from 'react-router-dom'
import { IThread } from '../model'
import { BiLike, BiComment, BiPencil } from 'react-icons/bi'
import { useState } from 'react'
import { useAuth } from '../context/AuthContext'
import ThreadUpdate from '../actions/threadsActions/update'
import getTime from '../tools/getTime'

interface ThreadProps {
    thread:IThread
}

export function Thread({ thread }:ThreadProps) {
    const [updateState, setUpdateState] = useState(false)
    const context = useAuth()
        if ( ! context ) {
            return null;
        }
        const { user } = context;

    return (
        <>
            <div className='border border-gray-300 flex bg-white rounded mb-2'>
                <div className='bg-slate-100 w-9 rounded-l'></div>
                {updateState ? <ThreadUpdate thread={thread} onClose={() => setUpdateState(false)}/> :
                <div className='block px-1.5 w-full '>
                    <div className='flex justify-between mt-1.5 h-4 text-xs'>
                        <div className='flex'>      
                            <img className='rounded-full w-5 h-5 mr-1.5' src={thread.community.image}/>
                            <Link to={`/c/${thread.community.slug}`} className='mr-0.5 font-bold hover:underline'>c/{thread.community.title} </Link>
                            <span className='text-slate-500'> • Posted by u/{thread.username} {getTime(thread)} ago</span>
                            { thread.created_at != thread.updated_at ? (
                                <span className='ml-1.5 text-slate-500'>(edited)</span>
                            ) : (<></>)}
                        </div>
                        <div>
                            {user?.username == thread.username ? (
                                <button 
                                    className='bg-gray-300 p-1 rounded'
                                    onClick={() => setUpdateState(true)}>
                                    <BiPencil size='1rem' />
                                </button>
                            ): (
                                <div></div>
                            )}
                        </div>
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
                    <div className='flex my-1 font-medium text-sm text-slate-500'>
                        <div className='mr-5'>
                            <a href="#" className='flex items-center'>
                            <BiLike size='1.3rem'/>
                            <span className='ml-1'>Likes</span>
                            </a>
                        </div>
                        <div>
                            <Link 
                                to={`/t/${thread.id}`}
                                className='flex items-center'>
                            <BiComment size='1.3rem'/>
                            <span className='ml-1'>Comments</span>
                            </Link>
                        </div>
                    </div>
                </div>
                }
            </div>
        </>
    )
}

export function CommunityThread({ thread }:ThreadProps) {
    return (
        <div className='mb-2 border border-gray-300 flex bg-white rounded'>
                <div className='bg-slate-100 w-9 rounded-l'></div>
                <div className='block px-1.5 w-full '>
                    <div className='flex mt-1.5 h-4 text-xs'>
                        <span className='text-slate-500'>Posted by u/{thread.username} {getTime(thread)} ago</span>
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
                    <div className='flex my-1 font-medium text-sm text-slate-500'>
                        <div className='mr-5'>
                            <a href="#" className='flex items-center'>
                            <BiLike size='1.3rem'/>
                            <span className='ml-1'>Likes</span>
                            </a>
                        </div>
                        <div>
                            <Link to={`/t/${thread.id}`} className='flex items-center'>
                            <BiComment size='1.3rem'/>
                            <span className='ml-1'>Comments</span>
                            </Link>
                        </div>
                    </div>
                </div>
            </div>
    )
}
