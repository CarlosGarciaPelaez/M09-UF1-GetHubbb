"""Aquest ordena dos numeros"""
PRIMER = int(input("Introdueix el primer valor"))
SEGON = int(input("Intrpdueix el segon valor"))

if PRIMER > SEGON:
    print("El numero mes gran es", PRIMER)
else:
    if PRIMER < SEGON:
        print("El numero mes gran es", SEGON)
