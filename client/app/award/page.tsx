"use client"
import Image from "next/image";
import Link from "next/link";

const Award = () => {
    return (
        <div className="flex flex-col gap-5 h-screen p-12">
            <Image src={"../logo.svg"} alt="NSF Logo" height={80} width={200} />
            <Link href={"/"} className="underline text-[#005EA2]"> Back to Search</Link>
            <p className="italic">Award #2212721</p>
            <h1 className="text-5xl">Engineering the Inclusive Mindset for the Future: A Blueprint for Systemic Change in Engineering Education</h1>
            <h2 className="text-xl font-semibold text-[#005EA2]">AMERICAN SOCIETY FOR ENGINEERING EDUCATION</h2>
            <div className="flex "></div>
        </div>
    );
}

export default Award;