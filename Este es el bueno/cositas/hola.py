class Coche:
    def __init__(self, **kargs):
        self.marca = kargs["marca"]
        self.precio = kargs["precio"]

    def info(self):
        print(self.marca, self.precio)


class Tesla(Coche):
    def __init__(self, **kargs):
        super().__init__(marca="tesla", precio=kargs["precio"])
        self.autonomia = kargs["autonomia"]

    def info(self):
        super().info()
        print(self.autonomia)


def construir():
    c = Coche(marca="honda", precio=23000)

    model300 = Tesla(precio=32222, autonomia=234)
    c.info()
    model300.info()



if __name__ == "__main__":
    construir()
