#14. Longest Common Prefix
'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
Note:

All given inputs are in lowercase letters a-z.
'''
class Solution(object):
    def longestCommonPrefix(self, strs):
        shortest_word=''
        answer=''
        for n in strs: #find the shortest word way3
            if len(n)>len(shortest_word):
                shortest_word=n
        short_len=len(shortest_word)
        n=int()
        if len(strs)==1: return strs[0]
        elif len(strs)==0: return answer
        else:
            for i in range(short_len):
                temp=strs[0][:i+1]
                for j in range(len(strs)):
                    if temp==strs[j][:i+1]:
                        n+=1
                answer=temp if n==j+1 else answer
                temp=[];n=0
        return answer