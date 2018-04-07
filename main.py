import sys
EOF='EOF'
#Sample String
string = "My Name is BLUE"

#Creating the buffer and placing tokens in it

sizeOfString = len(string)

buff = [0]*(sizeOfString+2)
#print(buff)

#Placing EOF at half ends of the buffer
buff[len(buff)-1]=EOF
buff[len(buff)//2]=EOF

#Populate the buffer with the input stream
listOfChar = list(string)

i=0
for index in range(len(buff)):
    if buff[index] is EOF:
        continue
    buff[index]=listOfChar[i]
    i+=1
    

print(buff)



