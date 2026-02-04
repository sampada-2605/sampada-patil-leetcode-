class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxl = 0
        left = 0
        uniqset = set()

        for right in range(len(s)):
            while s[right] in uniqset:
                uniqset.remove(s[left])
                left += 1

            uniqset.add(s[right])
            maxl = max(maxl, right - left + 1)

        return maxl






        