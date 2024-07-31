import Image from "next/image";
import Link from "next/link";
import Chat from "../../components/chat";
import axios from "axios";

const fetchData = async (id: string) => {
  const queryData = await axios.get(
    "http://api.nsf.gov/services/v1/awards.json",
    {
      params: {
        id: id,
        printFields:
          "rpp,offset,agency,awardAgencyCode,fundsObligatedAmt,awardeeName,awardeeCity,awardeeCountryCode,awardeeStateCode,awardeeZipCode,date,pdPIName,dunsNumber,id,coPDPI,expDate,startDate,title,abstractText",
      },
    }
  );

  return queryData.data;
};

export default async function Award({ params }: any) {
  const { name } = params;
  const data = await fetchData(name);
  console.log(data.response);
  return (
    <div className="flex flex-col gap-5 h-screen p-12">
      <Chat />
      <Image src={"../logo.svg"} alt="NSF Logo" height={80} width={200} />
      <Link href={"/"} className="underline text-[#005EA2]">
        {" "}
        Back to Search
      </Link>
      <p className="italic">Award ID: {name}</p>
      <h1 className="text-5xl">{data.response.award[0].title}</h1>
      <h2 className="text-xl font-semibold text-[#005EA2]">
        {data.response.award[0].awardeeName}
      </h2>
      <p className="text-xl">{data.response.award[0].abstractText}</p>
    </div>
  );
}
