import { DropdownMenuCheckboxItemProps } from "@radix-ui/react-dropdown-menu";
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
  DropdownMenuItem,
} from "@/components/ui/dropdown-menu";
import { useState } from "react";

import { DropdownMenuCheckboxes } from "./ui/dropdown";

export enum SearchMethod {
  SIMPLE = "Simple",
  ADVANCED = "Advanced",
  AI = "AI",
}

const Search: React.FC = () => {
  const [searchMethod, setSearchMethod] = useState<SearchMethod>(
    SearchMethod.SIMPLE
  );
  return (
    <div className="flex items-center justify-center text-xl mt-8 w-full">
      <DropdownMenuCheckboxes
        searchMethod={searchMethod}
        setSearchMethod={setSearchMethod}
      />
      <input
        className="py-3 px-4 rounded-r-lg border border-black outline-none w-1/3 mr-6"
        placeholder="Water Vapor Research..."
      />
      <button className="bg-[#005EA2] px-8 py-3 rounded-lg text-white">
        SEARCH
      </button>
    </div>
  );
};

export default Search;
