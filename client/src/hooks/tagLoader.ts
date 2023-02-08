import { useState, useEffect } from "react";
import axiosInstance from "../axios";
import { ITag } from "../model";

export function useTag() {
  const [tags, setTags] = useState<ITag[]>([]);

  async function fetchTag() {
    const response = await axiosInstance.get<ITag[]>("threads/tag/");
    setTags(response.data);
  }

  useEffect(() => {
    fetchTag();
  }, []);

  return { tags };
}
