#program to find whether the even number is even or odd
num=int(input("Enter a number: "))

if num%2==0:
    print(num,"is even number")
else:
    print(num,"is odd number")


total=0
for i in range(1,51):
    total+=i

print("The sum of numbers from 1 to 50 is:",total)

