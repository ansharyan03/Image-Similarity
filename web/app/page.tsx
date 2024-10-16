'use client';
import Image from "next/image";
import { useRef, useState } from "react";
import { Button } from "@mui/material";

export default function Home() {
  const [username, setUsername] = useState('');
  const [passphrase, setPassphrase] = useState('');
  
  const handleUpload = () => {
  }

  const handleUsername = (event: React.ChangeEvent<HTMLInputElement>) => {
    let value = event.target.value;
    setUsername(value);
  }
  
  const handlePassphrase = (event: React.ChangeEvent<HTMLInputElement>) => {
    let value = event.target.value;
    setPassphrase(value);
  }
  
  return (
    <main className="w-[100vw] h-[100vh] bg-black text-white lg:font flex min-h-screen flex-col items-center justify-between p-24">
      <div className="flex flex-row z-10 w-full max-w-5xl items-center justify-between font-mono text-sm p-8 border-slate-500 border bg-gray border-b-8 border-t-8 border-r-2 border-l-2 rounded-lg">
        <div className="flex flex-col w-[50%]">
          <input className="text-black mt-2 mb-2 p-1 bg-gray-300 rounded-sm" type="text" value={username} onChange={handleUsername}></input>
          <input className="text-black mt-2 mb-4 p-1 bg-gray-300 rounded-sm" type="text" value={passphrase} onChange={handlePassphrase}></input>
          <Button className="mt-2 mb-4 p-1 bg-gray-300 rounded-sm" onClick={handleUpload}></Button>
        </div>
        <div className="">
          <Button className="bg-gray-400 text-white" onClick={() => {console.log('bruh')}}>Upload Picture</Button>

        </div>
      </div>
    </main>
  );
}
