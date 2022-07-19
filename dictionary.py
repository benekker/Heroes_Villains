def heroes_dict(heroes):
    heroes_list = []
    for hero in heroes:
        hero = {
        "name": hero.name,
        "alter_ego": hero.alter_ego,
        "catchphrase": hero.catchphrase,
        "primary_ability": hero.primary_ability,
        "secondary_ability": hero.secondary_ability,
        }
        heroes_list.append(hero)
    return heroes_list

def villains_dict(villains):
    villains_list = []
    for villain in villains:
        villain = {
        "name": villain.name,
        "alter_ego": villain.alter_ego,
        "catchphrase": villain.catchphrase,
        "primary_ability": villain.primary_ability,
        "secondary_ability": villain.secondary_ability,
        }
        villains_list.append(villain)
    return villains_list






