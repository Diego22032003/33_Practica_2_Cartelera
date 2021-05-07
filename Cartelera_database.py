import mysql.connector

class MyDatabase:
    def open_connection(self):
        connectiion = mysql.connector.cennect(
            host="localhost",
            user="root",
            passwd="",
            database="db_Cartelera")
        return Connection

    def insert_db(self, Pelicula, Hora, Fecha, Idioma):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "INSERT INTO tbl_cartelera(PELICULA, HORA, BOLETOS, PRRECIO) VALUES(%,,%,%,%)"
        data = (pelicula, hora, fecha, idioma)
        cursor.execute(query, data)
        my_connection.commit()
        my_connection.close()