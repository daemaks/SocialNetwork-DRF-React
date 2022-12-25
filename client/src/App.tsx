import React from 'react';
import {Routes, Route} from 'react-router-dom'
import {Header} from './layouts/Header';
import {Footer} from './layouts/Footer';
import { Sidebar } from './layouts/Sidebar';
import TreadsList from './pages/ThreadsPage';
import SignUp from './components/register';
import SignIn from './components/login';
import LogOut from './components/logout';

export default function App() {
  return (
      <div className="App">
        <Header/>
        <Sidebar/>
          <Routes>
            <Route path="/" element={<TreadsList/>}/>
            <Route path='/login' element={<SignIn/>}/>
            <Route path='/logout' element={<LogOut/>}/>
            <Route path='/register' element={<SignUp/>}/>
          </Routes>
        <Footer/>
      </div>
  );
}
