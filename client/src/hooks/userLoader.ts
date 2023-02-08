import { useState, useEffect } from "react";
import axiosInstance from "../axios";
import { IUser } from "../model";

export function useUser(slug: any) {
  const [user, setUser] = useState<IUser>();

  useEffect(() => {
    fetchUser();
  }, []);

  async function fetchUser() {
    const response = await axiosInstance.get<IUser>(`/user/${slug}/`);
    setUser(response.data);
  }

  return { user };
}
