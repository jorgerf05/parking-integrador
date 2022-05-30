class Persona():
    def __init__(self, tipo: str, nombre: str, edificio: str, matricula="n/a" ):
        self.tipo = tipo
        self.nombre = nombre
        self.edificio = edificio
        self.matricula = matricula
    
    def __str__(self) -> str:
        return (f"---\nTipo: {self.tipo}\nNombre: {self.nombre}\nEdificio: {self.edificio}\nMatricula: {self.matricula}\n---")