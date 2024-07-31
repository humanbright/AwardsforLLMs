const Search: React.FC = () => {
  return (
    <div className="flex items-center justify-center text-xl mt-8 w-full">
      <button className="py-3  text-white w-1/8  px-4 border-[#005EA2] rounded-l-lg bg-[#005EA2]">
        Simple Search
      </button>
      <input className="py-3 rounded-r-lg border border-black outline-none w-1/3 mr-6" />
      <button className="bg-[#005EA2] px-4 py-3 rounded-lg text-white">
        SEARCH
      </button>
    </div>
  );
};

export default Search;