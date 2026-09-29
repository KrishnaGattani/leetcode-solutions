class Solution:
    def maxNumber(self, nums1, nums2, k):

        def getMax(nums, k):
            stack = []
            remove = len(nums) - k

            for num in nums:
                while stack and remove > 0 and stack[-1] < num:
                    stack.pop()
                    remove -= 1

                stack.append(num)

            return stack[:k]

        def merge(a, b):
            result = []

            while a or b:
                if a > b:
                    result.append(a.pop(0))
                else:
                    result.append(b.pop(0))

            return result

        answer = []

        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            a = getMax(nums1, i)
            b = getMax(nums2, k - i)

            current = merge(a[:], b[:])

            if current > answer:
                answer = current

        return answer