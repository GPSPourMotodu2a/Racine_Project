import serial
import time
import datetime

def GPS():
	debut = time.time()
	#Récupération des données du GPS
	def lireInfosGPS():
		try:
			with serial.Serial("/dev/ttyACM0") as ser:
				l = [str(ser.readline())[2:-5] for i in range(11)]
			return [el for el in l if not el.startswith("$GPTXT")]
		except:
			print("Puce GPS non connecté ou Droit d'éxécution insuffisant")
			return []
	l = lireInfosGPS()
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

	#Vérification du nombre de Satellite

	v = 0
	for i in range(len(Vitesse)):
		donnee = int(Donne[i-v][5])
		if donnee <= 3:
			Donne.remove(Donne[i-v])
			v = v+1

	if Donne == []:
		result = "Aucune donné valide"
	else:
		result = Donne

	print(time.time()-debut)
	return result

print(GPS())
