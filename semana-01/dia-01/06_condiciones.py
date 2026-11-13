# Condicionales
# if, else , elif

#[Regla de oro]: la identacion y el orden

#edad = 19

#if edad >= 18:
#    print("Eres matoy de edad")
#    print("!Felicidades!")
    
    
# una persona quiere postular a la presidencia del Perpu
# requisito, debe de contar con mas de 35 años

nombre = input("Escriba su nombre: ")
edad = int(input("¿Cuál es su edad?: "))

# Requisito: debe contar con más de 35 años
if edad > 35:
    print(f"Sr. {nombre}, usted es apto para postularse como presidente")
else:
    print(f"Sr. {nombre}, usted no es apto para postularse como presidente")