const hre = require("hardhat");

async function main() {
    const AIMLazyToken = await hre.ethers.getContractFactory("AIMLazyToken");
    const token = await AIMLazyToken.deploy("0xYourFeeRecipientAddress");

    await token.deployed();
    console.log("AIMLazy deployed to:", token.address);
}

main().catch((error) => {
    console.error(error);
    process.exit(1);
});
