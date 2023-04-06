nombre = input("¿Cómo te llamas? ")
ventas = int(input("¿Cuántas ventas has realizado este mes? "))

comisiones = ventas*13/100

print(f"De acuerdo, {nombre} este mes te correponde {round(comisiones,2)}€ de comisiones")