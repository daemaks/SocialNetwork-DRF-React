import { useState } from 'react'
import { Link } from 'react-router-dom'
import { ITag } from '../model'
import { useTagCommunities } from '../hooks/communitiesLoader'
import { MdKeyboardArrowDown } from 'react-icons/md'
import React from 'react'

interface TagProp {
    tag:ITag
}

export function Tag({tag}:TagProp) {
    const {communities} = useTagCommunities(tag.id)
    const [open, setOpen] =useState(false)

    return (
        <div className={open ? 'item open' : 'item'}>
            <div onClick={() => setOpen(!open)}>
                <span className='flex items-center justify-between'>
                    {tag.title}
                    <MdKeyboardArrowDown className='arrow'/>
                </span>
                <div className='bg-slate-400 '>
                    { communities.map(community => {
                        return (
                            <div key={community.id}>
                                <Link to={`/c/${community.slug}`} className='link capitalize'>{community.title}</Link>
                            </div>
                        ) 
                    })}
                </div>
            </div>
        </div>
    )
}
