from dao.conexao import Connection
from model.pessoa import Pessoa
from model.endereco import Endereco

class Pessoa_dao(Connection):
    def select_all(self):
        self.cursor.execute("SELECT * FROM 01_JVP_PESSOA")
        pessoas = self.cursor.fetchall()
        lista_pessoas = []
        for i in pessoas:
            p = Pessoa(i[0],i[1],i[2],i[3],i[4])
            lista_pessoas.append(p)

        return lista_pessoas
    
    def select_byId(self, Id):
        self.cursor.execute(f"SELECT * FROM 01_JVP_PESSOA WHERE Id = {Id}")
        pessoa = self.cursor.fetchone()
        p = Pessoa(pessoa[0],pessoa[1],pessoa[2],pessoa[3],pessoa[4])
        return p

    def select_completo(self):
        self.cursor.execute(f"SELECT * FROM 01_JVP_PESSOA P INNER JOIN 01_JVP_ENDERECO E ON P.ID_ENDERECO = E.ID")
        dados = self.cursor.fetchall()
        return dados

    def insert(self,pessoa : Pessoa):
        self.cursor.execute(f"INSERT INTO 01_JVP_PESSOA (Nome,Sobrenome,Idade,Id_Endereco) VALUES ('{pessoa.nome}','{pessoa.sobrenome}','{pessoa.idade}','{pessoa.id_endereco}')")
        self.connection.commit()
