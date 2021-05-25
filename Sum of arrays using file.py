
#Sum of Array using Files

lst = []
f = open('file.txt')
text = f.read()
lst = list(map(int,text.split(' ')))
print("Sum:",sum(lst))




