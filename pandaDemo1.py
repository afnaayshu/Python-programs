import pandas as pd
X = [3,4,5,6,7,8]
var1 = pd.Series(X,index = ['a','b','c','d','e','f'],dtype = float,name = "Python")
names = ['Afna','Meril','Gopika','Melissa']
var = pd.Series(names,index =['a','b','c','d'])
dic = {"name":["Python","C","C++","Java"],"Rank":[1,4,3,2]}
var2 = pd.Series(dic)
s = pd.Series(12,index=[1,2,3,4,5,6])
print(s)
print(type(s))
print(var1)
print(var2)
print(var)
#data frame
dic = {"names" : ['Afna','Meril','Gopika','Melissa'],"marks":[23,45,12,10]}
df = pd.DataFrame(dic)
print(df)
print(type(df))
