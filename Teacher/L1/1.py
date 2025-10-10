price = int(input("Яка ціна вашого товару? "))

if price < 100:
    print("Знижки немає")
elif 100 <= price < 500:
    print("Знижка 10%")
else:
    print("Знижка 20%")