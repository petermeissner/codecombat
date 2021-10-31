# Protect your base.
# Spawn units to assault the enemy base.
# Cast spells to react on enemies.

# rank:  95/21509
# score: 7658

while hero.time < 4:
    hero.cast("lightning", 35, 65)

hero.summon('shaman', 'B')
hero.summon('shaman', 'A')
hero.summon('warlock', 'C')


counter = 0
while True:
    counter = counter + 1
    if hero.canSummonAt(70, 40):
        location = "G"
    else:
        location = "A"
    if counter % 2 == 0:
        hero.summon('warlock', location)
    else:
        hero.summon('shaman', location)


