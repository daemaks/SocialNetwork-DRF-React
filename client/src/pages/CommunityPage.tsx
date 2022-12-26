import { useParams } from "react-router-dom";
import { useCommunity } from "../hooks/communitiesLoader"; 
import { ICommunity } from "../model";

interface CommunityProps {
    community:ICommunity
}

export default function CommunityDetails() {

    const { id } = useParams()
    const { community } = useCommunity(id)
    console.log(community)

    return (
        <div className="flex w-full mt-12 ml-80">
                <div className="flex w-full pt-8">
                    <div className="w-3/5">
                        <p></p>
                    </div>
                    <div className="w-2/5 h-full">
                    </div>
                </div>
            </div>
    )
}