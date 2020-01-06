filename = input('Enter a file name: ')
file = open(filename,'r')
count = 0
for line in file:
    if line.startswith('From '):
        linelst = line.split()
        print(linelst[1])
        count = count + 1
print("There were", count, "lines in the file with From as the first word")
