class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s=list(s)
        s=sorted(s)
        t=list(t)
        t=sorted(t)
        return t==s
