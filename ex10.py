"""Aquest programa no hace anada"""
PRIMER = int(input("Introdueix un valor"))
SEGON = int(input("Introdueix un altre valor"))

if SEGON > PRIMER:
    AUXILIAR = PRIMER
    PRIMER = SEGON
    SEGON = AUXILIAR

if PRIMER % SEGON == 0:
    print("El nombre", SEGON, "es multiple de", PRIMER)
else:
    print("El nombre", SEGON, "NO es multiple de", PRIMER)
