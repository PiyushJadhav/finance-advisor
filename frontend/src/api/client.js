const API_BASE = "http://localhost:8000";

export async function analyzePurchase(formData) {
  const response = await fetch(`${API_BASE}/analyze`, {
    method: "POST",
    body: formData,
  });

  if (!response.ok) {
    throw new Error("Failed to analyze purchase");
  }

  return response.json();
}

export async function healthCheck() {
  const response = await fetch(`${API_BASE}/health`);
  return response.json();
}
