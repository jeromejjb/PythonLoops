#Demonstrating while loops with Python 
count = 0 
while (count < 3):
    count = count + 1 
    print("Hello Jerry")
else:
    print("In Else Block")
    

# count = 4
# while (count == 4): print("Hello Jerry")

#Python For Loop to illustrate Iterating over range 0 to n-1 
n = 5
for i in range(0,n):
    print(i)
    
#Python interating by index 
list = ["Jerry", "bear", "is cool" ]
for index in range(len(list)):
    print (list[index])