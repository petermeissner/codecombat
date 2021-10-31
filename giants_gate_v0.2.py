# Protect your base.
# Spawn units to assault the enemy base.
# Cast spells to react on enemies.


units = hero.availableUnits


hero.summon('shaman', 'A')
hero.summon('shaman', 'B')
hero.summon('shaman', 'C')
hero.summon('shaman', 'A')
hero.summon('shaman', 'B')
hero.summon('shaman', 'C')
hero.summon('shaman', 'A')
hero.summon('shaman', 'B')


while True:
    if hero.canSummonAt(70, 40):
        hero.summon('shaman', 'G')
    hero.summon('warlock', 'A')


