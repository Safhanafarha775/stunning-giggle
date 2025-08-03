#function to greet the name of user
name=input("Enter your name : ")
def greet(name):
	print(f"Hello, {name}")
greet(name)

#function to add two numbers
def add(a,b):
	print("Sum = ",a+b)
a=int(input("Enter your 1st number : "))
b=int(input("Enter your 2nd number: "))
sum=add(a,b)

#function to check if a number is even or odd use a loop inside a function.
def check(num):
	if num==0:
		print("Number is Zero")
	elif num%2==0:
		print("Number is Even")
	else:
		print("Number is Odd")

num=int(input("Enter a number : "))
check(num)