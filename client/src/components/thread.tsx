import React from 'react'
import { IThread } from '../model'

interface ThreadProps {
    thread:IThread
}

export function Thread({ thread }:ThreadProps) {
    return (
        <div>
            {thread.title}
        </div>
    )
}