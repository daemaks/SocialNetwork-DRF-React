import { useState } from "react";
import axiosInstance from "../../axios";
import { IThread } from "../../model";
import { MdCheckCircleOutline, MdOutlineCancel } from "react-icons/md";
import { FiTrash } from "react-icons/fi";
import DeleteThread from "./delete";

interface ThreadProps {
  thread: IThread;
  onClose: () => void;
}
export default function ThreadUpdate({ thread, onClose }: ThreadProps) {
  const initialFormData = Object.freeze({
    title: thread.title,
    content: thread.content,
  });

  const [formData, updateFormData] = useState(initialFormData);

  const handleChange = (
    event:
      | React.ChangeEvent<HTMLInputElement>
      | React.ChangeEvent<HTMLTextAreaElement>
  ) => {
    updateFormData({
      ...formData,
      [event.target.name]: event.target.value.trim(),
    });
  };

  const handleSubmit = (event: React.MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();

    axiosInstance
      .put(`threads/thread/${thread.id}/`, {
        title: formData.title,
        community: thread.community.id,
        content: formData.content,
      })
      .then((res) => {
        window.location.reload();
      });
  };

  return (
    <div className="w-full">
      <div className="bg-white rounded p-1.5 ">
        <div className="mb-2">
          <input
            className="w-full p-2 rounded border border-gray-300 outline-0"
            type="text"
            name="title"
            defaultValue={thread.title}
            onChange={handleChange}
            placeholder="Title"
          />
        </div>
        <div className="mb-1">
          <textarea
            className="w-full h-fit p-2 rounded border border-gray-300 outline-0 resize-none"
            name="content"
            defaultValue={thread.content}
            onChange={handleChange}
            placeholder="Write something"
          ></textarea>
        </div>
        <div className="flex flex-row-reverse">
          <button
            onClick={handleSubmit}
            className="ml-1 p-1 rounded bg-green-700"
          >
            <MdCheckCircleOutline />
          </button>
          <button onClick={onClose} className="ml-1 p-1 rounded bg-yellow-300">
            <MdOutlineCancel />
          </button>
          <button
            onClick={() => {
              DeleteThread(thread.id);
            }}
            className="p-1 rounded bg-red-700"
          >
            <FiTrash />
          </button>
        </div>
      </div>
    </div>
  );
}
