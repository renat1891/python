# with open('text.txt', 'a') as file:
#    file.write('Hello, world!\n')

# with open('text.txt', 'r') as file:
#    text = file.read()


with open('text.txt', 'r') as file:
#    print(file.read(5))
    print(file.readline())
    print(file.readlines())