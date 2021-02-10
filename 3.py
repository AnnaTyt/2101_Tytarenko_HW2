# Task 3 =================================================================================

# ТЗ: Создать программу, которая будет подсчитывать, достаточен ли доход пользователя,
# что бы прожить определенный срок в определенной стране.

# Developer notes: Тут специально дано неполное и невнятное ТЗ.
# Ваша задача, перед тем как приступить к решению, задать все необходимые вопросы
# "заказчику". А после, основываясь на ответах, приступить к решению.
# ========================================================================================

En_rent = 1000
En_food = 2000
En_taxes = 4000  # 7000
En_total = En_rent + En_food + En_taxes

Fr_rent = 1000
Fr_food = 2000
Fr_taxes = 3000  # 6000
Fr_total = Fr_rent + Fr_food + Fr_taxes

Sv_rent = 6000
Sv_food = 1000
Sv_taxes = 1000 #8000
Sv_total = Sv_rent + Sv_food + Sv_taxes

while True:
    my_income = int(input("Please enter your income >>  "))
    if my_income >= En_total and my_income >= Fr_total and my_income >= Sv_total:
        print("You have enough to live in any country from:")
        print("Required monthly income in England = ", + En_total)
        print("Required monthly income in France = ", + Fr_total)
        print("Required monthly income in Sweden = ", + Sv_total)
        break
    else:
        if my_income >= Fr_total:
            print("You have enough to live in France")
            print("Required monthly income in France = ", + Fr_total)

        if my_income >= En_total:
            print("You have enough to live in England")
            print("Required monthly income in England = ", + En_total)

        if my_income >= Sv_total:
            print("You have enough to live in Sweden")
            print("Required monthly income in Sweden = ", + Sv_total)

        if my_income < En_total and Sv_total and my_income < Fr_total:
            print("You need to increase your monthly earnings.")
            break
    break
