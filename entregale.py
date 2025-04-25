class Productos:
    def __init__(self, nombre, fecha_caducidad, numero_lote):
        self.fecha_caducidad = fecha_caducidad
        self.numero_lote = numero_lote
        self.nombre = nombre

    def agregar_producto(self, lista):
        lista.append(self)


class Alamcen:
    def __init__(self,lista_frescos = [], lista_refigerados = [], lista_congelados = []):
        self.lista_frescos = lista_frescos
        self.lista_refrigerados = lista_refigerados
        self.lista_congelados = lista_congelados

    def mostrar_productos(self, lista):
        for producto in lista:
            print(producto)
    def __str__(self):
        return f"Nombre: {self.nombre}, Fecha de caducidad: {self.fecha_caducidad}, Número de lote: {self.numero_lote}"

class Frescos(Productos):
    def __init__(self, nombre, fecha_caducidad, numero_lote, fecha_envasado, pais_origen):
        super().__init__(nombre, fecha_caducidad, numero_lote)
        self.fecha_envasado = fecha_envasado
        self.pais_origen = pais_origen

    def __str__(self):
        return super().__str__() + f", Fecha de envasado: {self.fecha_envasado}, País de origen: {self.pais_origen}"

class Refrigerados(Productos):
    def __init__(self, nombre, fecha_caducidad, numero_lote, codigo_organismo):
        super().__init__(nombre, fecha_caducidad, numero_lote)
        self.codigo_organismo = codigo_organismo

    def __str__(self):
        return super().__str__() + f", Código del organismo: {self.codigo_organismo}"

class Congelados(Productos):
    def __init__(self, nombre, fecha_caducidad, numero_lote, temperatura_recomendada):
        super().__init__(nombre, fecha_caducidad, numero_lote)
        self.temperatura_recomendada = temperatura_recomendada

    def __str__(self):
        return super().__str__() + f", Temperatura recomendada: {self.temperatura_recomendada}"

def solicitar_datos_comunes():
    nombre = input("Nombre del producto: ")
    fecha_caducidad = input("Fecha de caducidad: ")
    numero_lote = input("Número de lote: ")
    return nombre, fecha_caducidad, numero_lote

def main():
    almacen = Alamcen(lista_frescos=[], lista_congelados= [], lista_refigerados= [])

    while True:
        print("\nMenú de gestión de productos:")
        print("1. Agregar producto fresco")
        print("2. Agregar producto refrigerado")
        print("3. Agregar producto congelado")
        print("4. Mostrar productos frescos")
        print("5. Mostrar productos refrigerados")
        print("6. Mostrar productos congelados")
        print("7. Salir")

        opcion = int(input("Seleccione una opción: "))

        match opcion:
            case 1:
                nombre, fecha_caducidad, numero_lote = solicitar_datos_comunes()
                fecha_envasado = input("Fecha de envasado: ")
                pais_origen = input("País de origen: ")
                producto = Frescos(nombre, fecha_caducidad, numero_lote, fecha_envasado, pais_origen)
                producto.agregar_producto(almacen.lista_frescos)
                print("Producto fresco agregado.")

            case 2:
                nombre, fecha_caducidad, numero_lote = solicitar_datos_comunes()
                codigo_organismo = input("Código del organismo de supervisión alimentaria: ")
                producto = Refrigerados(nombre, fecha_caducidad, numero_lote, codigo_organismo)
                producto.agregar_producto(almacen.lista_refrigerados)
                print("Producto refrigerado agregado.")

            case 3:
                nombre, fecha_caducidad, numero_lote = solicitar_datos_comunes()
                temperatura_recomendada = input("Temperatura de congelación recomendada: ")
                producto = Congelados(nombre, fecha_caducidad, numero_lote, temperatura_recomendada)
                producto.agregar_producto(almacen.lista_congelados)
                print("Producto congelado agregado.")

            case 4:
               producto.mostrar_productos(almacen.lista_frescos)


            case 5:
                producto.mostrar_productos(almacen.lista_refrigerados)

            case 6:
                producto.mostrar_productos(almacen.lista_congelados)

            case 7:
                print("Saliendo del programa.")
                break

            case _:
                print("Opción no válida. Por favor, seleccione una opción del 1 al 7.")
main()