import datetime
import matplotlib.pyplot as plt
import math

def glidende_gjennomsnitt(tider, temperaturer, n):
    gyldige_tider = []
    gjennomsnitt =[]
    standardavvik = []

    for i in range(n, len(temperaturer)-n):
        temp_slice = temperaturer[i - n:i + n + 1]
        gjennomsnitt_verdi = sum(temp_slice) / len(temp_slice)
        
        varians = sum((x - gjennomsnitt_verdi) ** 2 for x in temp_slice) / (len(temp_slice) - 1)
        std_avvik = math.sqrt(varians)

        gyldige_tider.append(tider[i])
        gjennomsnitt.append(gjennomsnitt_verdi)
        standardavvik.append(std_avvik)

    return gyldige_tider, gjennomsnitt, standardavvik

#Lister for ulike målinger
temperaturer_met = []
tider_met = []
trykk_met = []
temperaturer = []
tider = []
tider_baro = []
trykk_abs = []
trykk_bar = []

with open("temperatur_trykk_met_samme_rune_time_datasett.csv.txt", "r") as fil: #Åpner og leser av fil
    for linje in fil:
        Del = linje.strip().split(';')              #Strip fjerner mellomrom etc., split lager elementer ved ;
        if len(Del) >= 5:                      
            tid = Del[2]                            #Legger til 2. element i Del til tid
            temperatur = Del[3].replace(',', '.')   #Legger til 3.element i Del til temperatur og bytter , med .
            trykk = Del[4].replace(',', '.')
            try:
                if "am" in tid or "pm" in tid:      #Tar hensyn til pm og am
                    dato_obj = datetime.datetime.strptime(tid, "%d/%m/%Y %I:%M:%S %p") 
                else:
                    dato_obj = datetime.datetime.strptime(tid, "%d.%m.%Y %H:%M")
                
                tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")   #Omformer til standardtid
                temperatur_float = float(temperatur)
                trykk_float = float(trykk)
                tider_met.append(tid_standard)
                temperaturer_met.append(temperatur_float)               #Legger til verdier i de tomme listene
                trykk_met.append(trykk_float)
            except ValueError:                                          #Dersom en verdi error oppstår, slik som i første linje, hopper python over
                pass

with open("trykk_og_temperaturlogg_rune_time.csv.txt", "r") as fil:
    for linje in fil:
        Del = linje.strip().split(';')
        if len(Del) >= 5:
            tid = Del[0]
            temperatur = Del[4].replace(',', '.')
            trykk_abso = Del[3].replace(',', '.')
            trykk_baro = Del[2].replace(',', '.')

            if trykk_baro == (''):
                try:
                    if "am" in tid or "pm" in tid:    #Tar hensyn til pm og am
                        if " 00:" in tid:
                            tid = tid.replace("00:", "12:", 1)
                        dato_obj = datetime.datetime.strptime(tid, "%m/%d/%Y %I:%M:%S %p")
                    else:
                        dato_obj = datetime.datetime.strptime(tid, "%m.%d.%Y %H:%M")
                    
                    tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")
                    temperatur_float = float(temperatur)
                    trykk_abs_float = float(trykk_abso) * 10
                    
                    tider.append(tid_standard)
                    temperaturer.append(temperatur_float)
                    trykk_abs.append(trykk_abs_float)
                except ValueError:
                    pass
            else:
                try:
                    if "am" in tid or "pm" in tid:      #Tar hensyn til pm og am
                        if " 00:" in tid:
                            tid = tid.replace("00:", "12:", 1)
                        dato_obj = datetime.datetime.strptime(tid, "%m/%d/%Y %I:%M:%S %p")
                    else:
                        dato_obj = datetime.datetime.strptime(tid, "%m.%d.%Y %H:%M")
                    
                    tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")
                    temperatur_float = float(temperatur)
                    trykk_abs_float = float(trykk_abso) * 10
                    trykk_bar_float = float(trykk_baro) * 10
                    
                    trykk_bar.append(trykk_bar_float)
                    tider_baro.append(tid_standard)
                    tider.append(tid_standard)
                    temperaturer.append(temperatur_float)
                    trykk_abs.append(trykk_abs_float)
                except ValueError:
                    pass

#Lister for Sinnes og Sauda

tid_sinnes = []
tid_sauda = []
temperatur_sinnes = []
temperatur_sauda = []
trykk_sinnes = []
trykk_sauda = []


with open("temperatur_trykk_sinnes_samme_tidsperiode.csv.txt", "r") as fil:
    for linje in fil:
        Del = linje.strip().split(';')             
        if len(Del) >= 5:                      
            tid = Del[2]                           
            temperatur = Del[3].replace(',', '.')  
            trykk = Del[4].replace(',', '.')
            try:
                if "am" in tid or "pm" in tid:      #Tar hensyn til pm og am
                    dato_obj = datetime.datetime.strptime(tid, "%d/%m/%Y %I:%M:%S %p") 
                else:
                    dato_obj = datetime.datetime.strptime(tid, "%d.%m.%Y %H:%M")

                tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")  
                temperatur_float = float(temperatur)
                trykk_float = float(trykk)
                tid_sinnes.append(tid_standard)
                temperatur_sinnes.append(temperatur_float)               
                trykk_sinnes.append(trykk_float)
            except ValueError:                                          
                pass

with open("temperatur_trykk_sauda.csv.txt", "r") as fil:
    for linje in fil:
        Del = linje.strip().split(';')              
        if len(Del) >= 5:                      
            tid = Del[2]                           
            temperatur = Del[3].replace(',', '.')  
            trykk = Del[4].replace(',', '.')
            try:
                if "am" in tid or "pm" in tid:      #Tar hensyn til pm og am
                    dato_obj = datetime.datetime.strptime(tid, "%d/%m/%Y %I:%M:%S %p") 
                else:
                    dato_obj = datetime.datetime.strptime(tid, "%d.%m.%Y %H:%M")

                tid_standard = dato_obj.strftime("%Y-%m-%d %H:%M:%S")  
                temperatur_float = float(temperatur)
                trykk_float = float(trykk)
                tid_sauda.append(tid_standard)
                temperatur_sauda.append(temperatur_float)               
                trykk_sauda.append(trykk_float)
            except ValueError:                                          
                pass


tider_met_dt = [datetime.datetime.strptime(tid, "%Y-%m-%d %H:%M:%S") for tid in tider_met]
tider_dt = [datetime.datetime.strptime(tid, "%Y-%m-%d %H:%M:%S") for tid in tider]
tider_baro_dt = [datetime.datetime.strptime(tid, "%Y-%m-%d %H:%M:%S") for tid in tider_baro]
tid_sinnes_dt = [datetime.datetime.strptime(tid, "%Y-%m-%d %H:%M:%S") for tid in tid_sinnes]
tid_sauda_dt = [datetime.datetime.strptime(tid, "%Y-%m-%d %H:%M:%S") for tid in tid_sauda]

n=30
gyldige_tider, gjennomsnitt, std_avvik = glidende_gjennomsnitt(tider_dt, temperaturer, n)

trykk_diff = [abs_trykk - baro_trykk for abs_trykk, baro_trykk in zip(trykk_abs, trykk_bar) if abs_trykk is not None and baro_trykk is not None]
tid_diff = [tid for tid, abs_trykk, baro_trykk in zip(tider_baro_dt, trykk_abs, trykk_bar) if abs_trykk is not None and baro_trykk is not None]

n = 10
gyldige_tider_diff = tid_diff[n:-n]
gjennomsnitt_diff = [sum(trykk_diff[i-n:i+n+1]) / (2*n+1) for i in range(n, len(trykk_diff)-n)]

start_tid = datetime.datetime(2021, 6, 11, 17, 31)
slutt_tid = datetime.datetime(2021, 6, 12, 3, 5)

temperaturer_uis_filtered = []
tider_uis_filtered = []
temperaturer_met_filtered = []
tider_met_filtered = []

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

for tid, temperatur in zip(tider_met_dt, temperaturer_met):
    if start_tid <= tid <= slutt_tid:
        tider_met_filtered.append(tid)
        temperaturer_met_filtered.append(temperatur)

if temperaturer_met_filtered:
    max_temp_met = max(temperaturer_met_filtered)
    min_temp_met = min(temperaturer_met_filtered)

    temperaturfall_tider_met = [start_tid, slutt_tid]
    temperaturfall_values_met = [max_temp_met, min_temp_met]
else:
    temperaturfall_tider_met = []
    temperaturfall_values_met = []


min_temp_UiS = int(min(temperaturer))
max_temp_UiS = int(max(temperaturer))

min_temp_metro = int(min(temperaturer_met))
max_temp_metro = int(max(temperaturer_met))

plt.figure(figsize=(10, 10))
plt.subplot(5, 1, 1)
plt.title("Temperaturmålinger fra to kilder")
plt.plot(tider_met_dt, temperaturer_met, label="Måling fra Solas værstasjon")
plt.plot(tider_dt, temperaturer, label="Måling fra UiS")
plt.plot(gyldige_tider, gjennomsnitt, label="Gjennomsnittstemperatur")
plt.plot(temperaturfall_tider, temperaturfall_values, label="Temperaturfall Maksimal til Minimal for UiS")
plt.plot(temperaturfall_tider_met, temperaturfall_values_met, label="Temperaturfall Maksimal til Minimal for Metrologisk")
plt.plot(tid_sauda_dt, temperatur_sauda, label = "Temperatur Sauda")
plt.plot(tid_sinnes_dt, temperatur_sinnes, label = "Temperatur Sinnes")
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.legend()

plt.subplot(5, 1, 2)
plt.title("Trykkvariasjoner")
plt.plot(tider_met_dt, trykk_met, label = "Absoluttrykk MET") 
plt.plot(tider_dt, trykk_abs, label = "Absoluttrykk")
plt.plot(tider_baro_dt, trykk_bar, label = "Barometrisk trykk")
plt.plot(tid_sauda_dt, trykk_sauda, label = "Trykk Sauda")
plt.plot(tid_sinnes_dt, trykk_sinnes, label = "Trykk Sinnes")
plt.xlabel("Tid")
plt.ylabel("Trykk")
plt.legend()

plt.subplot(5, 1, 3)
plt.title("Differanse mellom absolutt og barometrisk trykk")
plt.plot(gyldige_tider_diff, gjennomsnitt_diff, label="Trykkdifferanse")
plt.xlabel("Tid")
plt.ylabel("Trykkdifferanse")
plt.legend()

plt.subplot(5,1,4)
plt.title("Standardavvik for temperaturmålinger fra UiS")
plt.errorbar(gyldige_tider, gjennomsnitt, yerr=std_avvik, errorevery=30, capsize=5, label="Gjennomsnitt med Standardavvik")
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.legend()

# Samle alle tidsdataene i én liste
alle_tidspunkter = tider_met_dt + tider_dt + tider_baro_dt + tid_sauda_dt + tid_sinnes_dt

# Sett x-aksens grenser basert på minimums- og maksimumstidspunkt
plt.xlim([min(alle_tidspunkter), max(alle_tidspunkter)])


plt.subplot(5, 2, 9)
plt.hist(temperaturer, bins=range(min_temp_UiS, max_temp_UiS + 2))
plt.xlabel("Temperatur")
plt.ylabel("Antall observasjoner")
plt.title("Antall observerte temperaturer ved UiS")

plt.subplot(5, 2, 10)
plt.hist(temperaturer_met, bins=range(min_temp_metro, max_temp_metro + 2))
plt.xlabel("Temperatur")
plt.ylabel("Antall observasjoner")
plt.title("Antall observerte temperaturer av Metrologisk institutt")


plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Oppgave e)
# Lister for å lagre forskjellene og tilhørende tidspunkter
temperatur_differanser = []
trykk_differanser = []
tidspunkter = []

for i in range(len(tider_met_dt)): #løkke for å finne samsvarende tidspunkter
    met_tid = tider_met_dt[i]
    if met_tid in tider_dt:
        j = tider_dt.index(met_tid)
        
        # Beregn forskjellen i temperatur og trykk
        temp_diff = abs(temperaturer_met[i] - temperaturer[j])
        trykk_diff = abs(trykk_met[i] - trykk_abs[j])
        
        # Legg til i lister for forskjeller og tidspunkt
        temperatur_differanser.append(temp_diff)
        trykk_differanser.append(trykk_diff)
        tidspunkter.append(met_tid)

# Beregn gjennomsnittlig forskjell
gjennomsnitt_temp_diff = sum(temperatur_differanser) / len(temperatur_differanser)
gjennomsnitt_trykk_diff = sum(trykk_differanser) / len(trykk_differanser)

# Finn tidspunktene med høyeste og laveste forskjell for temperatur og trykk
maks_temp_diff = max(temperatur_differanser)
min_temp_diff = min(temperatur_differanser)
maks_trykk_diff = max(trykk_differanser)
min_trykk_diff = min(trykk_differanser)

tid_maks_temp_diff = tidspunkter[temperatur_differanser.index(maks_temp_diff)]
tid_min_temp_diff = tidspunkter[temperatur_differanser.index(min_temp_diff)]
tid_maks_trykk_diff = tidspunkter[trykk_differanser.index(maks_trykk_diff)]
tid_min_trykk_diff = tidspunkter[trykk_differanser.index(min_trykk_diff)]

# Utskrift av resultatene
print(f"Gjennomsnittlig temperaturforskjell: {gjennomsnitt_temp_diff:.2f}°C")
print(f"Gjennomsnittlig trykkforskjell: {gjennomsnitt_trykk_diff:.2f} hPa")

print(f"Største temperaturforskjell på {maks_temp_diff:.2f}°C ved {tid_maks_temp_diff}")
print(f"Laveste temperaturforskjell på {min_temp_diff:.2f}°C ved {tid_min_temp_diff}")

print(f"Største trykkforskjell på {maks_trykk_diff:.2f} hPa ved {tid_maks_trykk_diff}")
print(f"Laveste trykkforskjell på {min_trykk_diff:.2f} hPa ved {tid_min_trykk_diff}")