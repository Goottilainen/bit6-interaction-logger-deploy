import { useState } from "react";

function App() {
  const [text, setText] = useState("");
  const [response, setResponse] = useState("");
  const [loading, setLoading] = useState(false);

  const sendPrompt = async () => {
    setLoading(true);
    setResponse("");

    try {
      const res = await fetch("http://127.0.0.1:5000/process", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ text }),
      });

      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      setResponse("Error connecting to backend");
    }

    setLoading(false);
  };

  return (
    <div style={{ padding: "2rem", fontFamily: "Arial" }}>
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
