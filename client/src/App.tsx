import {Routes, Route} from 'react-router-dom'
import {Header} from './layouts/Header';
import {Footer} from './layouts/Footer';
import { Sidebar } from './layouts/Sidebar';
import TreadsList from './pages/ThreadsPage';
import CommunityDetails from './pages/CommunityPage';
import SignUp from './components/register';
import LogOut from './components/logout';

export default function App() {
  return (
      <div className="App">
        <Header/>
        <Sidebar/>
          <Routes>
            <Route path="/" element={<TreadsList/>}/>
            <Route path='/c/:id' element={<CommunityDetails/>} />
            <Route path='/logout' element={<LogOut/>}/>
            <Route path='/register' element={<SignUp/>}/>
          </Routes>
        <Footer/>
      </div>
  );
}
