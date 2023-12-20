import array as arr

a = arr.array('i', [1, 2, 3])
#indexação
print (a[1])
#slicing
print (a[1:])

a = arr.array('i', [1, 2, 3])
a[1] = 20
print (a[1])