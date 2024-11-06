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
plt.plot(tid_sauda, temperatur_sauda, label = "Temperatur Sauda")
plt.plot(tid_sinnes, temperatur_sinnes, label = "Temperatur Sinnes")
plt.xlabel("Tid")
plt.ylabel("Temperatur")
plt.legend()


plt.subplot(2, 1, 2)
plt.title("Trykkvariasjoner")
plt.plot(tider_met_dt, trykk_met, label = "Absoluttrykk MET") 
plt.plot(tider_dt, trykk_abs, label = "Absoluttrykk")
plt.plot(tider_baro_dt, trykk_bar, label = "Barometrisk trykk")
plt.plot(tid_sauda, trykk_sauda, label = "Trykk Sauda")
plt.plot(tid_sinnes, trykk_sinnes, label = "Trykk Sinnes")
plt.xlabel("Tid")
plt.ylabel("Trykk")
plt.legend()

# Samle alle tidsdataene i én liste
alle_tidspunkter = tider_met_dt + tider_dt + tider_baro_dt + tid_sauda_dt

# Sett x-aksens grenser basert på minimums- og maksimumstidspunkt
plt.xlim([min(alle_tidspunkter), max(alle_tidspunkter)])

# plt.xlim([min(tider_met_dt + tider_dt), max(tider_met_dt + tider_dt)])  # Sett grensene for x-aksenO


plt.xticks(rotation=45)
plt.tight_layout()
plt.show()