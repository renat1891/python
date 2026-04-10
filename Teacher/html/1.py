def descending_order(num):
    return int("".join(sorted(str(num)))[::-1])


print(descending_order(1254))