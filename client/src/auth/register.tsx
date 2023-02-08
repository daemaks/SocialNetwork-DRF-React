import React, { useState } from "react";
import axiosInstance from "../axios";
import { useNavigate } from "react-router-dom";

interface SignUpProps {
  signUp: () => void;
}

export default function SignUp({ signUp }: SignUpProps) {
  const navigate = useNavigate();
  const initialFormData = Object.freeze({
    email: "",
    username: "",
    password: "",
  });

  const [formData, updateFormData] = useState(initialFormData);

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    updateFormData({
      ...formData,
      [event.target.name]: event.target.value.trim(),
    });
  };

  const handleSubmit = (event: React.MouseEvent<HTMLButtonElement>) => {
    event.preventDefault();

    axiosInstance
      .post(`user/auth/register/`, {
        email: formData.email,
        username: formData.username,
        password: formData.password,
      })
      .then((res) => {
        signUp();
        navigate("/");
      });
  };
  return (
    <div>
      <h1 className="text-2xl text-center mb-2">Sign Up</h1>
      <form>
        <div className="flex flex-col flex-nowrap text-sm">
          <input
            className="mx-auto mt-4 bg-gray-200 outline-none rounded-full py-2 px-4"
            onChange={handleChange}
            type="text"
            name="email"
            placeholder="Enter Email"
          />
          <input
            className="mx-auto mt-4 bg-gray-200 outline-none rounded-full py-2 px-4"
            onChange={handleChange}
            type="text"
            name="username"
            placeholder="Enter username"
          />
          <input
            className="mx-auto mt-4 bg-gray-200 outline-none rounded-full py-2 px-4"
            onChange={handleChange}
            type="password"
            name="password"
            placeholder="Enter Password"
          />
          <button
            className="mt-4 bg-zinc-600 rounded-full py-2 px-4 mx-auto w-1/2"
            type="submit"
            onClick={handleSubmit}
          >
            Submit
          </button>
        </div>
      </form>
    </div>
  );
}
