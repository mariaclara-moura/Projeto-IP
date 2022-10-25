import SpongeSprite
import SpriteGroups
import PlanctonSprite

import bobintrucoes

def personagens():
    bob = SpongeSprite.Sponge()
    plancton = PlanctonSprite.Plancton()
    SpriteGroups.todas_sprites.add(bob)
    SpriteGroups.todas_sprites.add(plancton)
    return bob,plancton

def personagens_menu():
    bob_menu = bobintrucoes.BobMenu()
    SpriteGroups.bob_menu.add(bob_menu)
    return bob_menu

bob,plancton = personagens()
bob_menu = personagens_menu()
