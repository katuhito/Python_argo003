# for i in range(1, 51):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             print("FizzBuzz", end=' ')
#         else:
#             print("Fizz", end=' ')
#     elif i % 5 == 0:
#         print("Buzz", end=' ')
#     else:
#         print(i, end=' ')


"""最初のFizzBuzzが出力される条件を最初にチェックするように修正"""

outputs = []
for i in range(1, 51):
    if i % 15 == 0:      #3と5の最小公倍数
        print("FizzBuzz", end=' ')
        outputs.append("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz", end=' ')
        outputs.append("Fizz")
    elif i % 5 == 0:
        print("Buzz", end=' ')
        outputs.append("Buzz")
    else:
        print(i, end=' ')
        outputs.append(str(i))

print(" ".join(outputs))
