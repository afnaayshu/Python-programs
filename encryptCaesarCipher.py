#caesar cipher program
orgText = input("Enter the message : ")
distance =int(input("Enter the distance : "))
textWords =orgText.split()
cipher = ""
for word in textWords:
    code = ""
    for ch in word:
        ordvalue = ord(ch)
        ciphervalue=ordvalue + distance
        if ciphervalue >= ord('a'):
            if ciphervalue>ord('z'):
                ciphervalue = (ord(ch)+distance - 97)%26+97
        else :
            if ciphervalue >= ord('A'):
                if ciphervalue>ord('Z'):
                    ciphervalue = (ord(ch)+distance - 65)%26+65
        code+=chr(ciphervalue)
    cipher = cipher+" "+code
    
print(cipher)
