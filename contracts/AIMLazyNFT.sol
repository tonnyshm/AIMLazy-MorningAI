// SPDX-License-Identifier: MIT
pragma solidity ^0.8.19;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";
import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

contract AIMLazyToken is ERC20, Ownable, ReentrancyGuard {
    uint256 public constant INITIAL_SUPPLY = 1_000_000 * 10**18; // 1 Million AIMLazy
    uint256 public transactionFee = 2; // 2% fee per transaction
    address public feeRecipient;

    mapping(address => uint256) public stakingBalance;
    mapping(address => uint256) public stakingTimestamp;
    uint256 public stakingRewardRate = 10; // 10% annual reward

    event Staked(address indexed user, uint256 amount);
    event Unstaked(address indexed user, uint256 amount);

    constructor(address _feeRecipient) ERC20("AIMLazy", "AIML") {
        _mint(msg.sender, INITIAL_SUPPLY);
        feeRecipient = _feeRecipient;
    }

    function transfer(address recipient, uint256 amount) public override returns (bool) {
        uint256 feeAmount = (amount * transactionFee) / 100;
        uint256 transferAmount = amount - feeAmount;

        _transfer(_msgSender(), feeRecipient, feeAmount);
        _transfer(_msgSender(), recipient, transferAmount);
        return true;
    }

    function stake(uint256 amount) external nonReentrant {
        require(amount > 0, "Cannot stake 0 tokens");
        require(balanceOf(msg.sender) >= amount, "Insufficient balance");
        
        _transfer(msg.sender, address(this), amount);
        stakingBalance[msg.sender] += amount;
        stakingTimestamp[msg.sender] = block.timestamp;
        emit Staked(msg.sender, amount);
    }

    function unstake() external nonReentrant {
        uint256 stakedAmount = stakingBalance[msg.sender];
        require(stakedAmount > 0, "No staked tokens");
        
        uint256 stakingDuration = block.timestamp - stakingTimestamp[msg.sender];
        uint256 reward = (stakedAmount * stakingRewardRate * stakingDuration) / (365 days * 100);

        stakingBalance[msg.sender] = 0;
        _mint(msg.sender, reward);
        _transfer(address(this), msg.sender, stakedAmount);
        emit Unstaked(msg.sender, stakedAmount);
    }
}
