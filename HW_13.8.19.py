tickets = int(input("Сколько билетов вы хотите заказать: "))
all_age = []
price = 0.0

for i in range(tickets):
    age = int(input(f"Введите возраст участика №{i + 1}: "))
    all_age.append(age)

    if age < 18:
        price = price + 0
        print("Бесплатный билет")
    elif age >= 18 and age <= 25:
        price = price + 990
        print("Стоимость билета - 990 р.")
    else:
        price = price + 1390
        print("Стоимость билета - 1390 р.")

all_price = round(price)

discount = int(all_price * 0.9)
if tickets > 3:
    print("При регистрации больше трёх человек,\nВы получаете дополнительную скидку 10%!")
    print("Стоимость билетов с учётом всех скидок: ", discount, "рублей.")
else:
    print("Общая стоимость билетов: ", all_price, "рублей.")
