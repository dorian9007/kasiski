
print("")
code = input("  [+] Der Code:  ")
print("")
iterations = int(input("  [+] N-Verschiebungen:  "))
print("")

verschiebendercode =  code
length = len(verschiebendercode)
counter = 0

for i in range(0, iterations):
	verschiebendercode = verschiebendercode+verschiebendercode[0]
	verschiebendercode = verschiebendercode[1:]
	print("")
	print(code)
	print("")
	print(verschiebendercode)
	print("----------")
	for i in range (0, length):
		if verschiebendercode[i] == code[i]:
			counter = counter+1
	print(counter)
	counter = 0