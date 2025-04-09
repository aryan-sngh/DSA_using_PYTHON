#max subarray
def max_subarray(nums,k):
    if len(nums)<k:
        return -1
    
    windowSum = sum(nums[:k])
    maxSum = windowSum
    left = 0
    for right in range(k,len(nums)):
        windowSum = windowSum -nums[left]+nums[right]
        left +=1
        maxSum = max(windowSum,maxSum)
        
    return maxSum

# nums = [1,12,-5,-6,50,3] 
# k = 4
# print(max_subarray([2, 1, 5, 1, 3, 2],3))

        
def longestSubstring(s):
    unquiSet = set()
    left = 0
    maxSum = 0
    
    for right in range(len(s)):
        while s[right] in unquiSet:
            unquiSet.remove(s[left])
            left += 1
        
        unquiSet.add(s[right])
        maxSum = max(maxSum,right-left+1)
        
    return maxSum

print(longestSubstring("abcabcbb"))
        
        
        
    