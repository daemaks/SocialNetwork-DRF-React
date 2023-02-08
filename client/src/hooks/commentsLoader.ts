import { useState, useEffect } from "react";
import axiosInstance from "../axios";
import { IComment } from "../model";

export function useComments(id: any) {
  const [comments, setComments] = useState<IComment[]>([]);

  async function fetchComments() {
    const response = await axiosInstance.get<IComment[]>(
      `threads/thread/${id}/comments/`
    );
    setComments(response.data);
  }

  useEffect(() => {
    fetchComments();
  }, []);

  return { comments };
}
