#traversing

# arr = [1,2,3,4,5]
# item = 22
# found = False
# for i in range(0,len(arr)):
#     # print(arr[i])
#     if item == arr[i]:
#         found = True
#         print("True")
#         break
    
# if(not found):
#     print("false")
   
    
    
def insertElement(arr,index,element):
    arr.insert(index,element)
    return arr

def deleteELement(arr,index):
    arr.pop(2)
    return arr
    
arr = [1,2,3,4,5]
print(insertElement(arr,2,10))
print(deleteELement(arr,2))
 

    
    

    