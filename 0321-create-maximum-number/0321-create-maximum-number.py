class Solution:
    def maxNumber(self, nums1, nums2, k):

        def maximum(nums, k):
            result = []
            remove = len(nums) - k

            for num in nums:
                while result and remove > 0 and result[-1] < num:
                    result.pop()
                    remove -= 1

                result.append(num)

            return result[:k]

        def combine(a, b):
            result = []

            while len(a) > 0 or len(b) > 0:

                if a > b:
                    result.append(a[0])
                    a.pop(0)
                else:
                    result.append(b[0])
                    b.pop(0)

            return result

        answer = []

        for i in range(k + 1):

            if i <= len(nums1) and k - i <= len(nums2):

                a = maximum(nums1, i)
                b = maximum(nums2, k - i)

                current = combine(a, b)

                if current > answer:
                    answer = current

        return answer