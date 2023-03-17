#find mode of list of numbers
n=int(input("Enter the limit : "))
numlist=[]
print("Enter the numbers : ")
for i in range(n):
   numlist.append(int(input()))
mode = numlist[0]
for i in range(n-1):
    if numlist.count(mode)<numlist.count(numlist[i+1]):
        mode = numlist[i+1]
print("Mode is : ",mode)
