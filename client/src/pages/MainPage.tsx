import { useThreads } from "../hooks/threadsLoader"
import { useCommunities } from "../hooks/communitiesLoader"
import Loader from "../components/loader"
import { Thread } from "../components/thread"
import { Community } from "../components/community"

export default function TreadsList() {

    const {loading, threads} = useThreads()
    const {communities} = useCommunities()

    return (
        <div>
            <div>
            { loading && <Loader /> }
            { threads.map(thread => <Thread thread={ thread } key={ thread.id } />)}
            </div>
            <div>
            { communities.map(community => <Community community={ community } key={ community.id } />)}
            </div>
        </div>


    )
}