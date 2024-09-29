number = str(input("Введите номер билета: "))
first3 = int(number[0]) + int(number[1]) + int(number[2])
second3 = int(number[3]) + int(number[4]) + int(number[5])
if first3 == second3:
    print("Счастливый")
else:
    print("Обычный")