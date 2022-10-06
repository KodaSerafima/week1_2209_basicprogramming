seconden = int (input("aantal seconden:"))


dagen = seconden // (seconden*60*60 * 24)
rest = seconden % (seconden*60*60 * 24)

uren = rest // (60*60)
rest = rest % (60*60)

minuten = rest // (60*60)
rest = rest % 60

seconden = rest 
print (f"d:h:m:s -> {dagen}:{uren}:{minuten}:{seconden}")