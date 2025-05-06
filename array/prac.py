from collections import deque
# #longestString

# def longestString(arr):
#     longestStr = ""
    
#     for i in range(0,len(arr)):
#         currentStr = arr[i]
#         if len(currentStr) > len(longestStr):
#             longestStr = currentStr
    
#     return longestStr


# arr = ["aryan","chaudhary","boy"]
# # print(longestString(arr))
            
# def findZeroTriplets(arr):
#     found = False
    
#     for i in range(0,len(arr)-2):
#         for j in range(i+1,len(arr)-1):
#             for k in range(j+1,len(arr)):
#                 if arr[i]+arr[j]+arr[k] == 0:
#                     print(arr[i],arr[j],arr[k])
#                     found = True
#     if not found:
#         print("no triplet")
        
# arr = [0,-1,2,-3,1]
# print(findZeroTriplets(arr))


# #findMaxMin


# def maxMin(arr):
#     max = arr[0]
#     min = arr[0]
    
#     for i in range(1,len(arr)):
#         if arr[i]>max:
#             max = arr[i]
#         elif arr[i]<min:
#             min = arr[i]
            
#     return max,min

# arr = [6,2,1,4,5]
# print(maxMin(arr))

#remove given element 

# def remove_element(arr,val):
#     i=0 
#     for j in range(len(arr)):
#         if arr[j] != val:
#             arr[i] = arr[j]
#             i+=1
#     return i


# arr = [1,2,3,4,5,6,6,2]
# len1 = remove_element(arr,2)
# print(arr[:len1])
        
        
#two sum

def twoSum(arr,target):
    check = False
    for i in range(0,len(arr)-1):
        for j in range(i+1,len(arr)):
            if arr[i]+arr[j] == target:
                print(i,j)
                check = True
    if not check:
        print("not found")
        
# twoSum([1,2,3,4,5,9],7)


#another twoSUm

def twoSum2(arr,target):
    numDict = {}
    for i in range(len(arr)):
        num = arr[i]
        compliment = target-num
        
        if compliment in numDict:
            return numDict[compliment],i
        numDict[num] = i
        
    return []

# print(twoSum2([1,2,3,4,5,9],10))
        

#find Duplicate
def findDuplicate(nums):
    numDict = {}
    for num in nums:
        if num in numDict:
            numDict[num]+=1
        else:
            numDict[num] = 1
            
    Duplicate = []
    for key in numDict:
        if numDict[key] > 1:
            Duplicate.append(int(key))
    return Duplicate
            
# print(findDuplicate([1,2,3,4,5,5,6,7,6]))

#itemInCommon
def itemInCommon(arr1,arr2):
    obj = {}
    for item in arr1:
        obj[item] = True
    
    for item in arr2:
        if item in obj:
            return True
    return False

# print(itemInCommon([1,2,3],[1,5,7]))

#two sum using two pointer approch

def twoSumtpa(arr,target):
    low = 0
    high = len(arr)-1
    while low<high:
        sum = arr[low] + arr[high]
        if sum == target:
            return low,high
        if sum>target:
            high -= 1
        elif sum<target:
            low +=1 
        
# print(twoSumtpa([1,2,3,4,5,6,7],9))

#binarySearch two pointer approach

def binaryseach(arr,target):
    arr.sort()
    print(arr)
    low = 0
    high = len(arr)-1
    while low<=high:
        mid = low+high//2
        if arr[mid] == target:
            return mid
        if arr[mid]>target:
            high -= 1
        elif arr[mid]<target:
            low +=1
            
# print(binaryseach([4,2,5,1,8,3,2],8))

#binary search using recursion

def bsearch(arr,low,high,target):
    
    if low>high:
        return -1
    mid = high+low//2
    if arr[mid] == target:
        return mid
    elif target>arr[mid]:
        return bsearch(arr,mid+1,high,target)
    else:
        return bsearch(arr,low,mid-1,target)
    
arr = [0,1,2,3,4,5,6,7,8]
low = 0
high = len(arr)-1      
# print(bsearch(arr,low,high,6))


#fibonici series
def fib(n):
    fiba = [0,1]
    for i in range(2,n+1):
        x = fiba[i-1] + fiba[i-2]
        fiba.append(x)
    for i in fiba:
        print(i,end=",")    
        
# fib(10)

def fib2(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib2(n-1)+fib2(n-2)

# print(fib2(7))


def findDuplicate2(nums):
    table = {}
    for i in nums:
        if i in table:
            return True
        else:
            table[i] = 1
    return False


# print(findDuplicate2([1,2,3,4,4]))            

#removeDuplicate:

def removeDuplicate2(nums):
    slow = 0
    fast = slow+1
    i = 0
    while i<=len(nums):
        if nums[slow] != nums[slow+1]:
            slow = fast
            fast += 1
        else:
            nums.pop(slow)
        i+= 1
    return nums
# print(removeDuplicate2([1,2,2,3,3,4,4,4,5]))

def reverse(x):
    rev = 0
    og = x
    if og<0:
        x = x*(-1)

    while x>0:
        u = x%10
        rev = rev*10+u
        x = x//10
    
    if og<0:
        rev = rev*(-1)
        
    if rev < -2**31 or rev > 2**31-1:
        return 0
         
    return rev


# print(reverse(1534236469))

#marge two sorted array
def merge(arr1,arr2):
    for i in arr2:
        arr1.append(i)
    
    list3 = sorted(arr1)
    
    return list3

# print(merge([1,2,3,4,5,6],[1,2,3,4,5,6,7,8]))

#max subarray k 
def max_subarray(nums,k):
    n = len(nums)
    if k>n:
        return -1
    
    current_sum = sum(nums[:k])        
    max_sum = current_sum
    
    for i in range(k,n):
        current_sum += nums[i]-nums[i-k]
        max_sum = max(max_sum,current_sum)
    
    return max_sum

# print(max_subarray([2, 1, 5, 1, 3, 2],3))

#average of max subarray:

def max_average(nums,k):
    currentSum = sum(nums[:k])
    maxSum = currentSum
    
    for i in range(k,len(nums)):
        currentSum = currentSum -nums[i-k] + nums[i]
        maxSum = max(currentSum,maxSum)
        
    return maxSum/k
# nums = [1,12,-5,-6,50,3] 
# k = 4
# print(max_average(nums,k))        
     

#move zeros
def moveZeros(nums):
    l = 0
    for r in range(0,len(nums)):
        if nums[r] != 0:
            temp = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            
            l+=1
    return nums


# print(moveZeros([0,0,1,0,3,12]))

#or
def moveZeroes2(nums):
    l = 0
    for _ in range(0,len(nums)):
        if nums[l] == 0:
            nums.append(nums.pop(l))
        if nums[l]!= 0:
            l+=1
    return nums

#reverse string in list:

def reverseString(s):
    reverseText = []
    while len(s)>0:
        reverseText.append(s.pop())
    
    return reverseText

#or
def reverseString2(s):
    for _ in range(len(s)):
        s.append(s.pop())
    return s
 
#or
def reverseString3(s):
    l = 0
    r = len(s)-1
    while l<=r:
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l+=1
        r-=1
    return s
   
s = ["A","R","Y","A","N"]
# print(reverseString3(s))

#square of a Sorted Array
def sortedSquare(nums):
    l = 0
    while l<len(nums):
        nums[l] = nums[l]**2
        l+=1
    return sorted(nums)

#or
def sortedSquare2(nums):
    for i in range(len(nums)):
        nums[i] = nums[i]**2
    
    return sorted(nums)
        
        

nums = [-4,-1,0,3,10]
# print(sortedSquare(nums))

def twoSum3(numbers, target):
        
        l = 0
        r = len(numbers)-1
        while l<r:
            sum = numbers[l]+numbers[r]
            if sum == target:
                return [l+1,r+1]
            if sum>target:
                r-=1
            else:
                l+=1
        
                
# print(twoSum3([2,7,11,15],9))    

#roman to integer
def romanToint(s):
    dict = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    
    left = 0
    result = 0
    n = len(s)
    
    while left<n:
        if left+1<n and dict[s[left]]<dict[s[left+1]]:
            result+=dict[s[left+1]]-dict[s[left]]
            left+=2
        else:
            result+=dict[s[left]]
            left+=1
            
    return result

# print(romanToint("MCMXCIV"))


def singleNumber(nums):
    dict = {}
    for num in nums:
        if num in dict:
            dict[num]+=1
        else:
            dict[num] = 1
            
    for key in dict:
        if dict[key] == 1:
            return key


# Input: nums = [2,2,1]

# Output: 1

# print(singleNumber([4,1,2,1,2])

#Majority Element

def majorityElement(nums):
    dict = {}
    maxcount = 0
    for i in nums:
        if i in dict:
            dict[i]+=1
        else:
            dict[i] = 1
    # print(dict)        
    # for key in dict:
    #     if dict[key]>max:
    #         max = dict[key]
    # for key,value in dict.items():
    #     if value == max:
    #         return(key)
    maxcount = max(dict.values())
    for key,value in dict.items():
        if value == maxcount:
            return key
# print(majorityElement([2,2,1,1,1,2,2]))


#3 sum 

def sum3(nums):
    nums.sort()
    res = []
    
    for i in range(len(nums)):
        if i>0 and nums[i] == nums[i-1]:
            continue
        left = i+1
        right = len(nums)-1
        
        while left<right:
            sum = nums[i]+nums[left]+nums[right]
            if sum>0:
                right-=1
            if sum<0:
                left+=1
            if sum == 0:
                res.append([nums[i],nums[left],nums[right]])
                left+=1
                if nums[left] == nums[left-1] and left<right:
                    left+=1
                
                                  
            
    return res 
    
    
# print(sum3([0,0,0,0]))

#remove elements:
def removeElement(nums,val):
    k = 0
    for num in nums:
        if num != val:
            nums[k] = num
            k+=1
    return k,nums

# print(removeElement([3,2,2,3],3))


#search insert position
def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
        if target>nums[i]:
            index = i+1
    return index
        
        
# print(searchInsert([1,3,5,6],5))
            

#missing number
def missingNumber(nums):
    for i in range(len(nums)):
        if i not in nums:
            return i
    
# print(missingNumber([9,6,4,2,3,5,7,0,1]))


#third max
def thirdMax(l):
    l = list(set(l))
    l.sort(reverse=True)
    
    if len(l)>=3:
        return l[2]
    else:
        return l[0]
    
            
            
# print(thirdMax([1,1,2]))

# Count Largest Group
def countLargestGroup(n):
    def calDigitSum(n):
        dsum = 0
        while n>0:
            u = n%10
            dsum+=u
            n = n//10
        return dsum

    dit = {}
    for i in range(1,n+1):
        digitSum = calDigitSum(i)
        if digitSum in dit:
            dit[digitSum]+=1
        else:
            dit[digitSum] = 1
    maxSize = max(dit.values())    
    
    
    count = 0
    for size in dit.values():
        if size == maxSize:
            count+=1
            
    

    
    return count

# print(countLargestGroup(13))

#duplicate number II

def containNearbyDuplicate(nums,k):
    dict = {}
    for i,num in enumerate(nums):
        if num in dict and i - dict[num] <= k:
            return True
        dict[num] = i
    return False
            
    
# print(containNearbyDuplicate([1,0,1,1],1))

# Next Greater Element I
def nextGreaterElement(num1,num2):
    list = []
    for num in num1:
        nextElemnt = num2.index(num)+1
        found = - 1
        for i in range(nextElemnt,len(num2)):
            if num2[i]>num:
                found = num2[i]
                break
        list.append(found)    
    
    return list

# print(nextGreaterElement([1,3,5,2,4],[6,5,4,3,2,1,7]))

#duplicate zeros
def duplicateZeros(arr):
    i = 0
    while i<len(arr):
        if arr[i] == 0:
            arr.insert(i+1,0)
            arr.pop()
            i+=2
        else:
            i+=1
        
    return arr
# print(duplicateZeros([0,4,1,0,0,8,0,0,3]))

#3392. Count Subarrays of Length Three With a Condition
def countSubarray(nums):
    count = 0
    # while i<len(nums)-2:
    for i in range(len(nums)-2):
        if nums[i]+nums[i+2] == nums[i+1]/2:
            count+=1
    return count
    


# print(countSubarray([2,-7,-6]))

#Intersection of Two Arrays
def intersection(num1,num2):
    n1 = set(num1)
    n2 = set(num2)
    
    common = n1 & n2
    
    return list(common)



def intersect(nums1, nums2):
    result = []
    for i in nums1:
        if i in nums2:
            result.append(i)
            nums2.remove(i)
    return result
            
# print(intersect([1,2,2,1],[2,2]))

def common(num1,num2):
    s1 = set(num1)
    s2 = set(num2)
    
    common= list(s1 & s2)
    if common:
        return min(common)
    else:
        return -1
    
def findDisappearedNumbers(nums):
    result = []
    l = len(nums)
    sett = set(nums)
    for i in range(1,l+1):
        if i not in sett:
            result.append(i)
    return result

# Checking if i in num_set is much faster (average O(1) time) than checking if i in nums (which takes O(n) time).
def findDifference(nums1, nums2):
        
    l1 = set(nums1)
    l2 = set(nums2)
    ans0 = list(l1-l2)
    ans1 = list(l2-l1)

    return [ans0,ans1]
    

print(findDifference([1,2,3],[2,4,6]))

    
                    
            
            
            
            
            
        
        
        



        
    
        
    