import React from 'react'
import SignUp from './register'
import SignIn from './login'

interface InOrUpProps {
    value: boolean
    close: () => void
}

export function InOrUp({value, close}:InOrUpProps) {
    if (value) {
        return <SignUp signUp={close}/>
    } else {
        return <SignIn signIn={close}/>
    }
}