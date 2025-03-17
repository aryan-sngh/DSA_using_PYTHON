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
        
twoSum([1,2,3,4,5,9],7)


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

print(twoSum2([1,2,3,4,5,9],10))
        
        