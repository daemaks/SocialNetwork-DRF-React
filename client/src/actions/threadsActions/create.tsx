import { useState, useEffect } from "react";
import { useNavigate, useLocation, Link } from "react-router-dom";
import axiosInstance from "../../axios";
import { ICommunity } from "../../model";

interface CommunityProp {
    community:ICommunity
}

export default function ThreadCreate() {
    const location = useLocation()
    const [locationState, setLocationState] = useState<CommunityProp | null>(null)
    const navigate = useNavigate()

    useEffect(() => {
        if (location.state) {
            let state = location.state as CommunityProp
            setLocationState(state)
        }
    }, [location])

    const initialFormData = Object.freeze({
        title: '',
        community: '',
        content: '',
    });

    const [formData, updateFormData] = useState(initialFormData)

    const handleChange = (event: React.ChangeEvent<HTMLInputElement> | React.ChangeEvent<HTMLTextAreaElement>) => {
        updateFormData({
            ...formData,
            [event.target.name]: event.target.value.trim(),
        })
    }

    const handleSubmit = (event: React.MouseEvent<HTMLButtonElement>) => {
		event.preventDefault();

		axiosInstance
			.post(`threads/thread/`, {
				title: formData.title,
                community: locationState?.community.id,
				content: formData.content,
			})
			.then((res) => {
				navigate(`/c/${locationState?.community.slug}`);
			});
	};

    return (
        <div className="flex justify-center py-5 px-6">
            <div className="w-[640px]">
                <div className="pb-5">
                    <h1 className="font-bold text-lg">Create a post</h1>
                </div>
                <div className="pb-5">
                    <div className="flex items-center justify-center rounded bg-white border border-gray-300 p-3 max-w-max">
                        <img className="rounded-full w-5 h-5 mr-1.5" src={locationState?.community.image}/>
                        <Link to={`/c/${locationState?.community.slug}`}>c/{locationState?.community.slug}</Link>
                    </div>
                </div>
                <div className="w-full bg-white rounded p-3">
                    <div className="mb-2">
                        <input 
                            className="w-full p-2 rounded border border-gray-300 outline-0"
                            onChange={handleChange}
                            type="text"
                            name="title"
                            placeholder="Title" />
                    </div>
                    <div className="mb-2">
                        <textarea
                            className="w-full h-64 p-2 rounded border border-gray-300 outline-0 resize-none"
                            onChange={handleChange}
                            name="content"
                            placeholder="Write something"></textarea>
                    </div>
                    <div className="flex flex-row-reverse">
                        <button 
                            onClick={handleSubmit}
                            className="ml-2 py-1 px-2 border-2 rounded font-semibold">Post</button>
                        <button 
                            onClick={() => navigate(-1)}
                            className="py-1 px-2 border-2 rounded font-semibold">Cancel</button>
                    </div>
                </div>
            </div>
            <div className="w-[320px] ml-6">

            </div>
        </div>
    )
}