import datetime
import matplotlib.pyplot as plt

def glidende_gjennomsnitt(tider, temperaturer, n):
    gyldige_tider = []
    gjennomsnitt =[]

    for i in range(n, len(temperaturer)-n):
        temp_slice = temperaturer[i - n:i + n + 1]
        gjennomsnitt_verdi = sum(temp_slice) / len(temp_slice)

        gyldige_tider.append(tider[i])
        gjennomsnitt.append(gjennomsnitt_verdi)

    return gyldige_tider, gjennomsnitt

temperaturer_met = []
tider_met = []
trykk_met = []
temperaturer = []
tider = []
trykk_abs = []
trykk_bar = []

with open("temperatur_trykk_met_samme_rune_time_datasett.csv.txt", "r") as fil:
    for linje in fil:
        Del = linje.strip().split(';')
        if len(Del) >= 5:
            tid = Del[2]
            temperatur = Del[3].replace(',', '.')
            trykk = Del[4].replace(',', '.')
            try:
                if "am" in tid or "pm" in tid:
                    dato_obj = datetime.datetime.strptime(tid, "%d/%m/%Y %I:%M:%S %p")
                else:
                    dato_obj = datetime.datetime.strptime(tid, "%d.%m.%Y %H:%M")
                
                tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")
                temperatur_float = float(temperatur)
                trykk_float = float(trykk)
                tider_met.append(tid_standard)
                temperaturer_met.append(temperatur_float)
                trykk_met.append(trykk_float)
            except ValueError:
                pass

with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r") as fil:
    for linje in fil:
        Del = linje.strip().split(';')
        if len(Del) >= 5:
            tid = Del[0]
            temperatur = Del[4].replace(',', '.')
            trykk_abso = Del[3].replace(',', '.')
            trykk_baro = Del[2].replace(',', '.')
            try:
                dato_obj = datetime.datetime.strptime(tid, "%m.%d.%Y %H:%M")
                
                tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")
                temperatur_float = float(temperatur)
                trykk_abs_float = float(trykk_abso)
                if trykk_baro: #Oppdaget at det ikke er måling på alle linjene. Vet ikke om dette løste det
                    trykk_bar_float = float(trykk_baro)
                    trykk_bar.append(trykk_bar_float)
                tider.append(tid_standard)
                temperaturer.append(temperatur_float)
                trykk_abs.append(trykk_abs_float)
            except ValueError:
                pass

tider_met_dt = [datetime.datetime.strptime(tid, "%Y-%m-%d %H:%M:%S") for tid in tider_met]
tider_dt = [datetime.datetime.strptime(tid, "%Y-%m-%d %H:%M:%S") for tid in tider]

n=30
gyldige_tider, gjennomsnitt = glidende_gjennomsnitt(tider_dt, temperaturer, n)

start_tid = datetime.datetime(2021, 6, 11, 17, 31)
slutt_tid = datetime.datetime(2021, 6, 12, 3, 5)

temperaturer_uis_filtered = []
tider_uis_filtered = []

for tid, temperatur in zip(tider_dt, temperaturer):
    if start_tid <= tid <= slutt_tid:
        tider_uis_filtered.append(tid)
        temperaturer_uis_filtered.append(temperatur)

if temperaturer_uis_filtered:
    max_temp = max(temperaturer_uis_filtered)
    min_temp = min(temperaturer_uis_filtered)

  temperaturfall_tider = [start_tid, slutt_tid]
    temperaturfall_values = [max_temp, min_temp]
else:
    temperaturfall_tider = []
    temperaturfall_values = []

plt.figure(figsize=(10, 5))
plt.subplot(2, 1, 1)
plt.title("Temperaturmålinger fra to kilder")
plt.plot(tider_met_dt, temperaturer_met, label="Måling fra Solas værstasjon")
plt.plot(tider_dt, temperaturer, label="Måling fra UiS")
plt.plot(gyldige_tider, gjennomsnitt, label="Gjennomsnittstemperatur")
plt.plot(temperaturfall_tider, temperaturfall_values, label="Temperaturfall Maksimal til Minimal")
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.legend()

plt.subplot(2, 1, 2)
plt.title("Trykkvariasjoner")
plt.plot(tider_met_dt, trykk_met, label = "Absoluttrykk MET") #Fungerer alene
plt.plot(tider_dt, trykk_abs, label = "Absoluttrykk") #Fungerer alene
plt.plot(tider_dt, trykk_bar, label = "Barometrisk trykk") #Får den ikke opp,
plt.xlabel("Tid")
plt.yplot("Trykk")
plt.legend()

plt.xlim([min(tider_met_dt + tider_dt), max(tider_met_dt + tider_dt)])  # Sett grensene for x-aksenO


plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


#Får opp en error om at : ValueError: x and y must have same first dimension, but have shapes (12098,) and (2017,)
# Livar kan du fikse, se om du greier å endre på det?