import { useState } from 'react'
import { Link } from "react-router-dom";
import { IComment } from "../model";
import getTime from "../tools/getTime";
import { useAuth } from '../context/AuthContext';
import CommentUpdate from '../actions/commentsActions/update';
import { BiPencil } from 'react-icons/bi'

interface CommentProps {
    comment : IComment
}

export default function Comment({comment} : CommentProps ) {
    const [updateState, setUpdateState] = useState(false)
    const context = useAuth()
        if ( ! context ) {
            return null;
        }
        const { user } = context;
    return (
        <div className="mb-4 ">
            {updateState ? <CommentUpdate comment={comment} onClose={() => setUpdateState(false)}/> :
                <div className='p-1 rounded-tl-3xl rounded-lg hover:bg-gray-100'>
                    <div className="flex justify-between ">
                        <div className="flex items-center">
                            <img 
                                src={comment.username.avatar}
                                className="rounded-full w-8 h-8 mr-2"/>
                            <Link to={`/u/${comment.username.slug}`} className="text-sm mr-1 cursor-pointer hover:underline">
                                {comment.username.username}
                            </Link>
                            <span className="text-sm text-slate-500">
                                • {getTime(comment)} ago
                            </span>
                        </div>
                        <div>
                            {user?.username == comment.username.username ? (
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
                    <div className="ml-4 mt-1 pl-6 border-l-2">
                        <p className="text-sm">
                            {comment.text}
                        </p>
                    </div>
                </div>
            }
        </div>
    )
}