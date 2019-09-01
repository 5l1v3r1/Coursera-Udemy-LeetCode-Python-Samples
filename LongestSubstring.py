#3. Longest Substring Without Repeating Characters
'''
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        temp=''
        ans=''
        for i in range(len(s)):
            if s[i] not in temp:
                temp=temp+s[i]
            else:
                if len(ans)<len(temp):
                    ans=temp
                temp = temp[temp.index(s[i])+1::] + s[i]
        return max(len(temp),len(ans))
Solution.lengthOfLongestSubstring(0,"stsskks")
Solution.lengthOfLongestSubstring(0,'anviaj')