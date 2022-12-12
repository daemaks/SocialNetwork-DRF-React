import React from 'react'

const LoginPage = () => {
  return (
    <div>
        <form>
            <input type="text" name='email' placeholder='Enter Email'/>
            <input type="password" name='password' placeholder='Enter Password'/>
            <input type="submit" />
        </form>
    </div>
  )
}

export default LoginPage