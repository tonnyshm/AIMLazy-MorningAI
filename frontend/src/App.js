import { useState } from "react";

function LazyAIChat() {
  const [input, setInput] = useState("");
  const [response, setResponse] = useState("");

  const getLazyReply = async () => {
    const res = await fetch(`http://localhost:8000/lazy-response?user_input=${input}`);
    const data = await res.json();
    setResponse(data.response);
  };

  return (
    <div>
      <h1>AIMLazy Chat</h1>
      <input value={input} onChange={(e) => setInput(e.target.value)} placeholder="Ask me anything..." />
      <button onClick={getLazyReply}>Ask</button>
      <p>{response}</p>
    </div>
  );
}

export default LazyAIChat;
