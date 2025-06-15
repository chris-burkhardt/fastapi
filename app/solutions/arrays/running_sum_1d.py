from typing import List

# Ref: API Request Format
"""
{
    "problem_id": "sum_1d",
    "category": "arrays",
    "input_data": {
        "nums": [1, 2, 3, 4]
    }
}
"""

# Problem Description
"""
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/

Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).
Return the running sum of nums.

Example 1:
Input: nums = [1,2,3,4]
Output: [1,3,6,10]
Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

Example 2:
Input: nums = [1,1,1,1,1]
Output: [1,2,3,4,5]
Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].

Example 3:
Input: nums = [3,1,2,10,1]
Output: [3,4,6,16,17]

Constraints:
1 <= nums.length <= 1000
-10^6 <= nums[i] <= 10^6
"""

# Solution Notes
"""
In-place modification approach:
For nums = [1, 2, 3, 4]:
i = 1: nums[1] = nums[1] + nums[0] → 2 + 1 = 3 → nums = [1, 3, 3, 4]
i = 2: nums[2] = nums[2] + nums[1] → 3 + 3 = 6 → nums = [1, 3, 6, 4]
i = 3: nums[3] = nums[3] + nums[2] → 4 + 6 = 10 → nums = [1, 3, 6, 10]
"""

def solve(input_data: dict) -> List[int]:
    """
    Args:
        input_data: A dictionary containing:
            - nums: List[int] - The input array
    
    Returns:
        List[int]: The running sum array
    """
    nums = input_data["nums"]
    
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    
    return nums 