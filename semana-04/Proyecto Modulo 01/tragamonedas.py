
import random


class Tragamonedas:

    simbolos = ["🍒", "🔔", "💎", "🍀", "⭐", "7️⃣"]

    def __init__(self, nombre, creditos):
        self.nombre = nombre

        
        self.__creditos = creditos
        self.__total_apostado = 0
        self.__total_ganado = 0
        
    @property
    def creditos(self):
        return self.__creditos

    def mostrar(self):
        print(f"🎰 {self.nombre} — Créditos: S/ {self.__creditos}")

    def girar(self):
        resultado = []

        for i in range(3):
            simbolo = random.choice(self.simbolos)
            resultado.append(simbolo)

        print(f"[ {'  '.join(resultado)} ]")

        return resultado

    def jugar(self, apuesta):

        if apuesta <= 0:
            print("⚠️ La apuesta debe ser mayor que cero.")
            return

        if apuesta > self.__creditos:
            print(f"❌ No tienes suficientes creditos. Dispones de S/ {self.__creditos}")
            return

        self.__total_apostado += apuesta

        self.__creditos -= apuesta

        resultado = self.girar()

        if resultado[0] == resultado[1] == resultado[2]:

            premio = apuesta * 10

            print(f"🎉 ¡JACKPOT! Ganaste S/ {premio}")

            self.__creditos += premio
            self.__total_ganado += premio

        elif (
            resultado[0] == resultado[1]
            or resultado[1] == resultado[2]
            or resultado[0] == resultado[2]
        ):

            premio = apuesta * 2

            print(f"✨ ¡Dos iguales! Ganaste S/ {premio}")

            self.__creditos += premio
            self.__total_ganado += premio

        else:

            print(f"😢 Perdiste S/ {apuesta}")

        self.mostrar()

    def mostrar_estadisticas(self):

        print(f"\n📊 ESTADISTICAS: {self.nombre}")
        print(f"Total apostado: S/ {self.__total_apostado}")
        print(f"Total ganado: S/ {self.__total_ganado}")
        print(f"Creditos actuales: S/ {self.__creditos}")



# Maquina de frutas
class TragamonedasFrutas(Tragamonedas):

    simbolos = ["🍒", "🍋", "🍊"]


# Maquina clasica
class TragamonedasClasico(Tragamonedas):

    simbolos = ["7️⃣", "💎", "🔔"]


# Maquina personalizada: Mundial 2026
class TragamonedasMundial(Tragamonedas):

    simbolos = ["🇵🇪", "🇦🇷", "🇫🇷", "🇧🇷"]

    # Sobrescritura del metodo jugar()
    def jugar(self, apuesta):

        if apuesta <= 0:
            print("⚠️ La apuesta debe ser mayor que cero.")
            return

        if apuesta > self.creditos:
            print(f"❌ No tienes suficientes creditos. Dispones de S/ {self.creditos}")
            return

        # Ejecutamos la logica de la clase padre
        # El premio normal por tres iguales es x10
        super().jugar(apuesta)



def jugar_maquina(maquina):

    print(f"🎰 Bienvenido a {maquina.nombre}")

    while maquina.creditos > 0:

        maquina.mostrar()

        try:
            apuesta = int(input("¿Cuánto apuestas? (0 para salir): "))

        except ValueError:
            print("⚠️ Ingresa un numero valido.")
            continue

        if apuesta == 0:
            print(f"💰 Saliste con S/ {maquina.creditos}. ¡Vuelve pronto!")
            break

        maquina.jugar(apuesta)

    else:
        print("❌ Te quedaste sin creditos. ¡GAME OVER!")


maquina_frutas = TragamonedasFrutas("La Frutal", 200)

maquina_clasica = TragamonedasClasico("La Clásica", 300)

maquina_mundial = TragamonedasMundial("Mundial 2026", 150)


# Guardamos todas las maquinas en una lista
maquinas = [
    maquina_frutas,
    maquina_clasica,
    maquina_mundial
]



def menu_casino():

    while True:

        print("\n" + "=" * 40)
        print("🎰         CASINO ROYALE         🎰")
        print("=" * 40)

        for i, maquina in enumerate(maquinas, start=1):

            if maquina.creditos > 0:
                print(f"{i}. {maquina.nombre} (S/ {maquina.creditos})")
            else:
                print(f"{i}. {maquina.nombre} (SIN CRÉDITOS)")

        print("4. Mostrar estadisticas de todas")
        print("5. Salir")

        print("=" * 40)

        try:
            opcion = int(input("\nElige una maquina: "))

        except ValueError:
            print("⚠️ Ingresa una opcion valida.")
            continue

        if opcion >= 1 and opcion <= 3:

            maquina_seleccionada = maquinas[opcion - 1]

            if maquina_seleccionada.creditos <= 0:
                print("Esta maquina no tiene creditos.")
            else:
                jugar_maquina(maquina_seleccionada)

        elif opcion == 4:

            print("📊 ESTADISTICAS DE TODAS LAS MAQUINAS")

            for maquina in maquinas:
                maquina.mostrar_estadisticas()

        elif opcion == 5:

            print("\n" + "=" * 40)
            print("💰 RESUMEN GENERAL DEL CASINO")
            print("=" * 40)

            total_apostado = 0
            total_ganado = 0
            total_creditos = 0

            for maquina in maquinas:

                maquina.mostrar_estadisticas()
                total_creditos += maquina.creditos

            print("TOTAL DE CREDITOS RESTANTES:")
            print(f"S/ {total_creditos}")

            print("🎰 ¡Gracias por visitar CASINO ROYALE!")
            print("=" * 40)

            break

        else:
            print("⚠️ Opcion incorrecta. Intenta nuevamente.")


if __name__ == "__main__":
    menu_casino()
