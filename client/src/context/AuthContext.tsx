import { createContext, useContext } from "react";
import { IUser } from "../model";

type AuthContextType = {
    user: IUser | null
    setUser : React.Dispatch<React.SetStateAction<IUser | null>>
}

export const AuthContext = createContext<AuthContextType | null>(null)

export const useAuth = () => useContext(AuthContext)