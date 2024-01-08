from karakters_info import *



karakter = input('welk kerakter wil je zijn mage/paladin/assisin\n')
if karakter == 'mage':
    player_hp = mage.health

elif karakter == 'paladin':
    player_hp = paladin.health

elif karakter == 'assisin':
    player_hp = assisin_karakter_hp
