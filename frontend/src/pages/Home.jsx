import { useState } from "react";
import UploadForm from "../components/UploadForm";
import ResultCard from "../components/ResultCard";
import { analyzePurchase } from "../api/client";

export default function Home() {
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleAnalyze = async (formData) => {
    try {
      setLoading(true);
      const data = await analyzePurchase(formData);
      setResult(data);
    } catch (err) {
      alert("Error analyzing purchase");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div>
      <UploadForm onSubmit={handleAnalyze} />
      {loading && <p>Analyzing...</p>}
      <ResultCard result={result} />
    </div>
  );
}
