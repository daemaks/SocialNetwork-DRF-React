import {Routes, Route} from 'react-router-dom'
import {Header} from './layouts/Header';
import {Footer} from './layouts/Footer';
import { Sidebar } from './layouts/Sidebar';
import TreadsList from './pages/ThreadsPage';
import CommunityPage from './pages/CommunityPage';
import UserPage from './pages/UserPage';
import LogOut from './components/logout';
import { useEffect, useState } from 'react';
import { IUser } from './model';
import { AuthContext } from './context/AuthContext';

export default function App() {
  const [user, setUser] = useState<IUser | null>(null)
  useEffect(() => {
    const data = localStorage.getItem('user' as string)
    if (data !== null ) setUser(JSON.parse(data) as IUser)
  }, [])

  return (
      <div className="App">
        <AuthContext.Provider value={{user, setUser}}>
          <Header/>
          <Sidebar/>
            <Routes>
              <Route path="/" element={<TreadsList/>}/>
              <Route path='/c/:slug' element={<CommunityPage/>} />
              <Route path='/u/:id' element={<UserPage/>}/>
              <Route path='/logout' element={<LogOut/>}/>
            </Routes>
          <Footer/>
        </AuthContext.Provider>
      </div>
  );
}
