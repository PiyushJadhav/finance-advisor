import { useState } from "react";

export default function UploadForm({ onSubmit }) {
  const [file, setFile] = useState(null);
  const [amount, setAmount] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!file || !amount) {
      alert("Please upload a CSV and enter an amount");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("purchase_amount", amount);

    onSubmit(formData);
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Large Purchase Analyzer</h2>

      <input
        type="file"
        accept=".csv"
        onChange={(e) => setFile(e.target.files[0])}
      />

      <input
        type="number"
        placeholder="Purchase amount ($)"
        value={amount}
        onChange={(e) => setAmount(e.target.value)}
      />

      <button type="submit">Analyze</button>
    </form>
  );
}
