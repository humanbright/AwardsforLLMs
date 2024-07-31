"use client";

import Image from "next/image";
import Search from "./components/search";
import { useState } from "react";
import { DropdownMenuCheckboxes } from "./components/ui/dropdown";

export default function Home() {
  const [active, setActive] = useState(false);
  const [expired, setExpired] = useState(false);


  return (
    <div className=" h-screen p-12">
      <Image src={"/logo.svg"} alt="NSF Logo" height={80} width={300} />
      <div className="flex items-center justify-center mt-32 flex-col">
        <h1 className=" font-bold text-7xl">Search Awards</h1>
        <Search />
        <div className="flex items-center mt-6 text-2xl justify-center">
          <div className="flex items-center justify-center mr-8">
            <input type="checkbox" className="mr-2 scale-150" />
            <h1>Active Awards</h1>
          </div>
          <div className="flex items-center justify-center">
            <input type="checkbox" className="mr-2 scale-150" />
            <h1>Expired Awards</h1>
          </div>
        </div>
      </div>
    </div>
  );
}
