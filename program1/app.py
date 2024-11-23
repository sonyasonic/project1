from datetime import datetime, timedelta
from mymodule_for_project import plane


def greet():
    name = input("Введите имя: ")
    print("Бу," + name + "! Испугался? Не бойся, я расскажу тебе, как ты спал :)")

def time_difference():
    time_format = "%H:%M"

    while True:
        sleep_str = input("Введи время засыпания (часы:минуты): ")
        wakeup_str = input("Введи время пробуждения (часы:минуты): ")

        try:
            time1 = datetime.strptime(sleep_str, time_format)
            time2 = datetime.strptime(wakeup_str, time_format)


            if time2 < time1:
                time2 += timedelta(days=1)
            else:
                timediff = time2 - time1
            return timediff

        except ValueError:
            print("Ошибка :(", "Введи правильный формат времени (часы:минуты)!", sep = "\n")


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
