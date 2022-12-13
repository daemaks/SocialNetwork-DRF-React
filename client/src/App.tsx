import React from 'react';
import {Routes, Route} from 'react-router-dom'
import {Header} from './components/Header';
import {Footer} from './components/Footer';
import MainPage from './pages/MainPage';
import SignUp from './components/register';
import SignIn from './components/login';

export default function App() {
  return (
    <div className="App">
      <Header/>
      <Routes>
        <Route path="/" element={<MainPage/>}/>
        <Route path='/login' element={<SignIn/>}/>
        <Route path='/register' element={<SignUp/>}/>
      </Routes>
      <Footer/>
    </div>
  );
}
