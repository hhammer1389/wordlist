import numpy as np
def num_letters(n_rows, n_columns):
    return n_rows * n_columns - (n_rows-2) * (n_columns-2)
assert num_letters(4,4)== 12
assert num_letters(4,13)== 30
assert num_letters(6,4)==16
assert num_letters(6,7)==22
print("Checking assertions")
#starting part 3
data = np.loadtxt("loop4.csv", delimiter=",", dtype=str, encoding = 'utf8')
words = [] #this will store the letters we extract from the data file
rows, columns = data.shape  #this gives you the number of rows and number of columns in the data file
i = 0
for i in range(columns-1):
    words.append(str(data[0,i]))
    i += 1
    if i > columns:
        break
y = 0
for y in range(rows-1):
    words.append(str(data[y,-1]))
    y += 1
    if y > rows-1:
        break
h = 0
for h in range(columns-1):
    words.append(str(data[-1,h]))
    h+=1
    if y > columns-1:
        break
k=0
for k in range(rows-1):
    words.append(str(data[k,0]))
    k+=1
    if k >rows:
        break
...
print(words) #check that you collected all the letters in your data file
word_list = []
assert len(words) == num_letters(rows, columns)
i = 0
for i in range(columns-1):
    word_list.append(str(data[0,i])+(str(data[0,i+1])))
    i += 1
    if i > columns:
        break
y = 0
for y in range(rows-1):
    word_list.append(str(data[y,-1])+ (str(data[y+1,-1])))
    y += 1
    if y > rows-1:
        break
h = 0
for h in range(columns-1):
    word_list.append(str(data[-1,h])+(str(data[-1,h-1])))
    h+=1
    if y > columns-1:
        break
k=0
for k in range(rows-1):
    word_list.append(str(data[k,0])+ (str(data[k-1,0])))
    k+=1
    if k >rows:
        break
print(word_list)
