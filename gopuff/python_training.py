class Solution:
    """
    Solution is a class utilizing Kadane's algorithm, which finds the maximum possible sum of a contiguous subarray within an array with n elements, a = (a1, a2, a3, … , an).

    Methods:
            run(a): Returns maximum sum
    """

    def run(self, a: list[int]) -> int:
        """
        Return maximum contiguous subarray sum within list.
        """
        maximum_sum = a[0]
        maximum_ending = a[0]

        for i in range(1, len(a)):
            maximum_ending = max(maximum_ending + a[i], a[i])
            maximum_sum = max(maximum_sum, maximum_ending)

        return maximum_sum
