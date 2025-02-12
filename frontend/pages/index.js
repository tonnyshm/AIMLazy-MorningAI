import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const getLazyResponse = async () => {
    const res = await axios.get(`http://localhost:8000/lazy-response?user_input=${input}`);
    setResponse(res.data.response);
  };

  return (
    <div className="container">
      <h1>AIMLazy AI Assistant</h1>
      <input type="text" value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={getLazyResponse}>Ask AI</button>
      <p>{response}</p>
    </div>
  );
}
