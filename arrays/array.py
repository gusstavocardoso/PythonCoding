import array as arr

# array do tipo inteiro
a = arr.array('i', [1, 2, 3])
print (type(a), a)

# array do tipo char
a = arr.array('u', 'BAT')
print (type(a), a)

# array do tipo float
a = arr.array('d', [1.1, 2.2, 3.3])
print (type(a), a)