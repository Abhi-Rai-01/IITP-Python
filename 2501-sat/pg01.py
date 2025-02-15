print('pankaj')
print('Hello world!')
print("Happy teacher's day")
print('''pankaj
hello world
happy teacher's day''')

print(6+8-2*2)
print("\n\n\n\n")



# type: str (string), int (integer), float (floating point), bool (boolean)
x = "BO CDA"
y = 105
z = 10.2
print(type(x), type(y), type(z))
print(type(True))
print(type(False))
print("\n\n\n\n")



x, y, z = "Python", "is", "good."
print(x,y,z)
print("\n\n\n\n")



x1 = 25
x2 = 5
y1 = x1 + x2
y2 = x1/x2
y3 = x1 * x2
print(y1)
print(y2)
print("sum of", x1, "and", x2, "is", y1)
print(f"sum of {x1} and {x2} is {y1}")
print("mul of", x1, "and", x2, "is", y3)
print("\n\n\n\n")



a = 10
b = 21
c = a + b
print("The sum after adding", a, "and", b, "is", c)
print("\n\n\n\n")



# list, dictionary, tuple, string
A = [2, 5, 5.5, "Raju", True]
B = [3, 6, 9, 2, 8, 5, 4, 1, 0, 7]

print(A)
print(len(A))
print(A[3])
print(A[-2])

print(len(B))
print(B[1:5])
print(B[:5])
print(B[1:])
print(B[5:1])
print(B[-5:-1])
print(B[-5:-3])
print(B[-5:])
print(B[:-3])
print(B[:])

print(B[1:8:1])
print(B[1:8])
print(B[1:8:2])
print(B[1:8:3])
print("\n\n\n\n")



A = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(f"list of odd numbers is {A[::2]}")
print("\n\n\n\n")



B = [3, 6, 9, 2, 8, 5, 4, 1, 0, 7]

print(B)
print(B[3])

B[3] = 5000

print(B)
print(B[3])
print("\n\n\n\n")



B = [3, 6, 9, 2, 8, 5, 4, 1, 0, 7]
print(B)

B.append("pankaj")
print(B)

B.remove(9)
print(B)