height = int(input("Введите рост пирамиды"))
for i in range(0, height):
	for j in range(height-i, 0, -1):
		print(" ", end="")
	for j in range(i, 0, -1):
		print(j, end="")
	for j in range (2, i+1):
		print(j, end="")
	print("")