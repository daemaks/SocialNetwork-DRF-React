import { Link } from "react-router-dom"
import { useThreads } from "../hooks/threadsLoader"
import { useCommunities } from "../hooks/communitiesLoader"
import Loader from "../components/loader"
import { Thread } from "../components/thread"
import { Community } from "../components/community"

export default function TreadsList() {

    const {loading, threads} = useThreads()
    const {communities} = useCommunities()

    return (
        <div className="flex w-full" >
            <div className="fixed top-12 w-80 bg-white h-full">
                <Link to="/">Home</Link>
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
            {/* <div>
            { communities.map(community => <Community community={ community } key={ community.id } />)}
            </div> */}
        </div>


    )
}