import React from 'react'

interface ModalProps {
    children: React.ReactNode
}

export function Modal({children}: ModalProps) {
    return (
        <>
            <div className='fixed bg-black/50 top-0 right-0 left-0 bottom-0'></div>
            <div className='w-[400px] p-6 rounded bg-white absolute top-20 left-1/2 -translate-x-1/2'>
                {children}
            </div>
        </>
    )
}