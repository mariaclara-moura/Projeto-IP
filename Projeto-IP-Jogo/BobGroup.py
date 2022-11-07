#importacoes necessarias
import SpongeSprite
import SpriteGroups
import PlanctonSprite
import inimigo_2
import BobInstrucoes
import PlanctonInstrucoes

# criando os personagens do jogo em si: bob, plancton e inimigo 2
class Personagens():
    def __init__(self):
        self.bobb = Personagens.bob(self)
        self.plancton = PlanctonSprite.Plancton()
        self.plancton2 = inimigo_2.Plancton_2()
        SpriteGroups.todas_sprites.add(self.plancton)

    def bob(self):
        self.bob = SpongeSprite.Sponge()
        SpriteGroups.todas_sprites.add(self.bob)
        return self.bob

# criando os personagens dos menus: bob's e plancton e adicionando eles a um grupo de sprites
class Personagens_menu():

    def __init__(self):
        self.bob_menuu = Personagens_menu.personagens_menu(self)
        self.bob_menuu2 = Personagens_menu.personagens_menu2(self)
        self.bob_menuu3 = Personagens_menu.personagens_menu3(self)

    def personagens_menu(self):
        self.bob_menu = BobInstrucoes.BobMenu()
        SpriteGroups.bob_menu.add(self.bob_menu)
        return self.bob_menu

    def personagens_menu2(self):
        self.bob_menu2 = BobInstrucoes.BobMenu2()
        SpriteGroups.personagensmenu2.add(self.bob_menu2)
        return self.bob_menu2

    def personagens_menu3(self):
        self.bob_menu3 = BobInstrucoes.BobMenu3()
        self.plancton_menu = PlanctonInstrucoes.PlanctonMenu()
        SpriteGroups.personagensmenu3.add(self.bob_menu3)
        SpriteGroups.personagensmenu3.add(self.plancton_menu)
        return self.bob_menu3

# chamando as classes por meio de variáveis
personagens = Personagens()
menus = Personagens_menu()






