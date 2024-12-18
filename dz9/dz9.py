import random

prizes = {
    777: 200,
    999: 100,
    555: 50,
    333: 15,
    111: 10,
    '*77': 5,
    '**7': 3,
    '*00': 2,
    '**0': 1
}

def calculate_prize(number):
    """
    Определяет выигрыш для данного числа.
    :param number: Выпавшее число (int)
    :return: Размер выигрыша (int)
    """
    str_number = str(number).zfill(3)
    if number in prizes:
        return prizes[number]
    elif str_number[1:] == '77':
        return prizes['*77']
    elif str_number[2] == '7':
        return prizes['**7']
    elif str_number[1:] == '00':
        return prizes['*00']
    elif str_number[2] == '0':
        return prizes['**0']
    return 0

def simulate_game(rounds=1_000_000):
    """
    Симуляция игры на лотерейном автомате.
    :param rounds: Количество игр
    :return: Средняя прибыль/убыток за одну игру
    """
    total_spent = 0
    total_won = 0

    for _ in range(rounds):
        total_spent += 1
        random_number = random.randint(0, 999)
        total_won += calculate_prize(random_number)

    average_profit = (total_won - total_spent) / rounds
    return average_profit
average_result = simulate_game(1_000_000)
print(f"Средний результат за одну игру: {average_result:.2f} руб.")
