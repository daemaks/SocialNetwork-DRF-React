import { createContext, useContext, useState } from "react";

type AuthContextProviderProps = {
    children: React.ReactNode
    userData: any
}

const AuthContext = createContext<any>(null)

export const AuthContextProvider = ({userData, children}:AuthContextProviderProps) => {
    const [user, setUser] = useState(userData)

    return (
        <AuthContext.Provider value={{ user, setUser }}>
            {children}
        </AuthContext.Provider>
    )
}

export const useAuth = () => useContext(AuthContext);