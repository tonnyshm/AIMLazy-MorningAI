const { ethers } = require("hardhat");

async function main() {
    const AIMLazy = await ethers.getContractFactory("AIMLazy");
    const aimLazy = await AIMLazy.deploy();

    console.log("AIMLazy contract deployed to:", aimLazy.address);
}

main()
    .then(() => process.exit(0))
    .catch((error) => {
        console.error(error);
        process.exit(1);
    });
