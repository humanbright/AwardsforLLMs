import Image from "next/image";
import Search from "./components/search";

export default function Home() {
  return (
    <div className=" h-screen p-12">
      <Image src={"/logo.svg"} alt="NSF Logo" height={80} width={300} />
      <div className="flex items-center justify-center mt-32 flex-col">
        <h1 className=" font-bold text-7xl">Search Awards</h1>
        <Search />
      </div>
    </div>
  );
}
