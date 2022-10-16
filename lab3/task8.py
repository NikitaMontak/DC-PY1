money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05
month = 0
while money_capital >= spend-salary:
    money_capital = money_capital+salary-spend
    spend=spend*1.05
    month+=1
# TODO Оформить решение

print(month)