// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract AIMLazy {
    mapping(address => uint256) public balances;

    event TokensMinted(address indexed user, uint256 amount);
    
    function mint(uint256 amount) public {
        balances[msg.sender] += amount;
        emit TokensMinted(msg.sender, amount);
    }
    
    function checkBalance() public view returns (uint256) {
        return balances[msg.sender];
    }
}
