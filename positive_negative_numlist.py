#python program to read n integers into a list and seprate positive and negative numbers into 2 different lists
n = int(input("Enter the number of integers : "))
numlist =[]
poslist =[]
neglist =[]
for i in range(n):
    num = int(input("Enter integer {} : ".format(i+1)))
    numlist.append(num)
    if num>0:
        poslist.append(num)
    elif num<0:
        neglist.append(num)
    else: #if num =0
        poslist.append(num)
print("List of integers : ");
numlist.sort()
print(numlist)
print("Positive integers (includes 0) : ")
poslist.sort()
print(poslist)
print("Negative integers : ")
neglist.sort()
print(neglist)