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
