from datetime import datetime, timedelta

def time_difference():
    """Функция time_difference используется для вычисления временного промежутка для его дальнейшего использования.
    Параметры:
    sleep_str: str - время засыпания;
    wakeup_str: str - время пробуждения;
    time1: str - время заспыаания в формате времени;
    time2: str - время пробуждения в формате времени;
    timediff: str - разница между time1 и time2, временной промежуток.
    Механика:
    1)пользовательский ввод;
    2)цикл while для возможности бесконечного ввода, пока не он не будет правильным;
    3)преобразование значений, введенных пользователем в формат времени с помощью datetime и timeformat;
    4)вычисление временного промежутка с помощью timedelta, с учетом перехода через полночь."""

    time_format = "%H:%M"

    while True:
        sleep_str = input("Введи время засыпания (часы:минуты): ")
        wakeup_str = input("Введи время пробуждения (часы:минуты): ")

        try:
            time1 = datetime.strptime(sleep_str, time_format)
            time2 = datetime.strptime(wakeup_str, time_format)


            if time2 < time1:
                time2 += timedelta(days=1)
            timediff = time2 - time1
            return timediff

        except ValueError:
            print("Неправильный ввод :( Попробуй ввести в формате 13:30 (часы:минуты)!")


def userflight(timediff):
    """Функция plane принимает значение timediff(поэтому эта функция вынесена именно в модуль) и,в зависимости от значений,
    выдает город, куда можно было слетать за это время. Механика:
    с помощью if-elif-else сравнивается timediff с помощью timedelta, далее в заивисимости от результата сравнения через print выводится
    соответствующая строка с городами"""

    if timedelta(hours=0) <= timediff <= timedelta(hours = 1, minutes = 30):
        print("За это время можно доехать до Пулково или долететь до Москвы, Вильнюса, Риги, Минска или Хельсинки")
    elif timedelta(hours=1, minutes=30)< timediff <= timedelta(hours=2):
        print("За это время можно долететь до Волгограда или Калининграда")
    elif timedelta(hours=2)<timediff<=timedelta(hours=3, minutes=30):
        print("За это время можно долететь до Варшавы, Казани, Мурманска, Екатеринбурга, Уфы, Самары,"
              "Ростова-На-Дону, Перми, Ижевска, Лондона или Парижа")
    elif timedelta(hours=3, minutes=30)<timediff<=timedelta(hours=5):
        print("За это время можно долететь до Астаны, Рима, Женевы, Омска, Астраани, Новосибирска или Барселоны")
    elif timedelta(hours=5)<timediff<=timedelta(hours=6, minutes=30):
        print("За это время можно долететь до Иркутска, Мадрида, Тбилиси или до Дубая")
    elif timedelta(hours=6, minutes=30) < timediff <= timedelta(hours=8):
        print("За это время можно долететь до Якутска, Хабаровска, Пекина, Читы, Томска или Благовещенска")
    elif timedelta(hours=8) < timediff <= timedelta(hours=9, minutes=30):
        print("За это время можно долететь до Петропавловска-Камчатского, Владивостока или Сеула")
    elif timedelta(hours=9, minutes=30) < timediff <= timedelta(hours=11):
        print("За это время можно долететь до Токио, городов Тайланда или до Шанхая")
    elif timediff == timedelta(hours=13, minutes=50): #маленький прикольчик :)
        print("Можно попасть в Сан-Франциско, город в стиле диско!!")
    else:
        print("За такое время можно долететь куда угодно!")

#тут была функция main, но мы поняли, что она не нужна, так что от нее избавились