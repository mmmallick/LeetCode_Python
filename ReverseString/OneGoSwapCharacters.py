#brute force swap index for the whole array by looping until midpoint
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n=len(s)-1
        mid=int((n+1) / 2)
        for i in range(mid):
            s[n-i],s[i]=s[i],s[n-i]
        
