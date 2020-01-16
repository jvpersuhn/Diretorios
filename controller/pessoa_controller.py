from dao.pessoa_dao import Pessoa_dao
from model.pessoa import Pessoa
from model.endereco import Endereco
class Pessoa_controller:
    def __init__(self):
        self.pd = Pessoa_dao()
    
    def select_all(self):
        pessoa = []
        for i in self.pd.select_all():
            pessoa.append(i)

        return pessoa

    def select_byId(self,Id):
        return self.pd.select_byId(Id)

    def select_tudo(self):
        lista_completa = []
        for i in self.pd.select_completo():
            p = Pessoa(i[0],i[1],i[2],i[3],i[4])
            e = Endereco(i[5],i[6],i[7],i[8],i[9],i[10],i[11])
            p.endereco = e
            lista_completa.append(p)
        return lista_completa