"use client";

import * as React from "react";
import { DropdownMenuCheckboxItemProps } from "@radix-ui/react-dropdown-menu";
import { Dispatch, SetStateAction } from "react";
import { SearchMethod } from "../search";
import {
  DropdownMenu,
  DropdownMenuCheckboxItem,
  DropdownMenuContent,
  DropdownMenuLabel,
  DropdownMenuSeparator,
  DropdownMenuTrigger,
} from "@/components/ui/dropdown-menu";

type Checked = DropdownMenuCheckboxItemProps["checked"];

export const DropdownMenuCheckboxes: React.FC<{
  searchMethod: SearchMethod;
  setSearchMethod: Dispatch<SetStateAction<SearchMethod>>;
}> = ({ searchMethod, setSearchMethod }) => {
  const [showStatusBar, setShowStatusBar] = React.useState<Checked>(true);
  const [showActivityBar, setShowActivityBar] = React.useState<Checked>(false);
  const [showPanel, setShowPanel] = React.useState<Checked>(false);

  return (
    <DropdownMenu>
      <DropdownMenuTrigger asChild>
        <button className="py-3  text-white w-1/8  px-4 border-[#005EA2] rounded-l-lg bg-[#005EA2]">
          {searchMethod}
        </button>
      </DropdownMenuTrigger>
      <DropdownMenuContent className="w-56">
        <DropdownMenuLabel>Search Method</DropdownMenuLabel>
        <DropdownMenuSeparator />
        <DropdownMenuCheckboxItem
          checked={searchMethod === SearchMethod.SIMPLE}
          onCheckedChange={() => setSearchMethod(SearchMethod.SIMPLE)}
        >
          Simple
        </DropdownMenuCheckboxItem>
        <DropdownMenuCheckboxItem
          checked={searchMethod === SearchMethod.ADVANCED}
          onCheckedChange={() => setSearchMethod(SearchMethod.ADVANCED)}
        >
          Advanced
        </DropdownMenuCheckboxItem>
      </DropdownMenuContent>
    </DropdownMenu>
  );
};
