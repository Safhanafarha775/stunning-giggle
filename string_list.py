
#print characters of a word entered by user
text=input("Enter a word: ")
for i in text:
	print(i)
	
#Sum of number in a list
num=[]
length=int(input("Enter the number of numbers that you want to enter : "))
print("Enter your nunbers : ")
for i in range(length):
	num1=int(input())
	num.append(num1)
print("Sum =",sum(num))