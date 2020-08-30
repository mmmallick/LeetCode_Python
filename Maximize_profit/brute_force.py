#Mehmood Mallick
#brute force solution that uses double loop, and recursion to find the most profitable
class Solution(object):
    
    def maxProfit(self, prices):
        return calculate(prices,0)
    
def calculate(prices,s):
    if(s>=len(prices)):
        return 0
        """
        :type prices: List[int]
        :rtype: int
        """
    profit=0
    profits=[]
    maxi=0
    for i in range(s,len(prices)):
        maxprofit=0
        for j in range(s+1,len(prices)):
            if (prices[i]<prices[j]):
                profit=calculate(prices,j+1)+(prices[j]-prices[i])
                    
                if(profit > maxprofit):
                    maxprofit=profit
                        
        if(maxprofit>maxi):
            maxi=maxprofit
            
    return maxi
    
