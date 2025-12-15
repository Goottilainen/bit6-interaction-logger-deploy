import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [result, setResult] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (!text.trim()) return;

    setLoading(true);
    setResult("");

    try {
      const response = await fetch("http://localhost:8000/process", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      const data = await response.json();
      setResult(data.result);
    } catch (error) {
      setResult("Error communicating with backend.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ maxWidth: "600px", margin: "40px auto", fontFamily: "Arial" }}>
      <h2>BIT6 Interaction Logger</h2>

      <p style={{ color: "#555" }}>
        This application demonstrates a simple frontend-to-backend interaction
        where user input is processed and stored by a backend service.
      </p>

      <textarea
        rows={4}
        style={{ width: "100%" }}
        placeholder="Write a short text..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <button
        onClick={handleSubmit}
        disabled={loading}
        style={{ marginTop: "10px" }}
      >
        {loading ? "Processing..." : "Submit"}
      </button>

      {result && (
        <div style={{ marginTop: "20px" }}>
          <strong>System Output:</strong>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
}

export default App;
