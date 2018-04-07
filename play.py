file = open('input.txt','r')
file = file.read()

count=0

for char in file:
    if char is ' ':
        count+=1

#print(count)

st = "My name is blue"

lst = list(st)

for i in range(10):
    print(i)