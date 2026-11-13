class Auto:
    def __init__(self, nroLlantas, color, tipo, marca , soat):
        self.nroLlantas = nroLlantas
        self.color = color
        self.tipo = tipo
        self.marca = marca
        self.soat = soat
        
mercedes =  Auto("4", "negro", "antiguo", "mercedes" , "Pacifico")

print(f"El carro  tiene {mercedes.nroLlantas} es color {mercedes.color}, marca {mercedes.marca}, tiene seguro{mercedes.soat}")