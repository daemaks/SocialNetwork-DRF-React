import React from "react";

interface ModalProps {
  children: React.ReactNode;
  onClose: () => void;
}

export function Modal({ children, onClose }: ModalProps) {
  return (
    <div className="overflow-hidden">
      <div
        className="fixed bg-black opacity-50 top-0 right-0 left-0 bottom-0"
        onClick={onClose}
      ></div>
      <div className="w-[400px] p-6 rounded bg-white absolute top-20 left-1/2 -translate-x-1/2">
        {children}
      </div>
    </div>
  );
}
