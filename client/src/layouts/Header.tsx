import {Link} from 'react-router-dom'
export function Header() {
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
                <Link to="/login">Login</Link>
                <span> | </span>
                <Link to="/logout">Logout</Link>
                <span> | </span>
                <Link to="/register">SignUp</Link>
        </div>
    )
}