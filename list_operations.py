#given list of marks, print all marks above 80
sub = int(input("Enter the number of subjects : "))
print("Enter the marks of each subject : ")
marks=[]
for i in range(sub):
	mark=int(input())
	marks.append(mark)
print("Marks above 80 are : ")
for mark in marks:
	if mark>=80:
		print(mark)

#count vowels in a word
vowels=['a','e','i','o','u']
text=input("Enter a word :")
count=0
for l in text.lower():
	if l in vowels:
		print(l)
		count+=1		
print(f" Number of vowels is {count}")

