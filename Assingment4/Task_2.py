file = open("output.txt", "w")
a=file.write(input("Enter any text: ") + "\n")
print("Data written in output.txt")
file.close()


file = open("output.txt", "a")
b=file.write(input("Enter additional text: "))
print("Data successfully appended")
file.close()


file = open("output.txt", "r")
c=file.readlines()
print("Your written content is: ")
print(c[0])
print(c[1])
file.close()
