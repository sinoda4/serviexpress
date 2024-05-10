from .carrito import Carrito

def cart(request):
    return {'carrito': Carrito(request)}