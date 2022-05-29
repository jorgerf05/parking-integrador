class Persona():
    def __init__(self, tipo: str, nombre: str, departamento: str, matricula="n/a" ):
        self.tipo = tipo
        self.nombre = nombre
        self.departamento = departamento
        self.matricula = matricula
    
    def __str__(self) -> str:
        return (f"---\nTipo: {self.tipo}\nNombre: {self.nombre}\nDepartamento: {self.departamento}\nMatricula: {self.matricula}\n---")