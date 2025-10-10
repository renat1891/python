# import x

# print(x.my_var)
# print(x.my_func(3, 4))

# from x import my_var, my_func

# print(my_var)
# print(my_func(3, 4))

# from x import *
# print(my_var)
# print(my_func(3, 4))

from x import my_func as mf, my_var as mv

print(mv)
print(mf(3, 4))