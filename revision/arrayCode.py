#BASIC OPERATION
#insertion 
def insertion(arr,index,element):
    arr.insert(index,element)
    return arr

# print(insertion([1,2,3,4,5],2,23))

# deletion
def deletion(arr,index):
    arr.pop(index)
    return arr

# print(deletion([1,2,3,4,5],2))

#searching

def searching(arr,item):
    for i in range(len(arr)):
        if arr[i] == item:
            return i
    else:
        return "not found"
            
# print(searching([1,33,44,2,5],5))

#sorting
def sorting(arr):
    sortArr= sorted(arr,reverse=True)
    return sortArr

# print(sorting([4,223,5,1,2]))

#traversal
def traversing(arr):
    for i in arr:
        print(i)
    
# traversing([23,231,442,3221])


#twoSum using two pointer

def twoPointer(arr,target):
    low = 0
    high = len(arr) - 1
    
    while low<high:
        sum = arr[low] + arr[high]
        
        if sum == target:
            print(low,high)
    
        if sum>target:
            high -= 1
        else:
            low += 1
            
# print(twoPointer([1,2,3,4,5,6],9))


#remove element 

def removeElement(arr,target):
    i = 0
    for j in range(len(arr)):
        if arr[j] != target:
            arr[i] = arr[j]
            i += 1
    return i

arr = [1,2,3,4,5,6,7,8]
len1 = removeElement(arr,6)
print(arr[:len1])


#binarySearch
def binarySearch(arr,target):
    low = 0
    high = len(arr) - 1
    while low<=high:
        mid = low+high//2
        
        if arr[mid] == target:
            return mid
        if arr[mid] > target:
            high -= 1
        else:
            low  += 1
print(binarySearch([1,2,3,4,5,6,7],5))