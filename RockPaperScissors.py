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
        print("Неправильный ввод данных")
print()
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
    win_l1=[]
    win1=0
    win_l2=[]
    win2=0
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
        print()
        shuffle(a)
        print(f"Компутер выбрал {a[0]}")
        print()
        if a[0]==1 and valik==1 or a[0]==2 and valik==2 or a[0]==3 and valik==3:
            print("Ничья")
        elif a[0]==1 and valik==2 or a[0]==2 and valik==3 or a[0]==3 and valik==1:
            print("Компутер выиграл")
            win_l1.append(int(1))
        elif a[0]==2 and valik==1 or a[0]==3 and valik==2 or a[0]==1 and valik==3:
            print("Пользователь выиграл")
            win_l2.append(int(1))
        win1=sum(win_l1)
        win2=sum(win_l2)
        print(f"Очки компутера «{win1}»")
        print(f"Очки пользователя «{win2}»")
        print()
        print("Желаете ли вы очистить счет? (1 - Да/0 - Нет)")
        while 1:
            try:
                point=int(input(" => "))
                if point==1 or point==0:
                    break
            except ValueError:
                print("Непрвильный ввод данных")
        if point==1:
            win_l1.clear()
            win_l2.clear()
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
    print("Пожалуйста, пишите латиницой, иначе программа погибнет!")
    name1=str(input("Пользователь1, как вас зовут? => "))
    name2=str(input("Пользователь2, как вас зовут? => "))
    winl1=[]
    win1=0
    winl2=[]
    win2=0
    while 1:
        print(f"{name1} выбери: камень - q/ ножницы - w/ бумага - e ")
        if read_key()=="q":
            valik=1
        elif read_key()=="w":
            valik=2
        elif read_key()=="e":
            valik=3
        print(f"{name2} выбери: камень - z/ ножницы - x/ бумага - c ")
        if read_key()=="z":
            valik2=1
        elif read_key()=="x":
            valik2=2
        elif read_key()=="c":
            valik2=3
        print(f"{name1} выбрал {valik}")
        print(f"{name2} выбрал {valik2}")
        if valik==1 and valik2==1 or valik==2 and valik2==2 or valik==3 and valik2==3:
            print("У вас получилась ничья")
        elif valik==1 and valik2==2 or valik==2 and valik2==3 or valik==3 and valik2==1:
            print(f"{name1} выиграл")
            winl1.append(int(1))
        elif valik==2 and valik2==1 or valik==3 and valik2==2 or valik==1 and valik2==3:
            print(f"{name2} выиграл")
            winl2.append(int(1))
        win1=sum(winl1)
        win2=sum(winl2)
        print(f"{name1} всего набрал «{win1}»")
        print(f"{name2} всего набрал «{win2}»")
        print()
        print("Желаете ли вы очистить счет? (backspace - Да/space - Нет)")
        print("При создании игры первый игрок всегда проигрывал, поэтому у него не очищается счёт при выигрышах")
        if read_key() == "backspace":
            winl1.clear()
            winl2.clear()
        if read_key() == "space":
            print("Так держать!")
        print()
        print("Желаете сыграть ещё одну игру? (r - Да/t - Нет)")
        if read_key() == "r":                   
            continue
        elif read_key() == "t": 
            print("Спасибо за игру!")
            quit()