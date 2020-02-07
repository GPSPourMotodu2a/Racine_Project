import time
import datetime

#Données GPS brut
l = ['$GPGGA,064036.289,4836.5375,N,00740.9373,E,1,04,3.2,200.2,M,,,,0000*0E','$GPVTG,054.7,T,034.4,M,005.5,N,010.2,K','$GPGSA,A,3,04,05,,09,12,,,24,,,,,2.5,1.3,2.1*39','$GPRMB,A,0.66,L,003,004,4917.24,N,12309.57,W,001.3,052.5,000.5,V*20','$HCHDG,125.5,,,,*41','$GPRMC,053740.000,A,2503.6319,N,12136.0099,E,2.69,79.65,100106,,,A*69','$GPGGA,094636.289,4836.54575,N,00740.0373,E,1,08,3.2,500.2,M,,,,0000*0E','$GPVTG,054.7,T,034.4,M,005.5,N,100.2,K','$GPGSA,A,3,04,05,,09,12,,,24,,,,,2.5,1.3,2.1*39','$GPRMB,A,0.66,L,003,004,4917.24,N,12309.57,W,001.3,052.5,000.5,V*20','$HCHDG,125.5,,,,*41','$GPRMC,053740.000,A,2503.6319,N,12136.0099,E,2.69,79.65,100106,,,A*69']

CL = []
for i in l:
	CL.append(i.split(","))


#Recupérer les données qui nous intéressent

Vitesse = []
Latitude = []
Longitude = []
Date = []
Altitude = []
NbrSatellite = []

for i in range(len(l)):
	if CL[i][0] == "$GPVTG":
		Vitesse.append(CL[i][7])

	elif CL[i][0] == "$GPGGA":
		Latitude.append(CL[i][2])
		Longitude.append(CL[i][4])
		Date.append(datetime.datetime.now().strftime("%Y%m%d")+CL[i][1])
		Altitude.append(CL[i][9])
		NbrSatellite.append(CL[i][7])

#Ordre des données stoqué // Sauvegarde de ces données
"""
Donne = [[Vitesse, Latitude, Longitude, Date, Altitude, NbrSatellite],[Vitesse, Latitude, Longitude, Date, Altitude, NbrStallite]]
Date = Année   Mois   Jour   Heure   Minute   Seconde
Vitesse en Km/H
Latitude : N
Longitude : E
Altitude : m
"""

Donne = []
for i in range(len(Vitesse)):
	Donne.append([Vitesse[i],Latitude[i],Longitude[i],Date[i],Altitude[i],NbrSatellite[i]])

print(Donne)
