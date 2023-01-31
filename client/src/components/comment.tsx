import { Link } from "react-router-dom";
import { IComment } from "../model";
import getTime from "../tools/getTime";

interface CommentProps {
    comment : IComment
}

export default function Comment({comment} : CommentProps ) {
    return (
        <div className="mb-4">     
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
            <div className="ml-4 mt-1 pl-6 border-l-2">
                <p className="text-sm">
                    {comment.text}
                </p>
            </div>
        </div>
    )
}