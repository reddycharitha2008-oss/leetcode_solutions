class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        mp = {0: -1}

        for i in range(len(nums)):
            prefix += nums[i]
            remainder = prefix % k

            if remainder in mp:
                if i - mp[remainder] >= 2:
                    return True
            else:
                mp[remainder] = i

        return False