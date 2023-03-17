#read list of numbers find median
numlist=[]
n = int(input("enter limit : "))
print("Enter the numbers : ")
for i in range(n):
    ele = int(input())
    numlist.append(ele)
numlist.sort()
print(numlist)
if(n%2==0):
    median = (numlist[(n%2)+2]+numlist[(n%2)+1])/2
else:
    median = numlist[(n%2)+1]/2
print("Median is {}".format(median))