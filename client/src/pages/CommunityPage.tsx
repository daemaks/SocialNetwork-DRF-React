import { useParams } from "react-router-dom";
import { useCommunity } from "../hooks/communitiesLoader"; 
import { Community } from "../components/community";
import { ICommunity } from "../model";

export default function CommunityDetails() {

    const { id } = useParams()
    const { community } = useCommunity(id as string)
    return (
        <div className="flex w-full mt-12 ml-80">
            <Community community={community as ICommunity} key={community?.id} />
            {/* <div className="flex w-full pt-8">
                <div className="w-3/5">
                </div>
                <div className="w-2/5 h-full">
                </div>
            </div> */}
        </div>
    )
}