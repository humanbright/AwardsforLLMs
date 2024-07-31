export default function SearchResult({ params }: any) {
  const { query } = params; // Access the dynamic route parameter

  return (
    <div className="h-screen flex items-center justify-center flex-col">
      <h1>User Profile</h1>
      <p>Dynamic Page for User ID: {query}</p>
    </div>
  );
}
