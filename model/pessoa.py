
class Pessoa:
    def __init__(self,Id,Nome,Sobrenome,Idade,Id_Endereco='NULL'):
        self.id = Id
        self.nome = Nome
        self.sobrenome = Sobrenome
        self.idade = Idade
        self.id_endereco = Id_Endereco
        self.endereco = None

    def __str__(self):
        return f'{self.id};{self.nome};{self.sobrenome};{self.idade};{self.id_endereco}'

    @property
    def endereco(self):
        return self.endereco

    @endereco.setter
    def endereco(self,endereco):
        self.endereco = endereco

    def mostra(self):
        print(f'{self.id} {self.nome} {self.sobrenome} {self.idade} {self.id_endereco} {self.endereco}')