a = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9 ,10]

findNum = int(input("What Number you you want to find?\n "))

if findNum in a:
    print("Your number exists\n")
else:
    print("doesnt exist\n")


largest = max(a)
print(largest , "is the largest number\n")

sum = 0
for i in a:
    sum = sum + i


print(sum , "is the sum of the list\n")




 
