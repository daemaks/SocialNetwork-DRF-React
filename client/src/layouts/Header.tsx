import { useState } from 'react'
import { Link } from 'react-router-dom'
import { Modal } from '../components/modal'
import { InOrUp } from '../components/loginOrRegister'
import { useAuth } from '../context/AuthContext'
import { BiExit } from 'react-icons/bi'

export function Header() {
    const [modal, setModal] = useState(false)
    const [value, setValue] = useState(true)
    const context = useAuth()
        if ( ! context ) {
            return null;
        }
        const { user } = context;
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
                {user ? (
                    <div className='relative'>
                        <div className='rounded-full flex justify-between items-center cursor-pointer'>
                            <div className='flex rounded-full p-1 duration-200 hover:bg-slate-100'>
                                <img className='rounded-full w-6 h-6 mr-1.5' src={`http://127.0.0.1:8000${user.avatar}`} alt='pic'/>
                                <Link to={`/u/${user.slug}`} className='ml-1'>u/{user.username}</Link>
                            </div>
                            <div className='ml-2 rounded-full p-1 duration-200 hover:bg-slate-100'>
                                <Link to="/logout">
                                    <BiExit size='1.3rem'/>
                                </Link>
                            </div>
                        </div>
                    </div>
                ) : (
                    <div className='bg-zinc-800 text-white px-2 py-1 rounded-full duration-200 hover:bg-slate-100 hover:text-black'>
                        <button onClick={() => setModal(true)}>
                        Get Started
                        </button>
                    </div>
                )}
            </div>
    )
}