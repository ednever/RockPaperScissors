from random import*
from keyboard import*
print("Привет, хочешь сыграть в камень ножницы бумага? (1 - Да/0 - Нет) ")
while 1:
    try:
        otvet=int(input(" => "))
        if otvet==1:
            break
        elif otvet==0:
            print("Жаль :( ")
            quit()
    except ValueError:
        print("Непрвильный ввод данных")
print("Хочешь сыграть с ботом или другом? (1 - С ботом/0 - С другом) ")
while 1:
    try:
        game=int(input(" => "))
        if game==1 or game==0:
            break
    except ValueError:
        print("Непрвильный ввод данных")
a=[1,2,3]

if game==1:
    bot=0
    chel=0
    while 1:
        print("Выбери: камень - 1/ ножницы - 2/ бумага - 3 ")
        while 1:
            try:
                valik=int(input(" => "))
                if valik==1 or valik==2 or valik==3:
                    break
            except ValueError:
                print("Непрвильный ввод данных")
        print(f"Ты выбрал {valik}")
        shuffle(a)
        print(f"Компутер выбрал {a[0]}")
        if a[0]==1 and valik==1 or a[0]==2 and valik==2 or a[0]==3 and valik==3:
            print("Ничья")
        elif a[0]==1 and valik==2 or a[0]==2 and valik==3 or a[0]==3 and valik==1:
            print("Компутер выиграл")
            bot+=1
        elif a[0]==2 and valik==1 or a[0]==3 and valik==2 or a[0]==1 and valik==3:
            print("Пользователь выиграл")
            chel+=1
        print("Желаешь ещё одну игру (1 - Да/0 - Нет)")
        while 1:
            try:
                zxc=int(input(" => "))
                if zxc==1 or zxc==0:
                    break
            except ValueError:
                print("Непрвильный ввод данных")
        if zxc==1:
            continue
        else: 
            print("Спасибо за игру!")
            print()
            quit()

elif game==0:
    while 1:
        print("Пользователь1 выбери: камень - q/ ножницы - w/ бумага - e ")
        if read_key()=="q":
            valik=1
        elif read_key()=="w":
            valik=2
        elif read_key()=="e":
            valik=3
        print("Пользователь2 выбери: камень - z/ ножницы - x/ бумага - c ")
        if read_key()=="z":
            valik2=1
        elif read_key()=="x":
            valik2=2
        elif read_key()=="c":
            valik2=3
        print(f"Пользователь1 выбрал {valik}")
        print(f"Пользователь2 выбрал {valik2}")
        if valik==1 and valik2==1 or valik==2 and valik2==2 or valik==3 and valik2==3:
            print("Ничья")
        elif valik==1 and valik2==2 or valik==2 and valik2==3 or valik==3 and valik2==1:
            print("Пользователь1 выиграл")
        elif valik==2 and valik2==1 or valik==3 and valik2==2 or valik==1 and valik2==3:
            print("Пользователь2 выиграл")
        print("Желаете ещё одну игру? (1 - Да/0 - Нет)")
        while 1:
            try:
                zxc=int(input(" => "))
                if zxc==1 or zxc==0:
                    break
            except ValueError:
                print("Непрвильный ввод данных")
        if zxc==1:
            continue
        else: 
            print("Спасибо за игру!")
            quit()