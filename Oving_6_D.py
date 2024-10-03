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
temperaturer = []
tider = []

with open("temperatur_trykk_met_samme_rune_time_datasett.csv.txt", "r") as fil:
    for linje in fil:
        Del = linje.strip().split(';')
        if len(Del) >= 5:
            tid = Del[2]
            temperatur = Del[3].replace(',', '.')
            try:
                if "am" in tid or "pm" in tid:
                    dato_obj = datetime.datetime.strptime(tid, "%d/%m/%Y %I:%M:%S %p")
                else:
                    dato_obj = datetime.datetime.strptime(tid, "%d.%m.%Y %H:%M")
                
                tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")
                temperatur_float = float(temperatur)
                tider_met.append(tid_standard)
                temperaturer_met.append(temperatur_float)
            except ValueError:
                pass

with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r") as fil:
    for linje in fil:
        Del = linje.strip().split(';')
        if len(Del) >= 5:
            tid = Del[0]
            temperatur = Del[4].replace(',', '.')
            try:
                dato_obj = datetime.datetime.strptime(tid, "%m.%d.%Y %H:%M")
                
                tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")
                temperatur_float = float(temperatur)
                tider.append(tid_standard)
                temperaturer.append(temperatur_float)
            except ValueError:
                pass

tider_met_dt = [datetime.datetime.strptime(tid, "%Y-%m-%d %H:%M:%S") for tid in tider_met]
tider_dt = [datetime.datetime.strptime(tid, "%Y-%m-%d %H:%M:%S") for tid in tider]

n=30
gyldige_tider, gjennomsnitt = glidende_gjennomsnitt(tider_dt, temperaturer, n)

plt.figure(figsize=(10, 5))
plt.plot(tider_met_dt, temperaturer_met, label="Måling fra Solas værstasjon")
plt.plot(tider_dt, temperaturer, label="Måling fra UiS")
plt.plot(gyldige_tider, gjennomsnitt, label="Gjennomsnittstemperatur")
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.title("Temperaturmålinger fra to kilder")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()