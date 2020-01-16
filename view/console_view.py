import sys
sys.path.append('C:/Users/900143/Desktop/Diretorios')
from controller.pessoa_controller import Pessoa_controller
from controller.endereco_controller import Endereco_controller

pc = Pessoa_controller()

#for i in pc.select_all():
#    print(i)

#print(pc.select_byId(1))

for i in pc.select_tudo():
    print(i.mostra())

ec = Endereco_controller()

#for i in ec.select_all():
#    print(i)

#print(ec.select_byId(1))

#ec.insert('Fim do mundo','24','oca','fim do mundo','blumevrau','89563365')


