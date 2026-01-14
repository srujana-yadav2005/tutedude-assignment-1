#area of triangle
#semi peri(s)=(a+b+c)/2
#area=root(s*(s-a)*(s-b)*(s-c))


a=float(input("enter a:"))
b=float(input("enter b:"))
c=float(input("enter c:"))
s=(a+b+c)/2
area=(s*(s-a)*(s-b)*(s-c))**0.5
print("area:",round(area,2))