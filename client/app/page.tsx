import Image from "next/image";

export default function Home() {
  return (
   <div className="flex h-screen items-center justify-center">
    <Image src={'/logo.svg'} alt="NSF Logo" />
      <h1>AWARDS</h1>
   </div>
  );
}
