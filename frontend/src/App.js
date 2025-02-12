import { useState, useEffect } from "react";
import { ethers } from "ethers";
import AIMLazyToken from "../contracts/AIMLazyToken.json";

const contractAddress = "0xYourDeployedContractAddress";

function App() {
    const [account, setAccount] = useState(null);
    const [balance, setBalance] = useState(0);

    useEffect(() => {
        async function loadBlockchainData() {
            const provider = new ethers.providers.Web3Provider(window.ethereum);
            const signer = provider.getSigner();
            const contract = new ethers.Contract(contractAddress, AIMLazyToken.abi, signer);
            const accounts = await provider.send("eth_requestAccounts", []);
            setAccount(accounts[0]);
            const balance = await contract.balanceOf(accounts[0]);
            setBalance(ethers.utils.formatEther(balance));
        }
        loadBlockchainData();
    }, []);

    return (
        <div>
            <h1>AIMLazy Token</h1>
            <p>Connected Wallet: {account}</p>
            <p>Balance: {balance} AIML</p>
        </div>
    );
}

export default App;
