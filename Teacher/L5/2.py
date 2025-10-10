text = "hello"

i = 1
for char in text:
    print(i, char)
    i+=1

print()

for i, char in enumerate(text, start=1):
    print(i, char)

# 1 h
# 2 e
# 3 l
# 4 l
# 5 o

print(list(enumerate(text)))