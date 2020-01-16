from dao.conexao import Connection
from model.endereco import Endereco

class Endereco_dao(Connection):
    def select_all(self):
        self.cursor.execute("SELECT * FROM 01_JVP_ENDERECO")
        enderecos = self.cursor.fetchall()
        lista_endereco = []
        for i in enderecos:
            e = Endereco(i[0],i[1],i[2],i[3],i[4],i[5],i[6])
            lista_endereco.append(e)

        return lista_endereco

    def select_byId(self,Id):
        self.cursor.execute(f"SELECT * FROM 01_JVP_ENDERECO WHERE Id = {Id}")
        endereco = self.cursor.fetchone()
        e = Endereco(endereco[0],endereco[1],endereco[2],endereco[3],endereco[4],endereco[5],endereco[6])
        return e

    def insert(self, endereco : Endereco):
        self.cursor.execute(f"INSERT INTO 01_JVP_ENDERECO (LOGRADOURO,NUMERO,COMPLEMENTO,BAIRRO,CIDADE,CEP) VALUES ('{endereco.logradouro}','{endereco.numero}','{endereco.complemento}','{endereco.bairro}','{endereco.cidade}','{endereco.cep}')")
        self.connection.commit()