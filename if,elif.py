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

#check whether a number is divisible by 2 & 3