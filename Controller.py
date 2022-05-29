import mysql.connector
from Persona import Persona

class Conexion():

    def __init__(self, usuario:str, contra:str):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user=usuario,
            password=contra,
            database="escuela"
            )
        self.cursor = self.mydb.cursor()

    def _showContents(self):
        print("--------------------------")
        for i in self.cursor:
            print(i)
        print("--------------------------\n")
    
    def insertPersona(self, p:Persona):
        """
        Anexa a una persona a la tabla personas. Recibe un objeto persona.
        """
        command = f"INSERT IGNORE INTO personas (matricula, nombre, departamento, tipo) VALUES ({p.matricula}, '{p.nombre}', '{p.departamento}', '{p.tipo}')"
        self.cursor.execute(command)
        self.mydb.commit()

    def buscarMatricula(self, matricula:int):
        """
        Busca a alguien por matricula dentro de la tabla personas.
        """

        self.cursor.execute(f"SELECT * FROM personas WHERE matricula = {matricula};")
        self._showContents()
    
    def buscarDepartamento(self, departamento:str):
        """
        Busca a alguien por departamento en la tabla personas.
        """
        self.cursor.execute(f"SELECT * FROM personas WHERE departamento = '{departamento}';")
        self._showContents()
    
    def buscarTipo(self, tipo:str):
        """
        Filtra y lista a los usuarios del tipo seleccionado dentro del estacionamiento.
        """
        self.cursor.execute(f"SELECT * FROM personas WHERE tipo = '{tipo}';")
        self._showContents()
    
    def close(self):
        self.cursor.close()
        self.mydb.close()
    