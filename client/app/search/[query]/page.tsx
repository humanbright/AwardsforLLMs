import axios from "axios";

import Image from "next/image";
import Link from "next/link";

const fetchData = async (keyword: string) => {
  const queryData = await axios.get(
    "http://api.nsf.gov/services/v1/awards.json",
    {
      params: {
        keyword: keyword,
      },
    }
  );

  return queryData.data;
};

export default async function SearchResult({ params }: any) {
  const { query } = params; // Access the dynamic route parameter

  const data = await fetchData(query);
  console.log(data.response);

  return (
    <div className="p-12">
      <Image src={"/logo.svg"} alt="NSF Logo" height={80} width={300} />
      <div className=" ml-8 flex items-center p-16">
        <h1 className="mr-auto text-4xl font-kyiv  ">Searching for: {query}</h1>
      </div>
      <div className="flex items-start">
        <div className="ml-8 h-screen  border-r-4 border-r-black font-old text-2xl p-10  drop-shadow-xl">
          <h1>Filtering</h1>
        </div>
        <div className="w-full">
          <div className="flex  w-full p-12 flex-col ">
            <h1 className="text-4xl mb-4 font-semibold">Awards</h1>
            {data.response.award.slice(0, 7).map((res: any, i: any) => (
              <div key={i} className="mb-4 py-4 px-2 border-b-2 border-b-black">
                <h1 className="text-3xl text-blue-600 mb-4">
                  <Link href={`/`} passHref>
                    {res.title}
                  </Link>
                </h1>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
