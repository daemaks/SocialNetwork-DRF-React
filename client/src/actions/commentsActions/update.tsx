import { useState } from 'react'
import { IComment } from '../../model'
import axiosInstance from '../../axios'
import { MdCheckCircleOutline, MdOutlineCancel } from 'react-icons/md'
import { FiTrash } from 'react-icons/fi'
import DeleteComment from './delete'

interface CommentProps {
    comment:IComment
    onClose: () => void
}

export default function CommentUpdate({comment, onClose} : CommentProps) {

    const initialFormData = Object.freeze({
        text: comment.text
    });

    const [formData, updateFormData] = useState(initialFormData)

    const handleChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        updateFormData({
            ...formData,
            [event.target.name]: event.target.value.trim(),
        })
        console.log(formData)
    }

    const handleSubmit = (event: React.MouseEvent<HTMLButtonElement>) => {
		event.preventDefault();

		axiosInstance
			.put(`threads/comment/${comment.id}/`, {
				text: formData.text
			})
			.then((res) => {
				window.location.reload()
			});
	};


    return (
        <div className="w-full">
            <div className="bg-white rounded p-1.5 ">
                <textarea
                    className="w-full h-fit p-2 rounded border border-gray-300 outline-0 resize-none"
                    name="text"
                    defaultValue={comment.text}
                    onChange={handleChange}></textarea>
                <div className="flex flex-row-reverse">
                        <button 
                            onClick={handleSubmit}
                            className="ml-1 p-1 rounded bg-green-700">
                                <MdCheckCircleOutline/>
                        </button>
                        <button
                            onClick={onClose}
                            className="ml-1 p-1 rounded bg-yellow-300">
                                <MdOutlineCancel/>
                        </button>
                        <button 
                            onClick={() => {DeleteComment(comment.id)}}
                            className="p-1 rounded bg-red-700">
                                <FiTrash/>
                        </button>
                    </div>
            </div>
        </div>
    )
}