#爬楼梯    python3
class Solution:
    def climbStairs(self, n: int) -> int:
        fst = 1
        scd = 2
        res = 0
        for i in range(2, n):
            res = fst + scd
            fst = scd
            scd = res
        return max(n, res)