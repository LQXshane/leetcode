# 3. Longest Substring Without Repeating Characters
# Classic Sliding Window
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # sliding window
        
        left, right = 0, 0
        dic = set()
        ans = 0
        while left < len(s) and right < len(s):
            if s[right] not in dic:
                dic.add(s[right])
                ans = max(ans, right - left + 1)
                right += 1
            else:
                dic.remove(s[left])
                left += 1
        return ans
# meet dup -> remove the far left
# no dup -> move right ptr as far as possible

# Approach 2: hashmap keeps the last occurance 

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest, left = 0, 0
        last = {} # marks the last occurance per each character
        
        for i, x in enumerate(s):
            if x in last and last[x] >= left:
                # e.g. abca
                # when you meet the second 'a'
                # move your left pointer to the next charater of the repeated 'a'- in this case 'b'
                # so that no repeating charaters will be there between i and left
                left = last[x] + 1
            last[x] = i
            longest = max(longest, i - left + 1)
        return longest
