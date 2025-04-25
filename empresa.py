"""Crea un sistema de videojuegos con una clase base Videojuego, que tendrá los siguientes atributos:
título: nombre del juego.
empresa: empresa que lo creó.
precio: precio del videojuego.
Dentro de los videojuegos tenemos dos tipos, los de plataformas, como Super Mario Bros y los de mundo abierto como el Fortnite.  
Los de plataformas se caracterizan por el número de niveles que puede tener el juego y por el tipo de movimiento de sus personajes, que puede ser 2D o 3D.
Los de mundo abierto tienen un máximo de km de mapa explorable. 

Ambas clases deben sobrescribir el método __str__() para mostrar su información específica.
A la hora de vender un videojuego se le puede aplicar un descuento, implementa un método que calcule el precio final.
Para los videojuegos de plataformas debemos implementar un método que realice el avance de nivel del jugador e imprima un mensaje por pantalla informando de este logro. Controla si se ha llegado al último nivel.
En el caso de los videojuegos de mundo abierto se permite explorar el mapa y se controla cuántos km se llevan explorados.

Crea un menú principal en el que el usuario pueda simular algunas operaciones antes de decidirse por un juego, para ello:
-Crea dos juegos de cada tipo y añádelos a listas diferentes
-Pregunta al usuario qué juego quiere probar, para ello imprime la información de las dos listas, de forma numerada.
-Dependiendo del juego que haya seleccionado ofrécele subir de nivel o explorar algunos kilómetros de mapa.
-Por último pregúntale si quiere saber el precio final del juego, para ello aplícale un 15% y pregúntale si quiere comprarlo.
-Si te dice que sí, borra el juego de la lista"""

class Videojuego():
    def __init__(self, nombre, empresa, precio):
        self.nombre = nombre 
        self.empresa = empresa 
        self.precio = precio 

    def calcular_precio(self, descuento):
        if descuento:
            precio = (precio * descuento) / 100
        return precio

    def __str__(self):
        return f" Nombre: {self.nombre}, Empresa: {self.empresa}, Precio: {self.precio}"
    
class Plataformas(Videojuego):
    def __init__(self, nombre, empresa, precio, totalNiveles, tipoMovimiento):
        super().__init__(nombre, empresa, precio)
        self.totalNiveles = totalNiveles
        self.nivelActual = 0
        self.tipoMovimiento = tipoMovimiento

    
    def avanzar_nivel(self):
        if self.nivelActual < self.totalNiveles:
            self.nivelActual += 1
            print(f"¡Has avanzado al nivel {self.nivel_actual}!")
        else:
            print("¡Felicidades! Has completado el último nivel.")


    def __str__(self):
        return super().__str__() + f"Niveles: {self.niveles}, Tipo de movimiento: {self.tipoMovimiento}"

class MundoAbierto(Videojuego):
    def __init__(self, nombre, empresa, precio,kmMaximos, kmActuales):
        super().__init__(nombre, empresa, precio)
        self.kmMaximos = kmMaximos
        self.kmActuales = kmActuales

    def mostrar_kilometros(self):
        print (f"Kilometros actuales: {self.kmActuales}km de {self.kmMaximos}km totales.")

    def __str__(self):
        return super().__str__() + f" Kilometros maximos: {self.kmMaximos}"

def main():
    juegos = []
    plataformas = []
    mundoAbierto = []

    for i in range(2):
        print("Agrega un juego de plataformas! ")
        juegoPlat = input("Nombre del juego: ")
        plataformas.append(juegoPlat)
        juegos.append(juegoPlat)

    for i in range(2):  
        print("Agrega un juego de mundo abierto! ")
        juegoMA = input("Nombre del juego: ")
        mundoAbierto.append(juegoMA)
        juegos.append(juegoMA)

    print("LISTA DE JUEGOS: ")
    

    for i, juego in enumerate(plataformas):
        print(f"{i + 1}: {juego}")

    for i, juego in enumerate(mundoAbierto):
        print(f"{i + 3}: {juego}")


    
    opcion = int(input("A QUE JUEGO QUIERES JUGAR:"))
    if opcion == 1 or 2:
        opcion.av
main()
