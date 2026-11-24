def addieren(a, b):
    return a + b

def subtraktion(a, b):
    return a - b

def multiplikation(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Division durch 0 nicht möglich"
    return a / b

def main():
    print("Taschenrechner")
    print("1 fuer Addition")
    print("2 fuer Subtraktion")
    print("3 fuer Multiplikation")
    print("4 fuer Division")

    wahl = input("Wahl eingeben: ")

    match wahl:
        case "1":
            a = float(input("Erste Zahl: "))
            b = float(input("Zweite Zahl: "))
            print("Resultat: {}".format(addieren(a, b)))
        case "2":
            a = float(input("Erste Zahl: "))
            b = float(input("Zweite Zahl: "))
            print("Resultat: {}".format(subtraktion(a, b)))
        case "3":
            a = float(input("Erste Zahl: "))
            b = float(input("Zweite Zahl: "))
            print("Resultat: {}".format(multiplikation(a, b)))
        case "4":
            a = float(input("Erste Zahl: "))
            b = float(input("Zweite Zahl: "))
            print("Resultat: {}".format(division(a, b)))
        case _:
            print("Falsche Auswahl, das Programm wird beendet.")

if __name__ == "__main__":
    main()
