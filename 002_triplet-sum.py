"""
Given an array of distinct elements. The task is to find triplets in the array whose sum is zero.

Examples: Input: arr|] = (0, -1, 2, -3, 1}
Output: (0 -1 1), (2 -3 1)
Explanation: The triplets with zero sum are 0 + -1 + 1 = 0 and 2 + - 3 + 1 = 0

Input: arr] = {1, -2, 1, 0, 5}
Output: 1-2 1
Explanation: The triplets with zero sum is 1 + - 2 + 1 = 0
"""


def triplet_sum(arr, target = 0):

    for i in range(len(arr)-1):
        j = i+1
        k = len(arr) - 1
        while(j < k):
            if arr[j] + arr[k] == arr[i]:
                return 1
            elif arr[j] + arr[k] < arr[i]:
                j += 1
            elif arr[j] + arr[k] > arr[i]:
                k -= 1
        return -1


arr = [ -1,0, 2, -3, 1]
print( triplet_sum(arr) )