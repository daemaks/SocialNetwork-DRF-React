import {Link} from 'react-router-dom'
export function Header() {
    return (
        <>
            <Link to="/">Home</Link>
            <span> | </span>
            <Link to="/login">Login</Link>
            <span> | </span>
            <Link to="/logout">Logout</Link>
            <span> | </span>
            <Link to="/register">SignUp</Link>
        </>
    )
}