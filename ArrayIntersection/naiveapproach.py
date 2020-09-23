class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums3=[]
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if(nums1[i]==nums2[j]):
                    temp=nums2[j]
                    nums2[j]=None
                    nums3.append(temp)
                    break
        return nums3
                    
