class Solution(object):
    def climbStairs(self, n):
        p=0
        q=0
        r=1
        for i in range(1,n+1):
            p=q
            q=r
            r=p+q
        return r
sol=Solution()
print(sol.climbStairs(5))