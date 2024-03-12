import sys

def convertir_pesos_chilenos(tasas, cantidad):
  
    soles = cantidad * tasas[0]
    pesos_argentinos = cantidad * tasas[1]
    dolares = cantidad * tasas[2]
    
    return soles, pesos_argentinos, dolares

if __name__ == "__main__":
    
    if len(sys.argv) != 5:  
        print("Uso: python conversiones.py tasa_sol tasa_peso_arg tasa_dolar cantidad_pesos")
    else:
        tasas = [float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])]
        cantidad_pesos = float(sys.argv[4])

        
        soles, pesos_argentinos, dolares = convertir_pesos_chilenos(tasas, cantidad_pesos)

        
        print(f"Los {cantidad_pesos} pesos equivalen a:")
        print(f"{soles} Soles")
        print(f"{pesos_argentinos} Pesos Argentinos")
        print(f"{dolares} Dólares")






