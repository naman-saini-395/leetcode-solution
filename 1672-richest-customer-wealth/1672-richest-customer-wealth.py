class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        output = []
        for acc in accounts:
            output.append(sum(acc))
        return max(output)
        