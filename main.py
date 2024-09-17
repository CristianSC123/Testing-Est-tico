class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = 0
    
    def añadir_stock(self, cantidad):
        self.stock =+ cantidad  # 

    def aplicar_descuento(self, descuento):
        self.precio = self.precio - (self.precio * descuento / 100)
    
    def cambiar_precio(self, nuevo_precio):
        if nuevo_precio > 0:
            self.precio == nuevo_precio  #
    
    def detalles_producto(self):
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Categoría:", self.categoria)
        print("Stock:", self.stock)


class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
        self.compras = []
    
    def agregar_compra(self, producto):
        self.compras.append(producto)
    
    def imprimir_historial_compras(self):
        if len(self.compras) == 0:
            print("No se ha registrado ninguna compra.")
        else:
            print(f"Historial de compras de {self.nombre}:")
            for producto in self.compras:
                print(f"Producto: {producto.nombre}, Precio: {producto.precio}")
        print()
    
    def cambiar_email(self, nuevo_email):
        self.email == nuevo_email


def imprimir_inventario(lista_productos):
    for producto in lista_productos:
        producto.detalles_producto()

def buscar_producto(nombre_producto, lista_productos):
    for producto in lista_productos:
        if producto.nombre == nombre_producto:
            return producto
    return None

def gestionar_usuarios_y_productos():
    producto1 = Producto("Camisa", 20, "Ropa")
    producto2 = Producto("Pantalones", 30, "Ropa")
    producto3 = Producto("Zapatos", 50, "Calzado")

    productos = [producto1, producto2, producto3]

    usuario1 = Usuario("Ana Pérez", "ana.perez@example.com")
    usuario2 = Usuario("Luis Gómez", "luis.gomez@example.com")
    
    producto1.añadir_stock(10)
    producto2.añadir_stock(5)
    producto3.añadir_stock(7)
    
    imprimir_inventario(productos)
    

    usuario1.agregar_compra(producto1)
    usuario1.agregar_compra(producto3)
    usuario2.agregar_compra(producto2)
    
    usuario1.imprimir_historial_compras()
    usuario2.imprimir_historial_compras()

    producto1.cambiar_precio(25)
    producto1.detalles_producto()

    prod_busqueda = buscar_producto("Sombrero", productos)
    if prod_busqueda is None:
        print("Producto no encontrado")
    else:
        prod_busqueda.detalles_producto()

    usuario1.cambiar_email("ana.nuevo@example.com")


gestionar_usuarios_y_productos()
