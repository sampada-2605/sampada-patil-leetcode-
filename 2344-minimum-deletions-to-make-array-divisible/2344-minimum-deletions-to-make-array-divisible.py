class Solution:
    def minOperations(self, nums: List[int], numsDivide: List[int]) -> int:
        gcd=numsDivide[0]
        for i in range(1,len(numsDivide)):
            gcd=math.gcd(gcd,numsDivide[i])
        nums.sort()
        for i in range(len(nums)):
            if gcd%nums[i]==0:
                return i
        return -1
        
        