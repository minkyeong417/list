filename = input('Enter a file name: ')
file = open(filename,'r')
lst = list()
for line in file:
    linelst = line.split()
    for word in linelst:
        if word not in lst:
            lst.append(word)
lst.sort()
print(lst)
