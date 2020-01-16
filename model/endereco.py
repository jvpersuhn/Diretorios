class Endereco:
    def __init__(self, Id, Logradouro, Numero, Complemento, Bairro, Cidade, Cep):
        self.id = Id
        self.logradouro = Logradouro
        self.numero = Numero
        self.complemento = Complemento
        self.bairro = Bairro
        self.cidade = Cidade
        self.cep = Cep

    def __str__(self):
        return f'{self.id};{self.logradouro};{self.numero};{self.complemento};{self.bairro};{self.cidade};{self.cep}'