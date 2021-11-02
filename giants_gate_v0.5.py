
# Rank:  53 / 21755
# Score: 7957

def heal():
    fs = hero.findFriends()
    for f in fs:
        if f.type == 'warlock' and f.health < 150:
            hero.cast("heal", f.x, f.y)
            break

def fireball():
  enemies = hero.findEnemies()
  if len(enemies) > 5:
      hero.cast("fireball", enemies[0].x, enemies[0].y)


while hero.time < 25:
    hero.summon('warlock', 'D')
    heal() 
    hero.summon('shaman', 'A')
    heal() 
    hero.summon('shaman', 'C')
    heal() 
    hero.summon('warlock', 'B')



while True:
    if hero.canSummonAt(70, 40):
        hero.summon('shaman', "G")
    else:
        fireball()
    heal() 
    location = "A"
    hero.summon('warlock', location)    
    hero.summon('shaman', location)    
    
