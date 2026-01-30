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
      {result.similar_decisions && result.similar_decisions.length > 0 && (
        <>
          <h4>Similar Past Decisions</h4>
          <div className="similar-decisions">
            {result.similar_decisions.map((decision, index) => (
              <div key={index} className="decision-item">
                <p>
                  <strong>Purchase Amount:</strong> $
                  {decision.purchase_amount.toFixed(2)}
                </p>
                <p>
                  <strong>Risk Level:</strong>
                  <span
                    className={`risk-badge ${decision.risk_level.toLowerCase()}`}
                  >
                    {decision.risk_level}
                  </span>
                </p>
                <p>
                  <strong>Outcome:</strong> {decision.outcome}
                </p>
              </div>
            ))}
          </div>
        </>
      )}
    </div>
  );
}
