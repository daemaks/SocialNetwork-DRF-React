import {useState} from 'react'
import {Link} from 'react-router-dom'
import { Modal } from '../components/modal'
import { InOrUp } from '../components/loginOrRegister'

export function Header() {
    const [modal, setModal] = useState(false)
    const [value, setValue] = useState(true)
    return (
        <div className='fixed flex items-center bg-neutral-400 h-12 w-full px-5'>
                <div className='mr-96'>
                    <Link to="/">Home</Link>
                </div>
                <div className='w-6/12'>
                    <label className="relative block">
                        <input
                            type="search" 
                            placeholder='Search'
                            className='w-9/12 px-3 py-2 rounded-3xl' />
                    </label>
                </div>
                {modal && <Modal onClose={() => setModal(false)}>
                    <div className='flex flex-col justify-center'>
                    <InOrUp 
                        value={value} 
                        close={() => setModal(false)}/>
                    <button 
                        className='text-xs mt-2 hover:underline'
                        onClick={() => setValue(!value)}>
                        {value ? (
                            <span>Already have an account? Sign in</span>
                        ): (
                            <span>Don’t have an account? Sign up</span>
                        )}
                    </button>
                    </div>
                </Modal>}
                <button onClick={() => setModal(true)}>
                    Get Started
                </button>
                <span> | </span>
                <Link to="/logout">Logout</Link>
                <span> | </span>
            </div>
    )
}