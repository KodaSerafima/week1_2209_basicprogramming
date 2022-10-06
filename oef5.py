dagen = float (input("geef het aantal dagen:"))
uren = float (input("geef het aantal uren:"))
minuten = float (input("geef het aantal minuten op:"))
seconden = float (input("geef het aantal seconden op:"))

totaal = seconden + (minuten*60) + (uren*60*60) + (dagen*60*60*24)
print (f"het aantal seconden zijn {totaal}")