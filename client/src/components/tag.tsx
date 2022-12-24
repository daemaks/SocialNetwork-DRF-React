import React from 'react'
import { ITag, ICommunity } from '../model'
import { useTagCommunities } from '../hooks/communitiesLoader'

interface TagProp {
    tag:ITag
}

export function Tag({tag}:TagProp) {
    const {communities} = useTagCommunities(tag.id)
    console.log(communities)

    return (
        <div>
            <button>
                {tag.title}
            </button>
            <ul>
                
            </ul>
        </div>
    )
}
