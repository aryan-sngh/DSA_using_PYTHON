def printRecrusive(num):
    if num <= 10:
        print(num)
        printRecrusive(num+1)

printRecrusive(1)