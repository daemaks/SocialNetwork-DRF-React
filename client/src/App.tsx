import { Routes, Route } from "react-router-dom";
import { Header } from "./layouts/Header";
import { Footer } from "./layouts/Footer";
import { Sidebar } from "./layouts/Sidebar";
import TreadsList from "./pages/ThreadsListPage";
import ThreadItem from "./pages/ThreadPage";
import CommunityPage from "./pages/CommunityPage";
import UserPage from "./pages/UserPage";
import LogOut from "./auth/logout";
import { useEffect, useState } from "react";
import { IUser } from "./model";
import { AuthContext } from "./context/AuthContext";
import ThreadCreate from "./actions/threadsActions/create";

export default function App() {
  const [user, setUser] = useState<IUser | null>(null);
  useEffect(() => {
    const data = localStorage.getItem("user" as string);
    if (data !== null) setUser(JSON.parse(data) as IUser);
  }, []);

  return (
    <div className="App">
      <AuthContext.Provider value={{ user, setUser }}>
        <Header />
        <Sidebar />
        <div className="max-w-full mt-12 ml-60">
          <Routes>
            <Route path="/" element={<TreadsList />} />
            <Route path="/c/:slug" element={<CommunityPage />} />
            <Route path="/u/:slug" element={<UserPage />} />
            <Route path="/t/:id" element={<ThreadItem />} />
            <Route path="/t/create" element={<ThreadCreate />} />
            <Route path="/logout" element={<LogOut />} />
          </Routes>
        </div>
        <Footer />
      </AuthContext.Provider>
    </div>
  );
}
