import React from 'react';
import {Routes, Route} from 'react-router-dom'
import {Header} from './components/Header';
import {Footer} from './components/Footer';
import MainPage from './pages/MainPage';
import LoginPage from './pages/LoginPage';
import SignUp from './components/register';

export default function App() {
  return (
    <div className="App">
      <Header/>
      <Routes>
        <Route path="/" element={<MainPage/>}/>
        <Route path='/login' element={<LoginPage/>}/>
        <Route path='/register' element={<SignUp/>}/>
      </Routes>
      <Footer/>
    </div>
  );
}
