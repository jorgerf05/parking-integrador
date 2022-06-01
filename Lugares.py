from tokenize import Octnumber


class Lugar():
    def __init__(self, id:int, ocupante:int , entrada:str, estado:int):
        self.id = id
        self.ocupante = ocupante
        self.entrada = entrada
        self.estado = estado
    def __str__(self) -> str:
        return (f"ID: {self.id}, Ocupante: {self.ocupante}, Entrada: {self.entrada}, Estado: {self.estado}")