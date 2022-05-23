# время из секунд в минуты часы дни
def duration(time):
    if time < 60:
        print(f'{time} сек')
    elif 60 < time < 3600:
        min = time // 60
        second = time % 60
        print(f'{min} мин {second} сек')
    elif 3600 < time < 86400:
        hour = time // 3600
        min = (time % 3600) // 60
        second = (time % 3600) % 60
        print(f'{hour} час {min} мин {second} сек')
    else:
        day = time // 86400
        hour = time % 86400 // 3600
        min = time % 86400 % 3600 // 60
        second = time % 86400 % 3600 % 60
        print(f'{day} дн {hour} час {min} мин {second} сек')
        print('Hello')


duration(400153)
