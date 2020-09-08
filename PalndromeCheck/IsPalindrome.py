class Solution(object):
    def isPalindrome(self, s) :
        s = ''.join(filter(unicode.isalnum, s))
        s=s.upper()
        print(s)
        return s == s[::-1]
