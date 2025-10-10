# #Код:
# dct = { 'x': '1', 'y': '2', 'z': '3', 'v': '5'}
# #Вихідний код:
# ['11', '222', '3333', '555555']


dct = { 'x': '1', 'y': '2', 'z': '3', 'v': '5'}
new_list = []

for v in dct.values():
    new_list.append(v * (int(v) + 1))
print(new_list)
