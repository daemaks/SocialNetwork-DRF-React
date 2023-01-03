import { useParams } from "react-router-dom";
import { useCommunity } from "../hooks/communitiesLoader"; 
import { Community } from "../components/community";
import { ICommunity } from "../model";
import { useCommunityThreads } from "../hooks/threadsLoader";
import Loader from "../components/loader"
import { CommunityThread } from "../components/thread"
import { BiCalendarPlus } from 'react-icons/bi'


export default function CommunityDetails() {

    const { id } = useParams()
    const { community } = useCommunity(id as string)
    const {loading, threads} = useCommunityThreads(id)

    const getCreatedTime = (community : ICommunity | null) => {
        // add create field in the Community model
        // return new Date(community.created).toDateString()
        return new Date(2022, 7, 12).toDateString()
      }
    

    return (
        <div className="max-w-full mt-12 ml-60">
            <Community community={community as ICommunity} key={community?.id} />
            <div className="flex flex-row justify-center mx-auto py-5 px-6">
                <div className="w-[640px]">
                { loading && <Loader /> }
                { threads.map(thread => <CommunityThread thread={ thread } key={ thread.id } />)}
                </div>
                <div className="block w-[320px] ml-6">
                    <div className="flex flex-col h-full">
                        <div className="align-baseline">
                            <div className="text-xs font-bold tracking-[.03em] leading-3 uppercase rounded-t p-3 bg-zinc-700 text-white">
                                <h2>About Community</h2>
                            </div>
                            <div className="p-3 bg-white rounded-b">
                                <div className="mb-2 relative">
                                    <div className="text-sm leading-[21px] font-normal">
                                        {community?.description}
                                    </div>
                                </div>
                                <div className="flex flex-row flex-nowrap text-sm leading-[18px] font-normal items-center">
                                    <BiCalendarPlus size='1.3rem'/>
                                    <span className="text-slate-500 ml-1">Created {getCreatedTime(community)}</span>
                                </div>
                                <hr className="my-6"/>
                                <div className="block">
                                    <div className="text-base leading-5 font-medium">
                                        {community?.members.length}
                                    </div>
                                    <p className="text-slate-500 ml-1 font-normal text-xs inline-block">Members</p>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}