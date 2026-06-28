class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack = []
        mp = {}

        # Next greater for every element in nums2
        for i in range(len(nums2) - 1, -1, -1):

            while stack and stack[-1] <= nums2[i]:
                stack.pop()

            if stack:
                mp[nums2[i]] = stack[-1]
            else:
                mp[nums2[i]] = -1

            stack.append(nums2[i])

        ans = []

        for num in nums1:
            ans.append(mp[num])

        return ans
