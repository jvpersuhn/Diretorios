from dao.endereco_dao import Endereco_dao
from model.endereco import Endereco

class Endereco_controller:
    def __init__(self):
        self.ed = Endereco_dao()
    
    def select_all(self):
        return self.ed.select_all()

    def select_byId(self,id):
        return self.ed.select_byId(id)

    def insert(self, logradouro, numero, complemento, bairro, cidade, cep):
        e = Endereco(None, logradouro, numero, complemento, bairro, cidade, cep)
        self.ed.insert(e)