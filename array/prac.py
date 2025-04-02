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
print(removeDuplicate2([1,2,2,3,3,4,4,4,5]))