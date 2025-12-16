import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendPrompt = async () => {
    if (!text.trim()) {
      setResponse("Please write something first.");
      return;
    }

    setLoading(true);
    setResponse("");

    try {
      const res = await fetch(
        "https://ai-webapp-backend.onrender.com/process",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ text }),
        }
      );

     
      if (!res.ok) {
        const errorText = await res.text();
        throw new Error(errorText || "Server error");
      }

      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      console.error(error);
      setResponse("❌ Error connecting to backend");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial", maxWidth: "600px" }}>
      <h2>AI Web App</h2>

      <textarea
        rows="4"
        style={{ width: "100%" }}
        placeholder="Write your prompt here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
      />

      <br /><br />

      <button onClick={sendPrompt} disabled={loading}>
        {loading ? "Sending..." : "Send"}
      </button>

      <br /><br />

      {response && (
        <>
          <h3>AI Response:</h3>
          <p>{response}</p>
        </>
      )}
    </div>
  );
}

export default App;
