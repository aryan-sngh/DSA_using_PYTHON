#example 1
#O(n)
# def beginnerExample(arr):
#   for i in range(0,len(arr)):
#     print(arr[i])
# beginnerExample([1,2,3,4,5,6,7,8,9,10])
#simple example of O(n) time complexity depends on the size of the input

#example 2
#O(1)
# def constantTimeExample(arr):
#   print(arr[0])
# constantTimeExample([1,2,3,4,5,6,7,8,9,10])
#simple example of O(1) time complexity no matter the size of the input

#example 3
#O(1)
# def constantTimeExample(arr):
#   print(arr[0])
#   print(arr[1])
# constantTimeExample([1,2,3,4,5,6,7,8,9,10])    
#simple example of O(1) time complexity no matter the size of the input

#example 4
#O(n^2)
# def intermediateExample1(arr):
#     for i in range(0,len(arr)):
#         for j in range(0,len(arr)):
#             print(arr[i],arr[j])
# intermediateExample1(arr=[1,2,3,4,5])
#simple example of O(n^2) time complexity depends on the size of the input as its increase no of operation twice

#example 5
#O(1)
# def intermediateExample2(arr):
#     mid=len(arr)//2
#     print(arr[mid])
# intermediateExample2([1,2,3,4,5])

#example 6
#O(n)
# def intermediateExample3(arr):
#     sum=0
#     for i in range(0,len(arr)):
#         sum+=arr[i]
#     print(sum)    
# intermediateExample3([1,2,3,4,5])
#simple example of O(n) time complexity depends on the size of the input 

#example 7
#O(1)
# def example7(n):
#     for i in range(1,min(n,10)):
#         print(i)
# example7(20)

#example 8
#O(n)
# def example8(n):
#     for i in range(1,max(n,10)):
#         print(i)
# example8(20)
# #as depend on input 

#example 9
# O(logn)
# def example9(n):
#     i=1
#     while(i<n):
#         print(i)
#         i*=2
# example9(36)

#example 10 //remove non dominent
#0(n^2)
# def example10(n):
#     for i in range(0,n):
#         for j in range(0,n):
#             print(i,j)
#     for k in range(0,n):
#         print(k)
# example10(10)