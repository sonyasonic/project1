from datetime import datetime, timedelta
from utils import time_difference, plane


def greet():
    name = input("Введите имя: ")
    print("Бу," + name + "! Испугался? Не бойся, я расскажу тебе, как ты спал :)")


if __name__ == "__main__":  # не особо поняла, зачем она, но в гугле сказали при импорте модулей с ней проще
    greet()
    timediff = time_difference()
    print(f"Длительность вашего сна: {timediff}")

    if timediff < timedelta(hours=6, minutes=30):
        print("Возможно, ты спал слишком мало. Твоя продолжительность сна должна быть больше...")
    elif timedelta(hours=6, minutes=30) <= timediff <= timedelta(hours=8):
        print("Неплохая продолжительность сна, но после загруженного дня этого может быть недостаточно...")
    elif timedelta(hours=8) <= timediff <= timedelta(hours=9, minutes=30):
        print("Это отличная продолжительность сна, так держать!")
    else:
        print("Такое количество сна может быть чрезмерным. Возможно, тебе стоит спать немного меньше...")

    plane(timediff)
