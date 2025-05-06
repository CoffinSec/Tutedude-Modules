try:
    file = open("sample.txt","r+")
    lines=file.readlines()
    for i in range(len(lines)):
        r_line=lines[i]
        print("Line",i+1,":",r_line)
        file.close()

except FileNotFoundError:
    print("The file 'sample.txt' is not Present")

try:
    file = open("sample1.txt", "r+")
    lines = file.readlines()
    for i in range(len(lines)):
        r_line = lines[i]
        print("Line", i + 1, ":", r_line)
        file.close()

except FileNotFoundError:
    print("The file 'sample1.txt' is not Present")
