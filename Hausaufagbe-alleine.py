import datetime

def CurrentDayTime():
    return datetime.datetime.now
def whenTheYearEnds():
    currentday = datetime.datetime.now
    endofyear = (2024, 12, 31)
    return (endofyear - currentday)
def abfrage():
    userinput = input("Wähle eine Aktion (Aktuelles Datum - 1, Wann das Jahr endet - 2): ")
    if userinput == "1":
        result = CurrentDayTime()
    elif userinput == "2":
        result = whenTheYearEnds()
    else:
        print("Ungültige Eingabe")

abfrage()