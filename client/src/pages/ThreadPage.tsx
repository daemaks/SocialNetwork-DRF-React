import { useParams, useNavigate, Link } from "react-router-dom"
import { useThread } from "../hooks/threadsLoader"
import { BsCardText } from 'react-icons/bs'
import { TfiClose } from 'react-icons/tfi'
import { IThread } from "../model"
import getTime from "../tools/getTime"


export default function ThreadItem() {
    const { id } = useParams()
    const navigate = useNavigate()
    const {thread} = useThread(id)

    return(
        <>
            <div className='overflow-hidden'>
                <div className='fixed bg-black opacity-80 top-12 right-0 left-0 bottom-0'></div>
                <div className='w-[1280px] bg-white absolute left-1/2 -translate-x-1/2'>
                    <div className="flex justify-between items-center w-full bg-black text-white px-8 py-4">
                        <div className="flex items-center">
                            <BsCardText/>
                            <span className="ml-2 text-sm">{thread?.title}</span>
                        </div>
                        <TfiClose 
                            className="cursor-pointer"
                            onClick={() => {navigate(-1)}}/>
                    </div>
                    <div className="w-full h-fit px-4">
                        <div className="mb-4">
                            <div className="flex p-1.5 w-full text-xs">
                                <img className='rounded-full w-5 h-5 mr-1.5' src={thread?.community.image}/>
                                <Link to={`/c/${thread?.community.slug}`} className='mr-0.5 font-bold hover:underline'>c/{thread?.community.title} </Link>
                                <span className='text-slate-500'> • Posted by u/{thread?.username}  {getTime(thread)} ago</span>
                            </div>
                            <div>
                                <div className='pt-1'>
                                    <span className='antialiased text-lg font-medium'>{thread?.title}</span>
                                </div>
                                <div className='flex justify-center'>
                                    <img className='max-h-[600px]' src={thread?.image}/>
                                </div>
                                <div className='pt-1'>
                                    <p className='antialiased text-sm'>{thread?.content}</p>
                                </div>
                            </div>
                        </div>
                        <div>
                            #comment
                        </div>
                    </div>
                </div>
            </div>
        </>
    )
}