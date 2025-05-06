hp = (40)
damage = (52)

def start_game(hp, damage):
    print(f"Welcome to game. Your Hp: ({hp})? and your damage is {damage}")

def culm(hp, damage):
    lev1 = int(input("Вы встретили Гадалку, ваши дейстивя? 1 - пошлю её за хлебом, 2 - запишусь на сеанс, 3 - пройду мимо. : "))
    if lev1 == 1:
        print("Вас отравили")

    elif lev1 == 2:
        print("Вы проиграли")
    
    else:
        print("ds ghjikb ehjdtym!")

start_game(hp, damage)
culm(hp, damage)