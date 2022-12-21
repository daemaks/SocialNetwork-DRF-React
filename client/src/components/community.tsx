import React from 'react'
import { ICommunity } from '../model'

interface CommunityProp {
    community:ICommunity
}

export function Community({ community }:CommunityProp) {
    return (
        <div>
            {community.title}
        </div>
    )
}