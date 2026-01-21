export default function ResultCard({ result }) {
  if (!result) return null;

  return (
    <div className="result-card">
      <h3>Recommendation</h3>
      <p>
        <strong>Status:</strong> {result.recommendation}
      </p>

      <h4>Summary</h4>
      <p>{result.summary}</p>

      <h4>Metrics</h4>
      <ul>
        <li>Savings Change: ${result.savings_change}</li>
        <li>Lowest Balance: ${result.lowest_balance}</li>
        <li>Risk Level: {result.risk_level}</li>
      </ul>
    </div>
  );
}
