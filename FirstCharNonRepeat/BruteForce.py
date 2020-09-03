class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if(len(s)==1):
            return 0
        n=len(s)
        listChar={i:s.count(i) for i in s}
             
     
        for i in range(n): 
            if listChar[s[i]] == 1: 
                return i 
        return -1
        
