s = 0
a = int(input("Сколько стоит 1 кг конфет: "))
s += a * 2
b = int(input("Цена буханки хлеба: "))
s += b
c = int(input("Цена за литр молока: "))
s += c * 0.75
print(f"Стоимость покупок: {s}")
