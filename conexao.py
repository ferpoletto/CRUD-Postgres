import psycopg2

class Connection():

    def get_connection(self):
        try:
            connection = psycopg2.connect(user="postgres",
                                          password="ads",
                                          host="127.0.0.1",
                                          port="5432",
                                          database="banco_livro")
            return connection
        except:
            print('Falha na conexão')
