# Importando a classe Blender Game Engine
import bge
# Bibliotecas de matemática: graus e radianos
from math import degrees, radians
# O atual controlador:
cont = bge.logic.getCurrentController()
# O objeto ligado no controlador principal
own = cont.owner
# A cena atual
scn = own.scene
# Lista de cenários:
scl = bge.logic.getSceneList()
# Lista de objetos:
obj = scn.objects

# Classe principal do game
class Game():
    def start(self):
        # Executa somente no início 
        #de carregamento da aplicação
        print('Game started.')
        self.rotate()
    def update(self):
        # Executa sempre enquanto a aplicação
        # estiver ativa.
        print("Game updating...")
    def rotate(self):
        #Para obter as informações de orientação:
        xyz = own.localOrientation.to_euler() 
        #Para aplicar uma rotação de 20 graus
        xyz.z = radians(45)
        # Para aplicar a rotação local:
        own.localOrientation = xyz
        # Para exibir a rotação em graus:
        print(degrees(xyz.z))
        # variável de depuração para exibir o ângulo
        own['angle'] = degrees(xyz.z)

def run():
    # Cria o objeto de Game
    g = Game()
    # Para executar apenas uma interação
    # Necessário ligar o sensor.
    if cont.sensors['tap'].positive:        
        # Executa o método start.
        g.start()
    
