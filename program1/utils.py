from datetime import datetime, timedelta

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
            print("Неправильный ввод")


def plane(timediff): #тут надо будет города дописать если это работает+пжшка поменяй название функции
    if timedelta(hours=0) <= timediff <= timedelta(hours = 1, minutes = 30):
        print("За это время можно доехать до Пулково или долететь до Москвы, Вильнюса, Риги, Минска или Хельсинки")
    elif timedelta(hours=1, minutes=30)< timediff <= timedelta(hours=2):
        print("За это время можно долететь до")
    elif timedelta(hours=2)<timediff<=timedelta(hours=3, minutes=30):
        print("За это время можно долететь до")
    elif timedelta(hours=3, minutes=30)<timediff<=timedelta(hours=5):
        print("За это время можно долететь до")
    elif timedelta(hours=5)<timediff<=timedelta(hours=6, minutes=30):
        print("За это время можно долететь до")
    elif timedelta(hours=6, minutes=30) < timediff <= timedelta(hours=8):
        print("За это время можно долететь до")
    elif timedelta(hours=8) < timediff <= timedelta(hours=9, minutes=30):
        print("За это время можно долететь до")
    elif timedelta(hours=9, minutes=30) < timediff <= timedelta(hours=11):
        print("За это время можно долететь до")
    else:
        print("За такое время можно долететь куда угодно!")

