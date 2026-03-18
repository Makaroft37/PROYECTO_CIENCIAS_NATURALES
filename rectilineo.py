print("=== Verificador de Movimiento Rectilíneo Uniforme (MRU) ===\n")

velocidad_inicial = float(input("Ingrese la velocidad inicial (m/s): "))
velocidad_final = float(input("Ingrese la velocidad final (m/s): "))
aceleracion = float(input("Ingrese la aceleración (m/s^2): "))
if velocidad_inicial == velocidad_final and aceleracion == 0:
    print("\nEl movimiento ES Rectilíneo Uniforme (MRU).")
else:
    print("\nEl movimiento NO es Rectilíneo Uniforme (MRU).")

print("=== Verificador de Movimiento Rectilíneo Uniformemente Acelerado (MRUA) ===\n")
velocidad_inicial = float(input("Ingrese la velocidad inicial (m/s): "))
velocidad_final = float(input("Ingrese la velocidad final (m/s): "))
aceleracion = float(input("Ingrese la aceleración (m/s^2): "))

if aceleracion != 0 and velocidad_inicial != velocidad_final:
    print("\nEl movimiento ES Rectilíneo Uniformemente Acelerado (MRUA).")
else:
    print("\nEl movimiento NO es Rectilíneo Uniformemente Acelerado (MRUA).")