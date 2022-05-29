import mysql.connector

class Conexion():

    def __init__(self, usuario, contra):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=usuario,
            password=contra,
            database="escuela"
            )
        self.cursor = self.mydb.cursor()

    def execute(self, cmd, args=0):
        self.cursor.execute(cmd)

    def showContents(self):
        for i in self.cursor:
            print(i)
    
    def insert(self, cmd, args):
        self.cursor.execute(cmd, args)
        self.mydb.commit()

class Persona():
    def __init__(self, tipo: str, nombre: str, departamento: str, matricula="n/a" ):
        self.tipo = tipo
        self.nombre = nombre
        self.departamento = departamento
        self.matricula = matricula
    
    def __str__(self) -> str:
        return (f"---\nTipo: {self.tipo}\nNombre: {self.nombre}\nDepartamento: {self.departamento}\nMatricula: {self.matricula}\n---")
        