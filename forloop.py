#print number 1 to 20
print("Numbers from 1 to 20 : ")
for i in range(20):
	print("        ",i+1)

#print only even numbers btw 1 to 50
print("Even numbers btw 1 to 50 : ")
for i in range(50):
	if (i+1)%2==0:
		print("       ",i+1)
		
#multiplication table of number entered by user
num=int(input("Enter a number : "))
print("Multiplication table of the given number is  : ")
for i in range(1,11):
	print(i," x ",num," = ",i*num)