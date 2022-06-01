import mysql.connector
from Persona import Persona
from datetime import datetime
from Lugares import Lugar

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
        command = f"INSERT IGNORE INTO personas (matricula, nombre, edificio, tipo) VALUES ({p.matricula}, '{p.nombre}', '{p.edificio}', '{p.tipo}')"
        self.cursor.execute(command)
        self.mydb.commit()

    def buscarMatricula(self, matricula:int):
        """
        Busca a alguien por matricula dentro de la tabla personas.
        """

        self.cursor.execute(f"SELECT * FROM personas WHERE matricula = {matricula};")
        self._showContents()
    
    def buscarEdificio(self, edificio:str):
        """
        Busca a alguien por edificio en la tabla personas.
        """
        self.cursor.execute(f"SELECT * FROM personas WHERE edificio = '{edificio}';")
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

    def _setupParking(self):
        self.cursor.execute("INSERT IGNORE INTO lugares (ID, matricula_ocupante, hora_llegada, estado) VALUES (1, NULL, NULL, 0)")
        self.cursor.execute("INSERT IGNORE INTO lugares (ID, matricula_ocupante, hora_llegada, estado) VALUES (2, NULL, NULL, 0)")
        self.cursor.execute("INSERT IGNORE INTO lugares (ID, matricula_ocupante, hora_llegada, estado) VALUES (3, NULL, NULL, 0)")
        self.mydb.commit()

    def ocuparLugar(self, matricula:int, id:int):
        try:
            time = datetime.now()
            timestr = time.strftime("%I:%M:%S")
            self.cursor.execute(f"update lugares set matricula_ocupante = {matricula}, hora_llegada = '{timestr}', estado = 1 where ID = {id};")
            self.mydb.commit()

        except mysql.connector.Error as err:
            print(err)
    
    def liberarLugar(self, id:int):
        try:
            self.cursor.execute(f"update lugares set matricula_ocupante = 0, hora_llegada = 'N/A', estado = 0 where ID ={id};")
            self.mydb.commit()
        
        except mysql.connector.Error as err:
            print(err)

    def leerLugares(self) -> list:
        lugares = []
        self.cursor.execute("select * from lugares")
        for l in self.cursor:
            lugares.append(Lugar(l[0], l[1], l[2], l[3]))
        
        return lugares
            
        