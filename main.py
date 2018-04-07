import sys
import pprint as pp
EOF='EOF'
#Sample String
#string = "My Name is BLUE and Green and yellow also it is a little bit of redish"

#Reading From the File
inputFile = sys.argv[1]
file = open(inputFile,'r')
string = file.read()

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
    
#Dividing the Buffer into two part
first=buff[0:len(buff)//2+1]
#print(first)
second=buff[len(buff)/2+1:len(buff)]
#print(second)

#Tokenizing individual items from the buffers

listOfTokens=[]
value=''

for index in range(len(first)-1):
    if(first[index] is not ' '):
        value+=first[index]
    else:
        listOfTokens.append(value)
        value=''

for index in range(len(second)-1):
    if(second[index] is not ' '):
        value+=second[index]
    else:
        listOfTokens.append(value)
        value=''

lastToken = string.split()
lastToken = lastToken[len(lastToken)-1]
listOfTokens.append(lastToken)
#print(listOfTokens)
#print(second)
pp.pprint(listOfTokens,width=3)


