speed=int(input("Как быстро едет машина"))
coctoyanie= input("Пьянны ли вы?")

if speed >=100 and coctoyanie == "Да" or speed >= 150 and coctoyanie == "Нет":
    print("Ты был оштрафован:<")

elif speed <=60:
    print("Всё ок, ты доехал до дома!")