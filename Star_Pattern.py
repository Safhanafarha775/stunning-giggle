#Nested Loop: print star pattern

#Right-Angled Triangle
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end=" ")
    print()
    
#Inverted Right Angled Triangle
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
	for j in range(i):
		print("*", end=" ")
	print()
	
#pyramid
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end=" ")
    # Print stars
    for k in range(i):
        print("*", end=" ")
    print()


#Diamond Pattern
rows = int(input("Enter number of rows: "))

# Upper part
for i in range(1, rows + 1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()

# Lower part
for i in range(rows - 1, 0, -1):
    for j in range(rows - i):
        print(" ", end=" ")
    for k in range(i):
        print("*", end=" ")
    print()