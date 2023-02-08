import axiosInstance from "../../axios";

export default function DeleteComment(id: number) {
  axiosInstance.delete(`threads/comment/${id}/`).then(() => {
    window.location.reload();
  });

  return;
}
