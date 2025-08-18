#fibonacci series

def fibonacci(n):
	if n<=1:
		return 1
	else:
		return fibonacci(n-1)+fibonacci(n-2)
num=int(input("Enter a Number : "))
print(f'Fibonacci Series of {num} : ')
for i in range(num):
	print(fibonacci(i))
	