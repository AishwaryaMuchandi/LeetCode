class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictio={}
        result=[]
        for i in range(len(nums)):
            dictio[nums[i]]=i

        for i in range(len(nums)):
            complement= target- nums[i]

            if complement in dictio and dictio[complement]!=i:
                return [i,dictio[complement]]