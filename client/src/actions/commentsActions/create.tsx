import { useState } from "react";
import axiosInstance from "../../axios";

export default function CommentCreate(id: any) {

    const initialFormData = Object.freeze({
        text: ''
    });

    const [formData, updateFormData] = useState(initialFormData)

    const handleChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
        updateFormData({
            ...formData,
            [event.target.name]: event.target.value.trim(),
        })
    }

    const handleSubmit = (event: React.MouseEvent<HTMLButtonElement>) => {
		event.preventDefault();

		axiosInstance
			.post(`threads/comment/create/`, {
                text: formData.text,
				thread: id.id
			})
			.then((res) => {
				window.location.reload()
			});
	};

    return (
        <div>
            <textarea 
                className="w-full h-32 p-2 rounded border border-gray-300 outline-0 resize-none max-h-fit"
                onChange={handleChange}
                name="text"
                placeholder="what are you thoughts?"></textarea>
            <button 
                onClick={handleSubmit}
                className="ml-2 py-1 px-2 border-2 rounded font-semibold">Post</button>
        </div>
    )
}