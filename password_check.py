#password checker
AZ = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
az="abcdefghijklmnopqrstuvwxyz"
num="0123456789"
spcl ="$@#"
c1=c2=c3=c4=False
password =input("Enter the password : ")
length = len(password)
if(length>=8):
    for ch in password:
        if ch in AZ:
            c1 = True
        if ch in az:
            c2 = True
        if ch in num:
            c3 = True
        if ch in spcl:
            c4 = True
else:
    print("Invalid Password, password is not long enough")

if c1==c2==c3==c4==True :
    print("Valid Password")
else:
    print("Invalid Password, password violates rules")
