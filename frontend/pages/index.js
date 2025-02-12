import { useState } from 'react';
import axios from 'axios';
import Navbar from '../components/Navbar';
import Footer from '../components/Footer';

export default function Home() {
    const [input, setInput] = useState('');
    const [response, setResponse] = useState('');

    const fetchResponse = async () => {
        const res = await axios.get(`/api/lazy-response?user_input=${input}`);
        setResponse(res.data.response);
    };

    return (
        <div>
            <Navbar />
            <h1>AIMLazy AI</h1>
            <input 
                type="text" 
                value={input} 
                onChange={(e) => setInput(e.target.value)} 
                placeholder="Ask something..." 
            />
            <button onClick={fetchResponse}>Ask AI</button>
            <p>{response}</p>
            <Footer />
        </div>
    );
}
