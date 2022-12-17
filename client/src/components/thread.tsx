import React from 'react'
import { IThread } from '../model'

interface ThreadProps {
    thread:IThread
}

export function Thread(props:ThreadProps) {
    return (
        <div>
            {props.thread.title}
        </div>
    )
}