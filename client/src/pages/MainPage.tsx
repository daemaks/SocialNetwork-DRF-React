import { Link } from "react-router-dom"
import { useThreads } from "../hooks/threadsLoader"
import { useCommunities } from "../hooks/communitiesLoader"
import Loader from "../components/loader"
import { Thread } from "../components/thread"
import { Community } from "../components/community"
import { IoHomeOutline } from 'react-icons/io5'
import { useTag } from "../hooks/tagLoader"
import { Tag } from "../components/tag"

export default function TreadsList() {

    const {loading, threads} = useThreads()
    const {communities} = useCommunities()
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
                    { communities.map(community => <Community community={ community } key={ community.id } />)}
                <div>
                </div>
                </div>
            </div>
            <div className="flex w-full mt-12 ml-80">
                <div className="flex w-full pt-8">
                    <div className="w-3/5">
                        { loading && <Loader /> }
                        { threads.map(thread => <Thread thread={ thread } key={ thread.id } />)}
                    </div>
                    <div className="w-2/5 h-full">
                    </div>
                </div>
            </div>
        </div>


    )
}