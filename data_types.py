import numpy as np

# integers
i = 10
print(type(i))

a_i = np.zeros(i,dtype=int)
print(type(a_i))
print(type(a_i[0]))

# floats
x = 19.0
print(type(x))

y = 1.9e2
print(type(y))

z = np.zeros(i,dtype=float)
print(type(z))
print(type(z[0]))

# string
s = "I am a string."
print(type(s))

# bool
yes = True
print(type(yes))

no = False
print(type(no))

# list
alpha_list = ["a", "b", "c"]
print(type(alpha_list))
print(type(alpha_list[0]))
alpha_list.append("d")
print(alpha_list)

# tuple
alpha_tuple = ("a", "b", "c")
print(type(alpha_tuple))

try:
    alpha_tuple[2] = "d"
except TypeError:
    print("We can't add elements to tuples!")
print(alpha_tuple)