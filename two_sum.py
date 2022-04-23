"""
The Problem:

Given an array of integers nums and an integer target, 
return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, 
and you may not use the same element twice.

You can return the answer in any order.

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

"""

# A solution that works, but is not optimal by any stretch
def two_sum_slow(nums, target):
    for i in range(len(nums) - 1):
        for j in range(i+1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i,j]

"""
In worst case this is O(n^2) if the single solution exists
at nums[::-1], nums[::-2]

If this list of nums is sufficiently long this solution is awful
"""


# A much better solution
def two_sum(nums, target):
    # dictionary of {nums[index]: index} to store a history of possible partners
    # that add up to the target
    partner_value_dict = {}
    for index, num in enumerate(nums):
        # pair is the "partner" value that added to num equals our target
        pair = target - num
        # if we already placed "pair" in the dictionary then partner_value_dict[pair] 
        # and index are the indices of our solution
        if pair in partner_value_dict:
            return [partner_value_dict[pair], index]
        # we didn't find "pair" in the dictionary so let's add this key, value
        # pair of {nums[index]: index}
        else:
            partner_value_dict[num] = index

nums = [2,7,11,15]
target = 9

print(two_sum(nums, target))

"""
In worst case this is O(n) if the solution is at nums[::-1], nums[::-2]

Why does this work?

The key to the problem is that there is ALWAYS only 1 pair of numbers that satisfy 
the condition of adding together to be the target value.

We can assume that for all the numbers in the list (x1, x2, ... xn) that there exists 
a pair such that xa + xb = target

To solve this with a single pass of the list we can change the equation above to 
xa = target - xb and since we know the target as long as we maintain a record of 
all previous values in the list we can compare the current value (xa) to it's ONLY 
pair, if it exists, in record of all previous values (xb)

"""