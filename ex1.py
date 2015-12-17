"""El programa comproba si un numero es divisible per 2 o per 3"""
PARELL = int(input("Introdueix un numero:"))
if PARELL % 2 == 0:
    print("El numero es divisible per 2")
elif PARELL % 3 == 0:
    print("El numero es divisible per 3")
else:
    print("El numero no es divisible per 2 ni per 3")

