class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix=0
        count=0
        hashmap={0:1}
        for num in nums:
            prefix+=num
            remainder=prefix%k
            if remainder in hashmap:
                count+=hashmap[remainder]
            hashmap[remainder]=hashmap.get(remainder,0)+1
        return count