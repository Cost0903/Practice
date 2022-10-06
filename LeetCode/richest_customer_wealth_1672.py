class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = []
        for account in range(len(accounts)):
            result.append(sum(accounts[account]))
        return max(result)