from time import sleep
import os
import sys
try:
    from pygame import mixer
except:
    print("Модуль pygame не установлен, музыки и звуков не будет. Чтобы установить модуль, открой консоль \nи пиши \'python -m pip install pygame\' на винде, или 'pip3 install pygame' на линуксе или маке")
    sleep(5)
GotEnd1 = False
GotEnd2 = False
GotEnd3 = False
GotEnd4 = False
GotEnd5 = False
GotEnd6 = False
ReleasedSaltman = False
ReleasedSoupman = False
GotFork = False
GotBread = False
GotGarlic = False
GotSaltSphere = False
GotSoupSphere = False
cwd = os.getcwd()
datadir = os.path.join(cwd, "data")
varspy = os.path.join(datadir, "vars.py")
try:
    os.mkdir(datadir)
except:
    pass
if os.path.exists(varspy):
    sys.path.append(datadir)
    from vars import *
else:
    f = open(varspy, 'w')
    f.write("""
GotEnd1 = False
GotEnd2 = False
GotEnd3 = False
GotEnd4 = False
GotEnd5 = False
GotEnd6 = False
ReleasedSaltman = False
ReleasedSoupman = False
GotFork = False
GotBread = False
GotGarlic = False
GotSaltSphere = False
GotSoupSphere = False
""")
    f.close()
    sys.path.append(datadir)
    from vars import *

#art
soup = """
 \##############/
  \____________/"""
salt= """
_________________
|                |
|                |
|       S        |
|       A        |
|       L        |
|       T        |
|                |
|                |
‾‾‾(           )‾‾
    (         )
     ‾‾‾‾‾‾‾‾‾
      .   .. .
       .  .  ..
      . . .   . .
"""
spoon = """
   (‾‾‾‾)
  (      )
 (        )
(          )
 (        )
  (      )
   (    )
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
    |  |
     ‾‾
"""
soupnsalt = """
_________________________________________________________
|                                                        |
|     _____                   ____                       |
|    ( . . )                 ( ' ' )                     |
|     ( / )                   ( ~ )     |                |
|___   ‾|‾‾  __          __    ‾|‾‾ ____|                |
|   \‾‾‾‾‾‾‾/  |        |  |‾‾‾‾‾‾‾‾|                    |
|    |  S   |  |       |   | S      |                    |
|    |      |  |      |    | /‾\/‾\ |                    |
|    \_____/               |/      \|			 |
|      | |                 ‾‾|‾‾‾|‾‾‾‾   	         |
|      | |                   |   |			 |
|                           			         |
|  скажи суп             соли суп 53 раза        	 |
|   5 раз                           		         |
|                             				 |
|             вызови их сегодня                          |
|               не отравись!                     	 |
|                             				 |
‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
"""
soupman = """
    Супмэн
     _____
    ( . . )
     ( / )
___   ‾|‾‾  __
   \‾‾‾‾‾‾‾/  |
    |  S   |  |
    |      |  |
    \_____/
      | |
      | |
"""
saltman = """
      Сольмэн
        ____
       ( ' ' )
        ( ~ )     |
   __    ‾|‾‾ ____|
  |  |‾‾‾‾‾‾‾‾|
 |   | S      |
|    | /‾\/‾\ |
     |/      \|
     ‾‾|‾‾‾|‾‾‾‾
       |   |
"""
logo = """
        _________________________________________________________________
        |  ____   ___  _   _ ____    _____    _  _____ ___ _   _  ____  |
        | / ___| / _ \| | | |  _ \  | ____|  / \|_   _|_ _| \ | |/ ___| |
        | \___ \| | | | | | | |_) | |  _|   / _ \ | |  | ||  \| | |  _  |
        |  ___) | |_| | |_| |  __/  | |___ / ___ \| |  | || |\  | |_| | |
        | |____/ \___/ \___/|_|     |_____/_/   \_\_| |___|_| \_|\____| |
        |                                                               |
        |       ____ ___ __  __ _   _ _        _  _____ ___  ____       |
        |      / ___|_ _|  \/  | | | | |      / \|_   _/ _ \|  _ \      |
        |      \___ \| || |\/| | | | | |     / _ \ | || | | | |_) |     |
        |       ___) | || |  | | |_| | |___ / ___ \| || |_| |  _ <      |
        |      |____/___|_|  |_|\___/|_____/_/   \_\_| \___/|_| \_\     |
        |                                                               |
        ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                                       ____
                                       |  |
                                       |  |
                                       |  |
     _____                             |  |                            ____
    ( . . )                            |  |                           ( ' ' )
     ( / )                             |  |                            ( ~ )     |
___   ‾|‾‾  __                         |  |                       __    ‾|‾‾ ____|
   \‾‾‾‾‾‾‾/  | \                     _|__|_                   / |  |‾‾‾‾‾‾‾‾|
    |  S   |  |  \                   (      )                 / |   | S      |
    |      |  |   \                 (        )               / |    | /‾\/‾\ |
    \_____/        \                (        )              /       |/      \|
      | |           \                (      )              /        ‾‾|‾‾‾|‾‾‾‾
      | |            \                (    )              /           |   |
                     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
(я не смог сделать такой текст русским, сорян)
(перевод: СИМУЛЯТОР ПОЕДАНИЯ СУПА)
"""
fork = """
|   |    |
|   |    |
|   |    |
|   |    |
‾‾‾‾|‾‾‾‾‾
    |
    |
    |
    |
    |
    |
    |
"""
#vars and lists
SpoonUpgrade = False
if GotEnd1:
    if GotEnd2:
        if GotEnd3:
            SpoonUpgrade = True
soupeaten = False
souppoisoned = True
toomuchsalt = False
forkysoup = False
garlicsoup = False
garlicbread = False
saltiness = 0
soupiness = 0
breakout = False
hotel = "trivago"
#actions
def save():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    f = open(varspy, 'w')
    f.write("GotEnd1 = " + str(GotEnd1))
    f.close()
    f = open(varspy, 'a')
    f.write("\nGotEnd2 = " + str(GotEnd2))
    f.write("\nGotEnd3 = " + str(GotEnd3))
    f.write("\nGotEnd4 = " + str(GotEnd4))
    f.write("\nGotEnd5 = " + str(GotEnd5))
    f.write("\nGotEnd6 = " + str(GotEnd6))
    f.write("\nReleasedSaltman = " + str(ReleasedSaltman))
    f.write("\nReleasedSoupman = " + str(ReleasedSoupman))
    f.write("\nGotFork = " + str(GotFork))
    f.write("\nGotBread = " + str(GotBread))
    f.write("\nGotGarlic = " + str(GotGarlic))
    f.write("\nGotSaltSphere = " + str(GotSaltSphere))
    f.write("\nGotSoupSphere = " + str(GotSoupSphere))
    f.close()
def eatsoup():
    global soupeaten
    print("Ты съел суп.")
    mixer.Channel(1).play(mixer.Sound('sound/soup eating.wav'))
    sleep(3)
    soupeaten = True
def addsalt():
    try:
        global GotEnd1
        global GotEnd2
        global GotEnd3
        global GotEnd4
        global GotEnd5
        global GotEnd6
        global ReleasedSaltman
        global ReleasedSaltman
        global GotFork
        global GotSaltSphere
        global GotSoupSphere
        global GotBread
        global GotGarlic
        global saltiness
        global souppoisoned
        global toomuchsalt
        global SpoonUpgrade
        global breakout
        howmuch = int(input("Сколько соли?\n"))
        print("Ты добавил " + str(howmuch) + " соли.")
        mixer.Channel(1).play(mixer.Sound('sound/salt shake.wav'))
        sleep(5)
        print("Теперь перемешивай")
        stir = 0
        while stir != "перемешать":
            stir = input(">")
            if stir == "перемешать":
                print("Ты перемешал суп.")
                mixer.Channel(1).play(mixer.Sound('sound/stir.wav'))
                sleep(6)
            else:
                print("просто напиши \"перемешать\"")
        saltiness += howmuch
        if saltiness > 9:
            souppoisoned = False
            if saltiness > 19:
                toomuchsalt = True
        if ReleasedSaltman == False:
            if saltiness == 53:
                if SpoonUpgrade:
                    print("Твоя ложка становится комически большой, так что ты себя бъёшь по голове ей.")
                    print("Очень солёный индивидуал выходит из твоего черепа, который треснул.")
                    mixer.music.stop()
                    mixer.music.unload()
                    mixer.music.load("sound/Man of Salt.wav")
                    mixer.music.play(-1)
                    print(saltman)
                    print("наконец-то, я освобожден из этой мозговой™ и костяной™ тюрьмы которой является твоя смертная голова")
                    if ReleasedSoupman == False:
                        print("не забудь освободить супмэна")
                    ReleasedSaltman = True
                    save()
                    sleep(8)
                    mixer.music.stop()
                    mixer.music.unload()
                    mixer.music.load("sound/normal days.wav")
                    mixer.music.play(-1)
        else:
            if GotEnd4:
                if saltiness == 53:
                    if GotSaltSphere:
                        breakout = True
                    else:
                        if forkysoup:
                            print("идиот твоя вилка расплавилась так что мы просто дадим тебе концовку 4")
                            breakout = True
                        else:
                            print("твоя вилка начинает светится так что ты делаешь логическое: колишь себя в лоб.")
                            print("Никакой крови нет, но странная жидкость которая ломает законы физики вытекает и становится сферой.")
                            mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
                            print("(Ты получил Сферу Соли! Возможно это то что Сольмэн забыл в твоей голове.)")
                            GotSaltSphere = True
                            save()
    except:
        print("мне нужно число, идиот")
def lookundertable():
    global soupnsalt
    global SpoonUpgrade
    print("Под столом написано:")
    if SpoonUpgrade:
        print(soupnsalt)
    else:
        print("Не соли - не живи.\nСоли слишком много - тоже сдохни.\nСоли правильно - живи.")
def clear():
    if os.name == "nt":
        _ = os.system("cls")
    else:
        _ = os.system("clear")
def eatsoupwithfork():
    global forkysoup
    print("Ты попытался съесть суп вилкой. Она расплавилась, теперь у тебя вилочный суп.")
    forkysoup = True
def addgarlic():
    global garlicsoup
    mixer.Channel(1).play(mixer.Sound('sound/garlic.wav'))
    print("Ты добавил чеснок в суп. Что-то не так.")
    mixer.music.stop()
    mixer.music.unload()
    garlicsoup = True
    sleep(3)
def addbread():
    global souppoisoned
    global toomuchsalt
    print("Ты добавил хлеб в суп.")
    if souppoisoned:
        print("Он растворился от отравы")
    elif toomuchsalt:
        print("Он растворился от соли")
    else:
        print("Это большое улучшение.")
    print("На столе появился ещё один кусок хлеба.")
def eatbread():
    print("Ты съел хлеб. Было вкусно, но ничего не произошло, кроме того что на столе появился ещё один кусок хлеба.")
def eatgarlic():
    print("Ты съел чеснок. На вкус как что-то которое надо есть на хлебе, а не просто так. На столе появился ещё один кусок чеснока.")
def makegarlicbread():
    global garlicbread
    print("Ты магически соединил чеснок и хлеб в чесночный хлеб.")
    mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
    garlicbread = True
def eatgarlicbread():
    global garlicbread
    if garlicbread:
        print("ммммммммммммммммм вкусна")
        print("Ты превратился в микроволновку (шучу).")
        garlicbread = False
    else:
        print("У тебя нет чесночного хлеба.")
#endings
def deathbypoison():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load("sound/cruel soup cruel life.wav")
    mixer.music.play(-1)
    mixer.Channel(1).play(mixer.Sound('sound/dying.wav'))
    print("Суп был отравлен, как и все другие супы, так что ты сдох")
    print("КОНЦОВКА 1/?: ОТРАВА")
    if GotEnd1 == False:
        GotEnd1 = True
        save()
def saltylife():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load("sound/Alive but salty.wav")
    mixer.music.play(-1)
    print("Суп был отравлен, как и все другие супы. НО, магическая сила соли нейтрализировала отраву, так что ты жив.")
    print("КОНЦОВКА 2/?: ЖИВ НО СОЛЁН")
    if GotEnd2 == False:
        GotEnd2 = True
        save()
def toosalty():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load("sound/Life is salty.wav")
    mixer.music.play(-1)
    mixer.Channel(1).play(mixer.Sound('sound/dying.wav'))
    print("Ты добавил слишком много соли. Отрава супа была нейтрализирована, но ты сдох от дегидрации/отравы натрием/и тд.")
    print("КОНЦОВКА 3/?: СЛИШКОМ СОЛЁНО")
    if GotEnd3 == False:
        GotEnd3 = True
        save()
def ascend():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    if ReleasedSaltman:
        if ReleasedSoupman:
            print("Сломав круговорот супа, ты телепортируешся в безопасное место с помощью сил Сольмэна и Супмэна.")
            print("КОНЦОВКА 4/?: КРУГОВОРОТ СЛОМАН")
            if GotEnd4 == False:
                GotEnd4 = True
                save()
def silverpoisoning():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    mixer.music.stop()
    mixer.music.unload()
    mixer.music.load("sound/A Silver End.wav")
    mixer.music.play(-1)
    mixer.Channel(1).play(mixer.Sound('sound/dying.wav'))
    print("Ты умер от отравы серебром, т.к. ты съел вилку которая смешалась с супом.")
    print("Концовка 5/?: ВИЛОЧНАЯ СМЕРТЬ")
    if GotEnd5 == False:
        GotEnd5 = True
        save()
def necksnap():
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSaltman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    mixer.music.load("sound/No.wav")
    mixer.music.play(-1)
    mixer.Channel(1).play(mixer.Sound('sound/neck snapping.wav'))
    print("Внезапно, я (главный програмист этой игры, Сириларон) появляюсь сзади тебя и ломаю тебе шею потому-что я не согласен с тем что ты только что сделал.")
    print("Концовка 6/?: СЛОМАННАЯ ШЕЯ")
    if GotEnd6 == False:
        GotEnd6 = True
        save()

#dicts
soupyanswers = {
"съесть суп": eatsoup,
"съесть": eatsoup,
"добавить соль": addsalt,
"посмотреть под стол": lookundertable
}
if GotFork:
    soupyanswers["съесть суп вилкой"] = eatsoupwithfork
if GotBread:
    soupyanswers["добавить хлеб"] = addbread
    soupyanswers["съесть хлеб"] = eatbread
if GotGarlic:
    soupyanswers["добавить чеснок"] = addgarlic
    soupyanswers["съесть чеснок"] = eatgarlic
if GotBread and GotGarlic:
    soupyanswers["сделать чесночный хлеб"] = makegarlicbread
    soupyanswers["съесть чесночный хлеб"] = eatgarlicbread
#game
def loopofsoup():
    global soup
    global salt
    global spoon
    global SpoonUpgrade
    global soupiness
    global soupnsalt
    global soupyanswers
    global soupman
    global saltman
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSoupman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    global forkysoup
    global saltiness
    global souppoisoned
    global toomuchsalt
    global breakout
    global fork
    clear()
    mixer.init()
    mixer.music.load('sound/normal days.wav')
    mixer.music.play(-1)
    print("Ты окружён невидимыми стенами, в тёмной пустоте™. Ты сидишь на стуле, на столе впереди тебя тарелка супа.")
    print(soup)
    print("Рядом с ней соль.")
    print(salt)
    print("Ещё ложка.")
    if SpoonUpgrade:
        print("Она немного светится.")
        if GotEnd4 == False:
            print("Ты чувствуешь нужду посмотреть под стол.")
    print(spoon)
    if GotFork:
        print("Вилка тоже тут.")
        print(fork)
    if GotGarlic:
        print("И чеснок.")
    if GotBread:
        print("И хлеб.")
    #loop of soup
    while soupeaten == False:
        print("Что ты хочешь сделать?")
        options = "съесть суп, добавить соль, суп, посмотреть под стол"
        if GotFork:
            options = options + ", съесть суп вилкой"
        if GotBread:
            options = options + ", добавить хлеб, съесть хлеб"
        if GotGarlic:
            options = options + ", добавить чеснок, съесть чеснок"
        if GotBread and GotGarlic:
            options = options + ", сделать чесночный хлеб, съесть чесночный хлеб"
        print("Действия: " + options)
        answer = input(">")
        if answer not in soupyanswers:
            if answer == "суп":
                print("s̸̟̄̕o̶̤̬̅u̸͙͍̾p̵̫͂̚")
                soupiness += 1
                if ReleasedSoupman == False:
                    if soupiness == 5:
                        if SpoonUpgrade == True:
                            print("Твоя ложка становится комически большой, так что ты себя бъёшь по голове ей.")
                            print("Очень супный индивидуал выходит из твоего черепа, который треснул.")
                            mixer.music.stop()
                            mixer.music.unload()
                            mixer.music.load("sound/Can you eat him with a spoon.wav")
                            mixer.music.play(-1)
                            print(soupman)
                            print("Наконец, краниальная тюрьма которой является твой череп сломана.")
                            if ReleasedSaltman == False:
                                print("не забудь освободить сольмэна")
                            ReleasedSoupman = True
                            save()
                            sleep(8)
                            mixer.music.stop()
                            mixer.music.unload()
                            mixer.music.load("sound/normal days.wav")
                            mixer.music.play(-1)
                else:
                    if GotEnd4:
                        if soupiness == 5:
                            if GotSoupSphere:
                                breakout = True
                            else:
                                if forkysoup:
                                    print("идиот твоя вилка расплавилась так что мы просто дадим тебе концовку 4")
                                    breakout = True
                                else:
                                    print("твоя вилка начинает светится так что ты делаешь логическое: колишь себя в лоб.")
                                    print("Никакой крови нет, но странная жидкость которая ломает законы физики вытекает и становится сферой.")
                                    mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
                                    print("(Ты получил Сферу Супа! Возможно это то что Супмэн забыл в твоей голове.)")
                                    GotSoupSphere = True
                                    save()

            else:
                print("это не в списке действий")
        else:
            action = soupyanswers[answer]
            action()
        if garlicsoup:
            break
        if GotEnd4 == False:
            if ReleasedSaltman:
                if ReleasedSoupman:
                    breakout = True

        if breakout:
            mixer.music.stop()
            mixer.music.unload()
            mixer.music.load("sound/Salty Soup.wav")
            mixer.music.play(-1)
            print("Силы Сольмэна и Супмэна освобождают тебя из круговорота супа!")
            break
    #the moment of truth
    if soupeaten:
        if forkysoup:
            silverpoisoning()
        elif souppoisoned:
            deathbypoison()
        elif toomuchsalt:
            toosalty()
        else:
            saltylife()
        sleep(10)
        mixer.music.stop()
        mixer.music.unload()
        mixer.music.load("sound/normal days.wav")
        mixer.music.play(-1)
        if GotEnd4:
            clear()
            mainmenu()
    else:
        if garlicsoup:
            necksnap()
            sleep(10)
            if GotEnd4:
                clear()
                mainmenu()
        else:
            if ReleasedSaltman:
                if ReleasedSoupman:
                    print("Напиши \"телепорт\" чтобы телепортироватся.")
                    ascension = 0
                    while ascension != "телепорт":
                        ascension = input(">")
                        if ascension == "телепорт":
                            ascend()
                            sleep(10)
                            clear()
                            mainmenu()
#main menu
def mainmenu():
    global soup
    global salt
    global spoon
    global SpoonUpgrade
    global soupiness
    global soupnsalt
    global soupyanswers
    global soupman
    global saltman
    global GotEnd1
    global GotEnd2
    global GotEnd3
    global GotEnd4
    global GotEnd5
    global GotEnd6
    global ReleasedSaltman
    global ReleasedSoupman
    global GotFork
    global GotSaltSphere
    global GotSoupSphere
    global GotBread
    global GotGarlic
    global forkysoup
    global saltiness
    global souppoisoned
    global toomuchsalt
    global garlicsoup
    global logo
    global soupeaten
    global breakout
    soupiness = 0
    saltiness = 0
    breakout = False
    toomuchsalt = False
    souppoisoned = True
    forkysoup = False
    soupeaten = False
    clear()
    try:
        mixer.init()
    except:
        pass
    try:
        mixer.music.stop()
        mixer.music.unload()
    except:
        pass
    mixer.music.load("sound/You can rest here, soupy traveler.wav")
    mixer.music.play(-1)
    print(logo)
    command = 0
    while True:
        print("Что ты хочешь сделать? Действия: начать игру, посмотреть концовки, кухня, выйти")
        command = input(">")
        if command == "начать игру":
            break
        elif command == "посмотреть концовки":
            print("Концовка 1: " + str(GotEnd1))
            print("Концовка 2: " + str(GotEnd2))
            print("Концовка 3: " + str(GotEnd3))
            print("Концовка 4: " + str(GotEnd4))
            print("Концовка 5: " + str(GotEnd5))
            print("Концовка 6: " + str(GotEnd6))
            print("Больше концовок будет скоро™")
        elif command == "кухня":
            print("Ты входишь в кухню. Пока что, ты не можешь с ней интерактировать. Супмэн и Сольмэн тоже здесь.")
            while True:
                print("Что ты хочешь сделать? Действия: выйти из кухни, говорить")
                kommand = input(">")
                if kommand == "выйти из кухни":
                    break
                elif kommand == "говорить":
                    if GotFork:
                        if GotSaltSphere:
                            if GotBread:
                                print("Похоже, Сольмэн слишком занят.")
                            else:
                                print("Сольмэн: Вот она, Сфера Соли! Вот, держи хлеб.")
                                sleep(3)
                                mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
                                print("Ты получил хлеб!")
                                GotBread = True
                                soupyanswers["добавить хлеб"] = addbread
                                soupyanswers["съесть хлеб"] = eatbread
                                save()
                                sleep(3)
                        else:
                            print("Сольмэн: Добавь 53 соли в суп.")
                        if GotSoupSphere:
                            if GotGarlic:
                                print("Похоже, Супмэн слишком занят.")
                            else:
                                print("Супмэн: Сфера супа! Не могу поверить что я её там забыл. Вот, держи чеснок.")
                                sleep(3)
                                mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
                                print("Ты получил чеснок!")
                                GotGarlic = True
                                soupyanswers["добавить чеснок"] = addgarlic
                                soupyanswers["съесть чеснок"] = eatgarlic
                                save()
                                sleep(3)
                        else:
                            print("Супмэн: Скажи суп 5 раз.")
                    else:
                        print("Сольмэн: Мы делаем эту кухню используемой смертными.")
                        sleep(3)
                        print("Супмэн: Но мы забыли кое-что в твоей голове.")
                        sleep(3)
                        print("Сольмэн: Можешь сделать то что сделал чтобы нас вызвать?")
                        sleep(3)
                        print("Soupman: Но этой вилкой.")
                        sleep(1)
                        mixer.Channel(1).play(mixer.Sound('sound/pickup.wav'))
                        print("Ты получил вилку!")
                        GotFork = True
                        soupyanswers["съесть суп вилкой"] = eatsoupwithfork
                        save()
                        sleep(3)
                if GotBread and GotGarlic:
                    soupyanswers["сделать чесночный хлеб"] = makegarlicbread
                    soupyanswers["съесть чесночный хлеб"] = eatgarlicbread
        elif command == "выйти":
            break
        else:
            print("Это не действие")
    if command == "начать игру":
        loopofsoup()
#start game
if GotEnd4:
    mainmenu()
else:
    loopofsoup()
