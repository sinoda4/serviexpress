from taller.models import Producto

class Carrito():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('session_key')

        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart

    def add(self, producto):
        producto_id = str(producto.pk)

        if producto_id in self.cart:
            pass
        else:
            self.cart[producto_id] = {'precio': str(producto.precio)}

        self.session.modified = True

    def __len__(self):
        return len(self.cart)
    
    def get_productos(self):
        #Obtienes los id del carrito
        productos_ids = self.cart.keys()
        #Mirar los productos con la base de datos
        productos = Producto.objects.filter(id_producto__in=productos_ids)

        #retornar
        return productos