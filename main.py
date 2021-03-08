weather_data =[]

f= open("madrid.csv","r")
data = f.read()
rows = data.split("\n")
for row in rows:
    split_row =row.split(",")
    weather_data.append(split_row)

    count=0

    for item in weather_data:
        count= count + 1

#enlever l'entete
new_weather = weather_data[1:366]

#verifier la presence d'un element dqns une liste en une ligne
animals = ["chien","lion","girafe"]

for animal in animals:
  if animal == "chien":
    print("Oui")

#encore mieux ici:

if "chien" in animals:
  print("ENCORRRE MIEUUUUXXX")


weather = []

for row in new_weather:
  weather.append(row[1])

print(weather[0:5])

weather_type =["Pluie","Soleil","Nuage","Nuage-Pluie","Orage","Climat"]
weather_type_found = []

# voici une boucle qui verify la presence d'un element dans une liste et retourne vrai ou faux.

for item in weather_type:
  found = item in weather
  weather_type_found.append(found)

print(weather_type_found)

