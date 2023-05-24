
class Cart():

    def __init__(self, request) -> None:
        self.session = request.session
        if 'key' not in request.session:
            cart = self.session['key'] = {'booboo': 456789}
        else:
            cart = self.session.get('key')
        self.cart = cart
