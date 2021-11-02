# Protect your base.
# Spawn units to assault the enemy base.
# Cast spells to react on enemies.


# Rank:  35/21755
# Score: 8198
# Notes: super weird experimental but somehow effective - for whatever reason


while hero.time < 25:
    hero.summon('warlock', 'D')
    hero.summon('warlock', 'A')
    hero.summon('shaman', 'A')
    e = hero.findNearestEnemy()
    hero.cast("lightning", e.x, e.y)



hero.summon('shaman', 'D') 
hero.summon('warlock', 'D')
hero.summon('shaman', 'B')
hero.summon('warlock', 'A')
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
        e = hero.findNearestEnemy()
        hero.cast("fireball", e.x, e.y)

    