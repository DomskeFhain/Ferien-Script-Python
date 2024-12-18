import datetime

def CurrentDayTime():
    return datetime.datetime.now
def whenTheYearEnds():
    currentday = datetime.datetime.now
    endofyear = (2024, 12, 31)
    return (endofyear - currentday)
def daycounter():    
    from datetime import datetime
    aktuelles_datum = datetime.now()
    benutzer_datum_str = input("Bitte geben Sie ein Datum im Format TT.MM.JJJJ ein: ")
    benutzer_datum = datetime.strptime(benutzer_datum_str, "%d.%m.%Y")
    differenz = (benutzer_datum - aktuelles_datum).days
    if differenz > 0:
         print(f"Es sind noch {differenz} Tage bis zum {benutzer_datum_str}.")
    elif differenz < 0:
            print(f"Das Datum {benutzer_datum_str} liegt bereits in der Vergangenheit. Es sind {-differenz} Tage seitdem vergangen.")
    elif differenz == 0:
            print("Das eingegebene Datum ist heute.")
    else:
            print("Das eingegebene Datum hat nicht das richtige Format oder ist ungültig.")

def what_weekday_is_today(tag, monat, jahr):
    if monat < 3:
        monat += 12
        jahr -= 1
    k = jahr % 100
    j = jahr // 100
    wochentag_index = (tag + (13 * (monat + 1)) // 5 + k + (k // 4) + (j // 4) - (2 * j)) % 7
    wochentage = ["Samstag", "Sonntag", "Montag", "Dienstag", "Mittwoch", "Donnerstag", "Freitag"]

    return wochentage[wochentag_index]

tag = int(input("Geben Sie den Tag ein: "))
monat = int(input("Geben Sie den Monat ein: "))
jahr = int(input("Geben Sie das Jahr ein: "))

wochentag = what_weekday_is_today(tag, monat, jahr)
print(f"Der Wochentag für das Datum {tag}.{monat}.{jahr} ist: {wochentag}")

from datetime import datetime, timedelta

def zeit_in_zukunft():
    # Aktuelle Zeit abrufen
    jetzt = datetime.now()

    # Benutzereingabe für Zeitspanne
    eingabe = input("Geben Sie die Zeitspanne ein (z.B. '2 Stunden', '30 Minuten', '1 Tag'): ")

    # Zerlegen der Eingabe in Zahl und Einheit
    teile = eingabe.split()

    if len(teile) != 2:
        print("Ungültige Eingabe. Bitte geben Sie die Zeitspanne im Format '<Zahl> <Einheit>' ein.")
        return

    anzahl_str = teile[0]
    einheit = teile[1].lower()

    # Überprüfen, ob die Anzahl eine gültige Zahl ist
    if not anzahl_str.isdigit():
        print("Bitte geben Sie eine gültige Zahl ein.")
        return

    anzahl = int(anzahl_str)
    if einheit in ['minute', 'minuten']:
        zukunft = jetzt + timedelta(minutes=anzahl)
    elif einheit in ['stunde', 'stunden']:
        zukunft = jetzt + timedelta(hours=anzahl)
    elif einheit in ['tag', 'tage']:
        zukunft = jetzt + timedelta(days=anzahl)
    else:
        print("Ungültige Einheit. Bitte verwenden Sie 'Minuten', 'Stunden' oder 'Tage'.")
        return
    print(f"In {eingabe} wird es sein: {zukunft.strftime('%Y-%m-%d %H:%M:%S')}")
       
def abfrage():
    userinput = input("Wähle eine Aktion (Aktuelles Datum - 1, Wann das Jahr endet - 2, Tagzähler -3, Wochentag - 4, Zeitverschiebung - 5 ): ")
    if userinput == "1":
        result = CurrentDayTime()
    elif userinput == "2":
        result = whenTheYearEnds()
    elif userinput == "3":
        result = daycounter()
    elif userinput == "4":
        result = what_weekday_is_today()
    elif userinput == "5":
        result = time_in_future()
    else:
        print("Ungültige Eingabe")

abfrage()