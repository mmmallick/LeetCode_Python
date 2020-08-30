Approach 2: Peak Valley Approach
class Solution(object):
    
    def maxProfit(self, prices):
        maximum=0
        peak=0
        valley=0
        index=0
        while(index<len(prices)-1):
            while (index<len(prices)-1 and prices[index]>= prices[index+1]):
                index+=1
            valley=prices[index]
            while (index<len(prices)-1 and prices[index]<= prices[index+1]):
                index+=1
            peak=prices[index]
            maximum=maximum+peak-valley
        
        return maximum
    
