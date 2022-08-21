wynik=0


print("Witam w kalkulatorze Wiktora,\nCzy chcesz wprowadzic liczby i wykonac dzialanie?")
x=int(input("\nWpiz 1 jeśli tak lub 2 jeśli nie\n"))
while x==1:
    a=input("Wpisz pierwszą liczbę: ")
    b=input("Wpisz drugą liczbę: ")
                
    print("\nJakie działanie chcesz wykonać?\n1.Dodawanie\n2.Odejmowanie\n3.Mnożenie\n4.Dzielenie\n5.Koniec programu")
    y=input("\n\nDokonaj wyboru: ")

    if int(y)==1:
        wynik=int(a)+int(b)
        print(wynik)
    elif int(y)==2:
        wynik=int(a)-int(b)
        print(wynik)
    elif int(y)==3:
        wynik=int(a)*int(b)
        print(wynik)
    elif int(y)==4:
        wynik=int(a)/int(b)
        print(wynik)
    elif int(y)==5:
        break
    else:
        print("Niepoprawny wybór, Koniec Programu")
    print("Czy chcesz nadal liczyć?")
    x=int(input("\nWpisz 1 jeśli tak lub 2 jeśli nie\n"))

    if x==2:
        break
print("Koniec programu")

