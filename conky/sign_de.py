# Übersetze Sternzeichen ins Deutsche

import fileinput

a = fileinput.input()[0].strip()

s = {"Ari": "♈ Widder",
     "Tau": "♉ Stier",
     "Gem": "♊ Zwillinge",
     "Can": "♋ Krebs",
     "Leo": "♌ Löwe",
     "Vir": "♍ Jungfrau",
     "Lib": "♎ Waage",
     "Sco": "♏ Skorpion",
     "Sag": "♐ Schütze",
     "Cap": "♑ Steinbock",
     "Aqu": "♒ Wassermann",
     "Pis": "♓ Fische",
     }

print("${font DejaVu Sans:size=16:bold}" + s[a][0] + "${font Droid Sans:size=11:bold}" + s[a][1:] + "${font} ")

# Tagesqualitäten:

q = {"Ari": "Feuer,Wärme,Eiweiß/Frucht\nKopf bis Oberkiefer; Sinnesorgane",
     "Tau": "Erde,Kälte,Salz,Wurzel\nUnterkiefer, Halsregion; Kreislauf",
     "Gem": "Luft,Licht,Fett,Blüte\nSchulter, Arme, Hände; Drüsensystem",
     "Can": "Wasser,Feuchte,Kohlenhydrate,Blatt\nBrustbereich, Lunge; Nervensystem",
     "Leo": "Feuer,Wärme,Eiweiß/Frucht\nHerzregion, Kreislauf; Sinnesorgane",
     "Vir": "Erde,Kälte,Salz,Wurzel\nVerdauungsorgane; Kreislauf",
     "Lib": "Luft,Licht,Fett,Blüte\nHüfte, Nieren, Blase; Drüsensystem",
     "Sco": "Wasser,Feuchte,Kohlenhydrate,Blatt\nGeschlechtsorgane; Nervensystem",
     "Sag": "Feuer,Wärme,Eiweiß/Frucht\nOberschenkel, Venen; Sinnesorgane",
     "Cap": "Erde,Kälte,Salz,Wurzel\nKnie, Knochen, Haut; Kreislauf",
     "Aqu": "Luft,Licht,Fett,Blüte\nUnterschenkel, Venen; Drüsensystem",
     "Pis": "Wasser,Feuchte,Kohlenhydrate,Blatt\nFüße, Zehen; Nervensystem",
     }

f = open("/tmp/moon.txt", "w")
f.write(q[a])
f.close()
