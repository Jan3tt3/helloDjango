class Computadora:
    def __init__(self, marca, ram):
        self.marca=marca
        self.ram=ram
    
    def descripcion(self):
        return f"Computadora {self.marca} con {self.ram}"

class SistemaOperativo:
    def __init__(self, nombre, version):
        self.nombre=nombre
        self.version=version
    
    def info(self):
        return f"{self.nombre} versión {self.version}"