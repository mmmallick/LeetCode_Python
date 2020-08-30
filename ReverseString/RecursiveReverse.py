#recursive solution untile reach mid point by using pointers from two ends left, and right
class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        n =len(s)
        def recursiveReverse(left,right):
            if left<right:
                s[left],s[right]=s[right],s[left]
                recursiveReverse(left+1,right-1)
            
        recursiveReverse(0,n-1)
        
