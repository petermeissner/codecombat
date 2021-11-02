# Protect your base.
# Spawn units to assault the enemy base.
# Cast spells to react on enemies.

# Notes:  Works ok. Most importantly introduces functions to lay the basis for 
#         better abstraction of technacalities to be able to concentrate on 
#         strategy.

# warlock
# Rank:  1255 / 21,844
# Score: 5678

# shaman
# Rank:  306 / 21,844
# Score: 7052

# ogre
# Rank:  2242 / 21,844
# Score: 4472

# thrower
# Rank:  1241 / 21,844
# Score: 5686

# munchkin
# Rank:  13522 / 21,844
# Score: 3319

# brawler
# Rank:  15971 / 21,844
# Score: 1718


import random

def summon_points():
    points = []
    
    # check summon points
    if hero.canSummonAt(15, 40):
        points.append('A')
    if hero.canSummonAt(30, 40):
        points.append('B')
    if hero.canSummonAt(35, 65):
        points.append('C')
    if hero.canSummonAt(35, 15):
        points.append('D')
    if hero.canSummonAt(65, 65):
        points.append('E')
    if hero.canSummonAt(70, 40):
        points.append('F')
    if hero.canSummonAt(65, 15):
        points.append('G')
    
    # return list of available summon points
    return points

def summon_if_possible(unit='warlock', locations=['E', 'G', 'F', 'B', 'A', 'D', 'C']):
    summoned = False
    summon_points_now = summon_points() 
    for l in locations:
        if l in summon_points_now:
            hero.summon(unit, l)
            summoned = True
            break
        else:
            pass
    return summoned
        

while True:
    summon_if_possible('warlock')
    

    