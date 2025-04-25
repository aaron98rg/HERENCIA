"""Se plantea desarrollar un programa que permita la gestión de una empresa agroalimentaria que trabaja con tres tipos de productos:
•	Productos frescos
•	Productos refrigerados
•	Productos congelados 

Todos los productos llevan esta información común: fecha de caducidad y número de lote. A su vez, cada tipo de producto lleva alguna información específica.

•	Los productos frescos deben llevar la fecha de envasado y el país de origen.
•	Los productos refrigerados deben llevar el código del organismo de supervisión alimentaria.
•	Los productos congelados deben llevar la temperatura de congelación recomendada.
Realiza un menú que pregunte qué tipo de producto se quiere crear y guárdalos en listas independientes para cada tipo."""

class Productos:
    def __init__(self, nombre, fecha_caducidad, numero_lote, peso, medidas):
        self.fecha_caducidad = fecha_caducidad
        self.numero_lote = numero_lote
        self.nombre = nombre
        self.peso = peso 
        self.medidas = medidas
    
    def calcular_coste_envio(self):
        precio = self.peso * 3
        return precio

    def __str__(self):
        return f"Nombre: {self.nombre}, Fecha caducidad: {self.fecha_caducidad}, Numero de lote: {self.numero_lote}, Peso: {self.peso}, Medidas: {self.medidas}"


class Frescos(Productos):
    def __init__(self, nombre, fecha_caducidad, numero_lote, fecha_envasado, pais_origen, peso, medidas):
        super().__init__(nombre, fecha_caducidad, numero_lote, peso, medidas)
        self.fecha_envasado = fecha_envasado
        self.pais_origen = pais_origen

    def __str__(self):
        return super().__str__() + f", Fecha de envasado: {self.fecha_envasado}, Pais: {self.pais_origen}"


class Refrigerados(Productos):
    def __init__(self, nombre, fecha_caducidad, numero_lote, codigo_organismo, peso, medidas):
        super().__init__(nombre, fecha_caducidad, numero_lote, peso, medidas)
        self.codigo_organismo = codigo_organismo

    def calcular_coste_envio(self):
        precio = super().calcular_coste_envio() + 2
        return precio

    def __str__(self):
        return super().__str__() + f", Codigo Organismo: {self.codigo_organismo}"


class Congelados(Productos):
    def __init__(self, nombre, fecha_caducidad, numero_lote, temperatura_recomendada, peso, medidas):
        super().__init__(nombre, fecha_caducidad, numero_lote, peso, medidas)
        self.temperatura_recomendada = temperatura_recomendada

    def calcular_coste_envio(self):
        precio = super().calcular_coste_envio() + 5
        return precio

    def __str__(self):
        return super().__str__() + f", Temperatura recomendada: {self.temperatura_recomendada}"


class Almacen:
    def __init__(self, lista_frescos, lista_refrigerados, lista_congelados, lista_productos):
        self.lista_frescos = lista_frescos
        self.lista_refrigerados = lista_refrigerados
        self.lista_congelados = lista_congelados
        self.lista_productos = lista_productos

    def agregar_producto(self, lista, producto):
        lista.append(producto)

    def mostrar_productos(self, lista):
        for i, producto in enumerate(lista):
            print(f"{i}: {producto}")

    def eliminar_producto(self, lista, indice):
        if 0 <= indice < len(lista):
            lista.pop(indice)
        else:
            print("Índice no válido.")


def datos_comunes():
    nombre = input("Nombre del producto: ")
    fecha_caducidad = input("Fecha de caducidad: ")
    numero_lote = input("Número de lote: ")
    peso = int(input("Peso: "))
    medidas = input("Medidas: ")
    return nombre, fecha_caducidad, numero_lote, peso, medidas


def main():
    almacen = Almacen(lista_frescos=[], lista_congelados=[], lista_refrigerados=[], lista_productos=[])

    while True:
        print("\nMenú de gestión de productos:")
        print("1. Agregar producto fresco")
        print("2. Agregar producto refrigerado")
        print("3. Agregar producto congelado")
        print("4. Mostrar productos frescos")
        print("5. Mostrar productos refrigerados")
        print("6. Mostrar productos congelados")
        print("7. Eliminar producto")
        print("8. Calcular precio")
        print("9. Salir")

        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                nombre, fecha_caducidad, numero_lote, peso, medidas = datos_comunes()
                fecha_envasado = input("Fecha de envasado: ")
                pais_origen = input("País de origen: ")
                producto = Frescos(nombre, fecha_caducidad, numero_lote, fecha_envasado, pais_origen, peso, medidas)
                almacen.agregar_producto(almacen.lista_frescos, producto)
                almacen.agregar_producto(almacen.lista_productos, producto)
                print("Producto fresco agregado.")

            case 2:
                nombre, fecha_caducidad, numero_lote, peso, medidas = datos_comunes()
                codigo_organismo = input("Código del organismo de supervisión alimentaria: ")
                producto = Refrigerados(nombre, fecha_caducidad, numero_lote, codigo_organismo, peso, medidas)
                almacen.agregar_producto(almacen.lista_refrigerados, producto)
                almacen.agregar_producto(almacen.lista_productos, producto)
                print("Producto refrigerado agregado.")

            case 3:
                nombre, fecha_caducidad, numero_lote, peso, medidas = datos_comunes()
                temperatura_recomendada = input("Temperatura de congelación recomendada: ")
                producto = Congelados(nombre, fecha_caducidad, numero_lote, temperatura_recomendada, peso, medidas)
                almacen.agregar_producto(almacen.lista_congelados, producto)
                almacen.agregar_producto(almacen.lista_productos, producto)
                print("Producto congelado agregado.")

            case 4:
                almacen.mostrar_productos(almacen.lista_frescos)

            case 5:
                almacen.mostrar_productos(almacen.lista_refrigerados)

            case 6:
                almacen.mostrar_productos(almacen.lista_congelados)

            case 7:
                print(almacen.lista_productos)
                indice = int(input("Seleccione el índice del producto a eliminar: "))
                almacen.eliminar_producto(almacen.lista_productos, indice)
                print("Producto eliminado.")

            case 8:
                print(almacen.lista_productos)
                indice = int(input("Seleccione el índice del producto para obtener su precio: "))
                if 0 <= indice < len(almacen.lista_productos):
                    producto = almacen.lista_productos[indice]
                    print(f"El coste de envío del producto es: {producto.calcular_coste_envio()}")
                else:
                    print("Índice no válido.")

            case 9:
                print("Saliendo del programa.")
                break

            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 9.")


main()