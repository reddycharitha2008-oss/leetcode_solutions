class Solution:
    def mySqrt(self, x: int) -> int:
        if X<2:
            return x
        l=1
        h=x
        ans=0
        while l<=h:
            mid=(l+h)//2
            if mid<=x//mid:
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans 