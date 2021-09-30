# Application Calculadora de Propinas

from typing import Dict
from calcular import Calculadora


print("\n")
print("Calculadora de Propinas")
print("\n")

menu_selection: Dict[str, str] = {
    "1": "7% - Bueno",
    "2": "8% - Muy Bueno",
    "3": "10% - Excelente"    
}
    
datos = Calculadora()
    
def use_menu(opt: str):
    
    if opt == "1":
        datos.entrada_datos()
        datos.porcentaje_calcular(0.07)
        
    elif opt == "2":
        datos.entrada_datos()
        datos.porcentaje_calcular(0.08)
        
    elif opt == "3":
        datos.entrada_datos()
        datos.porcentaje_calcular(0.10)
    else:
        print("Opcion Invalida")
        print("Ejecucion Finalizada")
        

menu = menu_selection.items()
for option, valor in menu:
    print(option, ": ", valor)

print("\n")

opt = input("Digite una Opcion: ")
print("\n")   
use_menu(opt)