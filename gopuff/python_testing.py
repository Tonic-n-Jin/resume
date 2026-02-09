from typing import List

import pytest


class Solution:
    """
    Longest Increasing Subsequence (LIS) with Binary Search.

    Time  : O(nlog(n))
    Space : O(n)
    """

    def run(self, sequence: List[int]) -> int:
        k = [sequence[0]]
        for i in sequence[1:]:
            if i > k[-1]:
                k.append(i)
            else:
                left, right = 0, len(k) - 1
                while left < right:
                    mid = (left + right) // 2
                    if k[mid] < i:
                        left = mid + 1
                    else:
                        right = mid
                k[left] = i
        return len(k)

    @pytest.mark.parametrize(
        "parameters,expected_output",
        [
            ([10, 9, 2, 5, 3, 7, 101, 18], 4),
            ([0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], 6),
        ],
    )
    def test_run(self, parameters: list[int], expected_output: int):
        solution = Solution()
        assert solution.run(parameters) == expected_output
