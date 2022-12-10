import React from 'react';
import {Routes, Route} from 'react-router-dom'
import {Header} from './components/Header';
import {Footer} from './components/Footer';
import MainPage from './pages/MainPage';

export default function App() {
  return (
    <div className="App">
      <Header/>
      <Routes>
        <Route path="/" element={<MainPage/>}/>
      </Routes>
      <Footer/>
    </div>
  );
}
