date_today = input("Welcher Tag ist heute(JJJJ/MM/TT): ")

winter_holidays_start_2024 = "2024.12.24"
winter_holidays_end_2024 = "2025.01.01"
easter_holidays_start25 = "2025.04.17"
easter_holidays_end25 = "2025.04.22"
summer_holidays_start25 = "2025.08.08"
summer_holidays_end25 = "2025.08.20"
winter_holidays_start25 = "2025.12.23"
winter_holidays_end25 = "2026.01.02"
first_may = "2025.05.01"
christi = "2025.05.29"
pfingsti = "2025.06.09"
tag_der_einheit = "2025.10.03"
reformation = "2025.10.31"


if winter_holidays_start_2024 <= date_today <= winter_holidays_end_2024:
    print("Du hast heute heute frei dank der Winterferien 2024")
elif easter_holidays_start25 <= date_today <= easter_holidays_end25:
    print("Du hast heute heute frei dank der Osterferien 2025")
elif summer_holidays_start25 <= date_today <= summer_holidays_end25:
    print("Du hast heute heute frei dank der Sommerferien 2025")
elif winter_holidays_start25 <= date_today <= winter_holidays_end25:
    print("Du hast heute heute frei dank der Winterferien 2025")
elif date_today == first_may:
    print("Heute ist Tag der Arbeit, du hast heute frei. Geh raus und feier bisschen")
elif  date_today == christi:
    print("Heute ist Christi Himmelfahrt, du kannst dich wieder hinlegen")
elif  date_today == pfingsti:
    print("Heute ist Pfingstmontag, LIEGEN BLEIBEN")
elif  date_today == tag_der_einheit:
    print("Heute ist Tag der Einheit, du hast heute frei und mach bloss kein Finger krum")
elif  date_today == reformation:
    print("Heute ist Reformationstag, du hast heute frei")
else:
    print("Es handelt sich um einen regulären Schulungstag , wenn es nicht gerade Wochenende ist =]")
    

# Winterferien 2024 2024.12.24-2025.01.01
# Ostern 2025.04.18-2025.04.21
# Sommerferien 2025.08.11-2025.08.19
# Winterferien 2025 225.12.24-2026.01.01
# 1.Mai 2025.05.01
# Christi Himmelsfahrt 2025.05.29
# Pfingstmontag 2025.06.09
# Tag der deutschen Einheit 2025.10.03 
# Reformationstag 2025.10.31