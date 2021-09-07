fname = input("Enter file name:")
fhand = open(fname)
count = 0
for line in fhand:
    if line.startswith("From"):
        line = line.rstrip().split()
    if len(line) < 3 or line[0] != 'From':
        continue
    print(line[1])
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
