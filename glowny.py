from lib.modul1.modulA import funcA
from lib.modul2.modulB import funcB
from lib.modul3.modulC import funcC
from datetime import date
from time import strftime

funcA()
funcB()
funcC()

print("Skrypt wykonany: " + str(date.today()) + " o godzinie " + strftime("%H:%M:%S"))