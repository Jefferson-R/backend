
# Muestres los morosos

for cliente in clientes:
    if cliente["deuda"] > 0:
        print(f"MOROSOS: {cliente["nombre"]}")

for cliente in clientes:
    if cliente["deuda"] > 100 and cliente["dias_atraso"] > 30:
        print(f"LOS MOROSOS GRAVES {cliente["nombre"]}  DIAS DE ATRASO: {cliente["dias_atraso"]}")
        
cliente_mayor = [0]
for cliente in clientes:
    if cliente["deuda"] > cliente_mayor["deuda"]:
        cliente_mayor = cliente

print(f"CLIENTE CON MAYOR DEUDA: {cliente_mayor["deuda"]}")      

cliente_sin_deuda = clientes[0]

for cliente in clientes:
    if clientes["deuda"] == 0:
        cliente_sin_deuda.append(cliente["nombre"])
print(cliente_sin_deuda)


# Imprimir deuda acumulada
deuda_acumulada = 0
for cliente in clientes:
    deuda_acumulada = deuda_acumulada + cliente["deuda"]
print(f"TOTAL DE DEUDA ACUMULADA {deuda_acumulada/len(cliente)}")    
    


# --------------------------

# INTERBANK
# El siguiente usuario esta teniendo los siguientes movimientos
movimientos = [
    { "fecha": "2024-01-15", "tipo": "deposito", "monto": 1500.00},
    { "fecha": "2024-01-20", "tipo": "retiro", "monto": 200.00},
    { "fecha": "2024-02-05", "tipo": "deposito", "monto": 500.00},
    { "fecha": "2024-02-10", "tipo": "retiro", "monto": 100.00},
    { "fecha": "2024-02-15", "tipo": "deposito", "monto": 300.00},
    { "fecha": "2024-02-20", "tipo": "retiro", "monto": 50.00},
    { "fecha": "2024-02-25", "tipo": "deposito", "monto": 1000.00 }
]


# 01. Sumar todos los depositos


     
# 02. Sumar todos los retiros



# 03. Calcular el balance final (depositos - retiros)

# 04. Mostrar el deposito mas grande
# 05. Mostrar el retiro mas grande


depositos = []
retiros = []

for movimiento in movimientos:
    if movimiento["tipo"] == "deposito":
        depositos.append(movimiento["monto"])
    else:
        retiros.append(movimiento["monto"])

print(f"La suma de los depositos {sum(depositos)}")
print(f"La suma de los retiros {sum(retiros)}")
print(f"El saldo es {sum(depositos) - sum(retiros)}")
print(f"El deposito mas grande {max(depositos)}")
print(f"El retiro mas grande {max(retiros)}")