"""
Two Sum

Given an array of integers, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.

You may assume that each input would have exactly one solution.

Input: numbers={2, 7, 11, 15}, target=9
Output: index1=1, index2=2
"""


class Solution:
    def twoSum(self, numbers, target):
        num_map = {}

        for i in range(len(numbers)):
            num = numbers[i]
            if num in num_map:
                num_map[num].append(i)
            else:
                num_map[num] = [i]

        if len(num_map) > 0:
            for i in range(len(numbers)):
                num = numbers[i]
                index_list = num_map.get(target - num)

                if not index_list:
                    continue

                if len(index_list) == 2 and index_list[0] == i and index_list[1] > i:
                    return tuple(i + 1 for i in index_list)
                elif index_list[0] > i:
                    return (i + 1, index_list[0] + 1)


if __name__ == '__main__':
    solution = Solution()
    print solution.twoSum((0, 4, 3, 0), 0)

