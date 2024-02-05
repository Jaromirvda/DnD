import psycopg2

# verander de juiste info hieronder voor jou eigen pgadmin info
conn = psycopg2.connect(host='localhost', database='', user='postgres', password='')
cur = conn.cursor()

# Tier 1 Monsters
cur.execute('select monster_name, monster_damage, monster_hp, monster_speed, monster_armer from monster_tier1 where monster_id = 1')
tier1_monster1_data = cur.fetchone()
tier1_monster1_name, tier1_monster1_damage, tier1_monster1_hp, tier1_monster1_speed, tier1_monster1_armer = tier1_monster1_data

cur.execute('select monster_name, monster_damage, monster_hp, monster_speed, monster_armer from monster_tier1 where monster_id = 2')
tier1_monster2_data = cur.fetchone()
tier1_monster2_name, tier1_monster2_damage, tier1_monster2_hp, tier1_monster2_speed, tier1_monster2_armer = tier1_monster2_data

cur.execute('select monster_name, monster_damage, monster_hp, monster_speed, monster_armer from monster_tier1 where monster_id = 3')
tier1_monster3_data = cur.fetchone()
tier1_monster3_name, tier1_monster3_damage, tier1_monster3_hp, tier1_monster3_speed, tier1_monster3_armer = tier1_monster3_data

# Tier 2 Monsters
cur.execute('select monster_name, monster_damage, monster_hp, monster_speed, monster_armer from monster_tier2 where monster_id = 1')
tier2_monster1_data = cur.fetchone()
tier2_monster1_name, tier2_monster1_damage, tier2_monster1_hp, tier2_monster1_speed, tier2_monster1_armer = tier2_monster1_data

cur.execute('select monster_name, monster_damage, monster_hp, monster_speed, monster_armer from monster_tier2 where monster_id = 2')
tier2_monster2_data = cur.fetchone()
tier2_monster2_name, tier2_monster2_damage, tier2_monster2_hp, tier2_monster2_speed, tier2_monster2_armer = tier2_monster2_data

cur.execute('select monster_name, monster_damage, monster_hp, monster_speed, monster_armer from monster_tier2 where monster_id = 3')
tier2_monster3_data = cur.fetchone()
tier2_monster3_name, tier2_monster3_damage, tier2_monster3_hp, tier2_monster3_speed, tier2_monster3_armer = tier2_monster3_data

# Bosses
cur.execute('select boss_name, boss_damage, boss_hp, boss_speed, boss_armer from boss where boss_id=1')
boss1_data = cur.fetchone()
boss1_name, boss1_damage, boss1_hp, boss1_speed, boss1_armer = boss1_data

cur.execute('select boss_name, boss_damage, boss_hp, boss_speed, boss_armer from boss where boss_id=2')
boss2_data = cur.fetchone()
boss2_name, boss2_damage, boss2_hp, boss2_speed, boss2_armer = boss2_data

cur.execute('select boss_name, boss_damage, boss_hp, boss_speed, boss_armer from boss where boss_id=3')
boss3_data = cur.fetchone()
boss3_name, boss3_damage, boss3_hp, boss3_speed, boss3_armer = boss3_data

# Characters
cur.execute('select class_name, class_hp, class_damage, class_speed, magic_damage, true_damage, stealth_damage, class_armer from karakter_classes where class_id =1')
mage_karakter_data = cur.fetchone()
mage_karakter_name, mage_karakter_hp, mage_karakter_damage, mage_karakter_speed, mage_karakter_magic_damage, mage_karakter_true_damage, mage_karakter_stealth_damage, mage_karakter_armer = mage_karakter_data

cur.execute('select class_name, class_hp, class_damage, class_speed, magic_damage, true_damage, stealth_damage, class_armer from karakter_classes where class_id =2')
assisin_karakter_data = cur.fetchone()
assisin_karakter_name, assisin_karakter_hp, assisin_karakter_damage, assisin_karakter_speed, assisin_karakter_magic_damage, assisin_karakter_true_damage, assisin_karakter_stealth_damage, assisin_karakter_armer = assisin_karakter_data

cur.execute('select class_name, class_hp, class_damage, class_speed, magic_damage, true_damage, stealth_damage, class_armer from karakter_classes where class_id =3')
paladin_karakter_data = cur.fetchone()
paladin_karakter_name, paladin_karakter_hp, paladin_karakter_damage, paladin_karakter_speed, paladin_karakter_magic_damage, paladin_karakter_true_damage, paladin_karakter_stealth_damage, paladin_karakter_armer = paladin_karakter_data

cur.close()
conn.close()

print (paladin_karakter_hp)