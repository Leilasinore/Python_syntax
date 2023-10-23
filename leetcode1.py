# class Solution:
#leetcode solution two sum problem solution,,
def twoSum( nums, target):
        numshashtable = {}
        for i,num in enumerate(nums):
            compliment= target-num
            if compliment in numshashtable:
               return [numshashtable[compliment], i]

            else: numshashtable[num] = i


        return []

#To run the solution above just call the function and give it two parameters,an array of nums and an integer as a target sum as illustrated below

indicesOfTwoNumbers=twoSum([3,3],6)
print(indicesOfTwoNumbers)