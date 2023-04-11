
#sort n numbers in python
n=int(input("Enter the limit : "))
numlist=[]
print("Enter the numbers : ")
for i in range(n):
   numlist.append(int(input()))
print("List before sorting : {}".format(numlist))
for i in range(n):
    for j in range(n-i-1):
        if numlist[j]>numlist[j+1]:
            temp=numlist[j]
            numlist[j]=numlist[j+1]
            numlist[j+1]=temp
           
print("List after sorting : {}".format(numlist))
#
