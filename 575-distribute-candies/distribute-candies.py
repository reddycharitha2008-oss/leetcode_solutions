class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        s=set(candyType)
        if len(candyType)//2>=len(s):
            return len(s)
        else:
            return len(candyType)//2


