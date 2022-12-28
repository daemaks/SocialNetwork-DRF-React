import { useParams } from "react-router-dom";
import { useCommunity } from "../hooks/communitiesLoader"; 
import { Community } from "../components/community";
import { ICommunity } from "../model";
import { useCommunityThreads } from "../hooks/threadsLoader";
import Loader from "../components/loader"
import { CommunityThread } from "../components/thread"


export default function CommunityDetails() {

    const { id } = useParams()
    const { community } = useCommunity(id as string)
    const {loading, threads} = useCommunityThreads(id)
    

    return (
        <div className="max-w-full mt-12 ml-60">
            <Community community={community as ICommunity} key={community?.id} />
            <div className="flex flex-row justify-center mx-auto py-5 px-6">
                <div className="w-[640px]">
                { loading && <Loader /> }
                { threads.map(thread => <CommunityThread thread={ thread } key={ thread.id } />)}
                </div>
                <div></div>
            </div>
        </div>
    )
}