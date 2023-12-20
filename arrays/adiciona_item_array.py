import array as arr

a = arr.array('i', [1, 2, 3])
a.append(10)
print (a)

import array as arr
a = arr.array('i', [1, 2, 3])
a.insert(1,20)
print (a)

a = arr.array('i', [1, 2, 3, 4, 5])
b = arr.array('i', [6,7,8,9,10])
a.extend(b)
print (a)