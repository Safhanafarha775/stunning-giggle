#check if a no is even or odd
num=int(input("Enter a number: "))
if num%2==0:
	print(num," is even number")
else:
	print(num," is odd number")
	
#check if a person is eligible for vote or not
age=int(input("Enter your age: "))
if age>=18:
	print("This person is eligible to vote")
else:
	print("This person is not eligible to vote")
	
#Grade calculator using if else ladder
mark=int(input("Enter your mark: "))
if mark>=90:
	print("Grade = A")
elif mark>=80:
	print("Grade = B")
elif mark>=70:
	print("Grade = C")
elif mark>=60:
	print("Grade = D")
elif mark>=50:
	print("Grade = E")
else:
	print("Failed")	
	
#greatest of 3 numbers
a=int(input("Enter 1st number : "))
b=int(input("Enter 2nd number : "))
c=int(input("Enter 3rd number : "))
if a>b:
	if a>c:
		print(f"{a} is the greatest number")
	else:
		print(f"{c} is the greatest number")
else:
	if b>c:
		print(f"{b} is the greatest number")
	else:
		print(f"{c} is the greatest number")
#check whether a number is divisible by 2 & 3
num=int(input("Enter a number : "))
if num%2==0 & num%3==0:
	print(f"{num} is divisible by 2 and 3")
else:
	print(f"{num} is not divisible by 2 and 3")