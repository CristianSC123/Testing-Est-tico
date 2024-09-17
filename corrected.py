"""
Este módulo gestiona la lógica de un sistema de productos y usuarios.
Contiene clases para manejar inventarios y compras, así como funciones para gestionar usuarios y productos.
"""

class Producto:
    """
    Esta clase representa un producto en el inventario con su nombre, precio, categoría y stock.
    """
    def __init__(self, nombre, precio, categoria):
        """
        Inicializa un nuevo producto con su nombre, precio y categoría.
        El stock comienza en 0.
        """
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = 0
    
    def anadir_stock(self, cantidad):
        """
        Añade una cantidad al stock del producto.
        """
        self.stock += cantidad  # Corrección del operador
    
    def aplicar_descuento(self, descuento):
        """
        Aplica un descuento al precio del producto. El descuento es un porcentaje.
        """
        self.precio = self.precio - (self.precio * descuento / 100)
    
    def cambiar_precio(self, nuevo_precio):
        """
        Cambia el precio del producto si el nuevo precio es mayor que 0.
        """
        if nuevo_precio > 0:
            self.precio = nuevo_precio  # Corrección del operador
    
    def detalles_producto(self):
        """
        Muestra los detalles del producto.
        """
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Categoría:", self.categoria)
        print("Stock:", self.stock)


class Usuario:
    """
    Esta clase representa un usuario que puede realizar compras.
    """
    def __init__(self, nombre, email):
        """
        Inicializa un usuario con su nombre y correo electrónico.
        El historial de compras comienza vacío.
        """
        self.nombre = nombre
        self.email = email
        self.compras = []
    
    def agregar_compra(self, producto):
        """
        Añade un producto al historial de compras del usuario.
        """
        self.compras.append(producto)
    
    def imprimir_historial_compras(self):
        """
        Imprime el historial de compras del usuario.
        Si no tiene compras, lo indica.
        """
        if len(self.compras) == 0:
            print("No se ha registrado ninguna compra.")
        else:
            print(f"Historial de compras de {self.nombre}:")
            for producto in self.compras:
                print(f"Producto: {producto.nombre}, Precio: {producto.precio}")
        print()
    
    def cambiar_email(self, nuevo_email):
        """
        Cambia el email del usuario.
        """
        self.email = nuevo_email  # Corrección del operador


def imprimir_inventario(lista_productos):
    """
    Imprime los detalles de todos los productos en la lista de productos.
    """
    for producto in lista_productos:
        producto.detalles_producto()

def buscar_producto(nombre_producto, lista_productos):
    """
    Busca un producto en la lista de productos por su nombre.
    Si lo encuentra, lo retorna, de lo contrario retorna None.
    """
    for producto in lista_productos:
        if producto.nombre == nombre_producto:
            return producto
    return None

def gestionar_usuarios_y_productos():
    """
    Función principal para gestionar usuarios y productos.
    Añade stock, imprime el inventario, gestiona compras y cambios de precio.
    """
    producto1 = Producto("Camisa", 20, "Ropa")
    producto2 = Producto("Pantalones", 30, "Ropa")
    producto3 = Producto("Zapatos", 50, "Calzado")

    productos = [producto1, producto2, producto3]

    usuario1 = Usuario("Ana Pérez", "ana.perez@example.com")
    usuario2 = Usuario("Luis Gómez", "luis.gomez@example.com")
    
    producto1.anadir_stock(10)
    producto2.anadir_stock(5)
    producto3.anadir_stock(7)
    
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
