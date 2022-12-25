import { Link } from "react-router-dom"
//Hooks
import { useTag } from "../hooks/tagLoader"
//Componnets
import { Tag } from "../components/tag"
//Icons
import { IoHomeOutline } from 'react-icons/io5'

export function Sidebar() {

    const {tags} = useTag()

    return (
        <div className="flex w-full" >
            <div className="fixed top-12 w-80 bg-white h-full">
                <div className="py-4 px-6">
                    <div className="antialiased text-[10px] font-bold text-slate-500 pb-4">FEEDS</div>
                    <div className="text-sm pb-4">
                        <Link className="flex items-center" to="/">
                            <IoHomeOutline size='1.3rem'/>
                            <span className="ml-1">Home</span>
                        </Link>
                    </div>
                    <div className="antialiased text-[10px] font-bold text-slate-500 pb-4">TOPICS</div>
                    <div className="text-sm pb-4">
                        {tags.map(tag => <Tag tag={tag} key={tag.id}/>)}
                    </div>
                <div>
                </div>
                </div>
            </div>
        </div>
    )
}