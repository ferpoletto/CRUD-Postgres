import psycopg2
from CRUD_Postgres.conexao import Connection

class Livro():

    def __init__(self):
        connection = Connection().get_connection()

    def cadastrar(self, autor, tipo):
        pass

    def mostrar(self, mostrar):
        pass

    def editar(self, atualiza, autor, tipo):
        pass

    def deletar(self, delete):
        pass
    def existe(self, find):
        flag = 0



        return flag





