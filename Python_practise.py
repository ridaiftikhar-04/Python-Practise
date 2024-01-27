#practise
nums = [1,2,3,4,5]
for num in nums:
    if num == 3:
        print("Number found!")
        continue
    print(num)  

#Nested Loop / Inner loop 
for num in nums:
    for letter in 'abc':
        print(num , letter)

#To iterate to a loop till specific index 
for num in range(7):
    print(num)

#While loop
x = 3
while x<10:
    print(x)
    x = x+1

y=1
print("Infinite Loop")
while True:
    print(y)
    y += 1