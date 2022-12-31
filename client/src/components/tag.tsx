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

    const dropdowns = document.querySelectorAll('.dropdown');
    dropdowns.forEach(dropdown => {
        const select = dropdown.querySelector('.select') as Element
        const caret = dropdown.querySelector('.caret') as Element
        const menu = dropdown.querySelector('.menu') as Element
        const options = dropdown.querySelectorAll('.menu li') as NodeListOf<Element>

        select.addEventListener('click', () => {
            caret.classList.toggle('rotate-180');
            menu.classList.toggle('menu-open');
        });

        options.forEach(option => {
            option.addEventListener('click', () => {
                caret.classList.remove('rotate-180');
                menu.classList.remove('menu-open');
            })
        });
    })

    return (
        <div className='dropdown relative'>
            <div className='select flex justify-between items-center cursor-pointer p-1 duration-200 hover:bg-slate-100'>
                <span>{tag.title}</span>
                <div className='caret'> <MdKeyboardArrowDown/> </div>
            </div>
            <ul className='menu p-1 absolute left-[50%] w-full opacity-0 none translate-x-[-50%] duration-200 z-[1]'>
            { communities.map(community => {
                return (
                    <li className='p-1 hover:bg-slate-100'>
                        <Link to={`/c/${community.id}`} className='capitalize'>{community.title}</Link>
                    </li>
                )
            })}
            </ul>
        </div>
    )
}
