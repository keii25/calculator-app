# Calcular porcentajes

class Calculadora:
    def __init__(self):
        self.total:int
        self.num_personas:int
        
    def entrada_datos(self):
        self.total = int(input("Digite total de Comida: "))
        self.num_personas = int(input("Num Personas: "))   
    
            
    def porcentaje_calcular(self,porcentaje):     
        result = (self.total * porcentaje) / self.num_personas
        round(result)
        print(f"Propina: Total a pagar {round(result)} por persona")
        
        

        
        
        
        
    
    