from datetime import timedelta
from utils import time_difference, userflight

#приветствуем пользователя
def greet():
    """Функция greet это функция, которая выдает приветствие.
    Параметры:
    name: str - имя пользователя.
    Механика:
    1) пользователь вводит имя;
    2) на выходе получается строка с введеным от пользователя именем."""

    name = input("Введите имя: ")
    print("Бу," + name + "! Испугался? Не бойся, я расскажу тебе, как ты спал :)")

if __name__ == "__main__":
    greet()
    timediff = time_difference()
    print(f"Длительность твоего сна: {timediff}")

#следующая конструкция позволяет оценить длительность сна: промежуток timediff сравнивается с каким-то временем с помощью timedelta
    if timediff < timedelta(hours=6, minutes=30):
        print("Возможно, ты спал слишком мало. Твоя продолжительность сна должна быть больше...")
    elif timedelta(hours=6, minutes=30) <= timediff <= timedelta(hours=8):
        print("Неплохая продолжительность сна, но после загруженного дня этого может быть недостаточно...")
    elif timedelta(hours=8) <= timediff <= timedelta(hours=9, minutes=30):
        print("Это отличная продолжительность сна, так держать!")
    else:
        print("Такое количество сна может быть чрезмерным. Возможно, тебе стоит спать немного меньше...")

#вызываем главную отличительную функцию проекта из модуля
    userflight(timediff)

print("Еще увидимся!")