import random, time, sys
#change fun. to not repeat itself
#Make more like VGC
    #need to duplicate player stats, and monster stats...
    #make either input for functions

#      NOTES
#      1. VGC Mode not work
#      2. 
win = 0
lose = 0
gob_killed = 0
troll_killed = 0
orc_killed = 0
point = 0
santa_time = 0
shield = 0
use_move = 0
defence = 0
mon_damage = 0
power_move = 0
mon_strength = 0
crazy = 0
heal = 0
p_attack = 0
money = 0
sword = 0
shields = 0
armor = 0
horse = 0
buy_modifier = 1
bomb = 0
heal_pot = 0
invincible_pot = 0
str_pot = 0
temp_shield = 0
item = 0
damage_s = 0
invinc = 0
hp_points = 0
hard = 0
speed2 = 0
strength2 = 0
health2 = 0
name2 = 0
defence2 = 0
p_attack2 = 0
dexterity2 = 0
#mana2 = 0
magic_discription2 = None
two_p = 0
b_mode = 0
br_shield = 0
bonus = 0
action = 0
crit = 0
highscore = 0
hit = 0
mon_dext = 0
damage = 0
quest = 0
focus = 0
ol_charge = 0
mon_speed = 0
ai = False
mp_used = False
mon_attacked = False
fly = False
FirstSelected = False
speed_add = False
double = False
firstTurn = True
ability_add = False


def clear_stats() :
    global speed_add, double, firstTurn, ability_add, crazy, money, sword, shields, armor, horse, buy_modifier, item, shield, power_move, two_p, b_mode, bonus, action, crit, alive, done, journey, focus, ol_charge, ai, mp_used
    money = 0
    crazy = 0
    sword = 0
    shields = 0
    armor = 0
    horse = 0
    buy_modifier = 1
    bomb = 0
    heal_pot = 0
    invincible_pot = 0
    str_pot = 0
    temp_shield = 0
    item = 0
    shield = 0
    power_move = 0
    two_p = 0
    b_mode = 0
    bonus = 0
    action = 0
    crit = 0
    mon_dext = 0
    journey = None
    alive = True
    done = True
    focus = 0
    ol_charge = 0
    ai = False
    mp_used = False
    speed_add = False
    double = False
    firstTurn = True
    ability_add = False
    
def choose_mode() :
    global ability_add, speed_add, double, crazy, money, hard, journey, ai
    clear_stats()
    print('1 = easy mode  2 = hard mode  3 = crazy mode  4 = buy mode  5 = journey mode  6 = AI mode  7 = VGC mode')
    if ability_add == False and speed_add == False : #always happens??
        print('8 = speed addition  9 = ability addition')
    elif not ability_add :
        print('9 = ability addition')
    elif not speed_add :
        print('8 = speed addition')       
    ans = input()
    if str(ans) == 'n' :
        end_game()
    try :
        int(ans)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        choose_mode()
    else :
        if int(ans) == 1 :
            choose_mon()
        elif int(ans) == 2 :
            hard = hard + 0.5
            choose_hard_mon()
        elif int(ans) == 3 :
            crazy = 1
            crazy_mode()
        elif int(ans) == 4 :
            buy_modifier = 2
            money = 500
            buy()
        elif int(ans) == 5 :
            journey = 0
            journey_mode()
        elif int(ans) == 6 :
            ai = True
            AI_mode()
            #AI_mode(monster,mon_health,mon_strength,mon_dext,'''mon_def''',mon)
        elif int(ans) == 7 :
            double = True
            AI_mode()
            #AI_mode(monster,mon_health,mon_strength,mon_dext,'''mon_def''',mon)
            #AI_mode(monster2,mon_health2,mon_strength2,mon_dext2,mon_def2,mon2)
        #elif int(ans) == 5 :
            #two_player()
        elif int(ans) == 8 :
            speed_add = True
            choose_mode()
        elif int(ans) == 9 :
            ability_add = True
            choose_mode()
        else :
            choose_mon()
'''
def two_player() :
    global two_p
    two_p = 1
    choose_two_mon()
    print('player 1')
    choose_fighter()
    print('player 2')
    choose_fighter_2()

def choose_two_mon() :
    global monster, mon, mon_health, mon_strength, monster_2, mon_health_2, mon_strength_2
    mon = random.randint(1,3)
    if mon == 1 :
        monster = "Goblin"
        mon_health = 50
        mon_strength = 2
    elif mon == 2:
        monster = "Troll"
        mon_health = 60
        mon_strength = 4
    elif mon == 3:
        monster = 'Orc'
        mon_health = 48 
        mon_strength = 5
    mon = random.randint(1,3)
    if mon == 1 :
        monster_2 = "Goblin"
        mon_health_2 = 50
        mon_strength_2 = 2
    elif mon == 2:
        monster_2 = "Troll"
        mon_health_2 = 60
        mon_strength_2 = 4
    elif mon == 3:
        monster_2 = 'Orc'
        mon_health_2 = 48 
        mon_strength_2 = 5
        
def choose_fighter_2() :
    global speed_2, strength_2, health_2, name_2, ans, defence_2, p_attack_2
    print('Choose your fighter:')
    print('1 = Swordmaster str: +2  spd: +6  HP: 40    def: +1')
    print('2 = Knight      str: +3  spd: -1  HP: 35    def: +6')
    print('3 = Wizard      str: +6  spd: +2  HP: 35    def: 0')
    print('4 = Prince      str: 1-9 spd: 1-8 HP: 30-42 def: +1-6 random stats')
    print('5 = Princess    str: -4  spd: +5  HP: 70    def: +2')
    print('6 = Archer      str: +2  spd: +4  HP: 25    def: +1 50% monster miss')
    print('7 = Berserker   str: +2  spd: +1  HP: 50    def: 0')
    print('8 = Zombie      str: +3  spd: +5  HP: 35    def: 0  can have negative HP')
    print('9 = Overlord    str: __  spd: __  HP: __    def: __ choose your stats')
    ans = input()
    if int(ans) == 1:
        name_2 = 'Swordmaster'
        strength_2 = 2
        speed_2 = 6
        health_2 = 40
        defence_2 = 1
        p_attack_2 = '(20 damage)'
    elif int(ans) == 2:
        name_2 = 'Knight'
        strength_2 = 3
        speed_2 = -1
        health_2 = 35
        defence_2 = 6
        p_attack_2 = '(+3 defence and 5-12 damage)'
    elif int(ans) == 3:
        name_2 = 'Wizard'
        strength_2 = 6
        speed_2 = 2
        health_2 = 35
        defence_2 = 0
        p_attack_2 = '(-1-30 damage)'
    elif int(ans) == 4:
        name_2 = 'Prince'
        strength_2 = random.randint(1,9)
        speed_2 = random.randint(1,8)
        health_2 = random.randint(30,42)
        defence_2 = random.randint(1,6)
        print('str: ' + str(strength) + '  spd: ' + str(speed) + '  HP: ' + str(health) + '  defense: ' + str(defence))
        p_attack_2 = '(change defense, strength and +5 health)'
    elif int(ans) == 5:
        name_2 = 'Princess'
        strength_2 = -4
        speed_2 = 5
        health_2 = 70
        defence_2 = 2
        p_attack_2 = '(heal 25 damage)'
    elif int(ans) == 6:
        name_2 = 'Archer'
        strength_2 = 2
        speed_2 = 4
        health_2 = 25
        defence_2 = 1
        p_attack_2 = '(reset battle)'
    elif int(ans) == 7 :
        name = 'Berserker'
        strength = 2
        speed = 1
        health = 50
        defence = 0
        p_attack = '(+10 str -8 def)'
    elif int(ans) == 8 :
        name = 'Zombie'
        strength = 3
        speed = 5
        health = 35
        defence = 0
        p_attack = '(change HP to 1)'
    elif int(ans) == 9 :
        name = 'Overlord'
        ol_points = 14
        print('Choose your stats (the rest will be health x5)')
        time.sleep(0.75)
        print('OL: ' + str(ol_points))
        time.sleep(0.75)
        print('Choose strength; -5,13')
        ans = input()
        if int(ans) <= ol_points and int(ans) >= -5 and int(ans) <= 13:
            strength = ans
            ol_points = int(ol_points) - int(ans)
        else :
            print('You cannot use that amount')
            time.sleep(0.75)
            print('You will get 2 str')
            strength = 2
            ol_points = int(ol_points) - 2
        print('Choose speed; -1,13')
        ans = input()
        time.sleep(0.75)
        print('OL: ' + str(ol_points))
        if int(ans) <= ol_points and int(ans) >= -1 and int(ans) <= 13:
            speed = ans
            ol_points = int(ol_points) - int(ans)
            print(str(speed))
        else :
            print('You cannot use that amount')
            time.sleep(0.75)
            print('You will get 3 spd')
            ol_points = int(ol_points) - 3
            speed = 3
        print('Choose defence; -5,13')
        ans = input()
        time.sleep(0.75)
        print('OL: ' + str(ol_points))
        if int(ans) <= ol_points and int(ans) >= -5 and int(ans) <= 13:
            defence = ans
            ol_points = int(ol_points) - int(ans)
            print(str(defence))
        else :
            print('You cannot use that amount')
            time.sleep(0.75)
            print('You will get 1 def')
            ol_points = int(ol_points) - 1
            defence = 1
        health = ol_points*5
        print('HP: ' + str(health))
        p_attack = "(gain two turns of invincibility)"
    elif int(ans) == 10:
        global santa_time
        name_2 = 'Santa'
        strength_2 = 44
        speed_2 = 18
        health_2 = 1
        defence_2 = 0
        santa_time = santa_time +1
        p_attack_2 = '(-1000-1000 damage)'
    elif int(ans) == random.randint(11,21):
        name_2 = 'King'
        speed_2 = 100
        health_2 = 100
        defence_2 = 100
        print('You chose the correct number. You will be the King')
        time.sleep(0.75)
        print('How much strength do you want?')
        strength_2 = int(input())
        p_attack_2 = '(2 damage + strength)'
    elif int(ans) == 99:
        name_2 = 'Test'
        print('How much strength do you want?')
        strength_2 = int(input())
        print('How much speed do you want?')
        speed_2 = int(input())
        print('How much health do you want?')
        health_2 = int(input())
        print('How much defense do you want?')
        defence_2 = int(input())
        p_attack_2 = '(2 damage + strength)'
    else:
        print('That is not an option, you will be a footsoldier')
        name_2 = 'Footsoldier'
        strength_2 = -1
        speed_2 = -1
        health_2 = 25
        defence_2 = 0
        p_attack_2 = '(heal 10 damage, deal 1-20 damage)'        
'''
def buy() :
    if int(money) > 0 :
        print(str(money) + ' gold')
        time.sleep(0.75)
        print('1 = swords  2 = shields  3 = armor  4 = horses  5 = items  6 = packages 7 = done buying')
        ans = input()
        try :
            int(ans)
        except :
            print('That is not a number.')
            time.sleep(0.75)
            buy()
        else :
            if int(ans) == 1 :
                buy_sword()
            elif int(ans) == 2 :
                buy_shield()
            elif int(ans) == 3 :
                buy_armor()
            elif int(ans) == 4 :
                buy_horse()
            elif int(ans) == 5 :
               buy_item()
            elif int(ans) == 6 :
                buy_package()
            elif int(ans) == 7 :
                choose_hard_mon()    
    else :
        choose_hard_mon()    
        
def buy_item() :
    global money, sword, item, bomb, temp_shield, heal_pot, str_pot, invincible_pot
    print('1 = bomb(100g)  2 = health potion(100g)  3 = invincible potion(250g)  4 = temporary shield(100g)  5 = strength potion(100g)  6 = get out')
    ans = input()
    try :
        int(ans)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        buy_item()
    else :
        if int(ans) == 1 and int(money) - 100 >=0 :
            bomb = bomb +1
            item = item +1
            money = money - 100
            buy()
        elif int(ans) == 2 and int(money) - 100 >=0 :
            heal_pot = heal_pot +1
            money = money - 100
            item = item +1
            buy()
        elif int(ans) == 3 and int(money) - 250 >=0 : 
            invincible_pot = invincible_pot +1
            item = item +1
            money = money - 250
            buy()
        elif int(ans) == 4 and int(money) - 100 >=0 :
            temp_shield = temp_shield +1
            item = item +1
            money = money - 100
            buy()
        elif int(ans) == 5 and int(money) - 100 >=0 :
            str_pot = str_pot +1
            item = item +1
            money = money - 100
            buy()
        elif int(ans) == 6 :
            buy()
        else :
            print('you cannot buy that')
            buy()
        
        
def buy_sword() :
    global money, sword
    print('1 = dagger(125g) +1 str  2 = short sword(200g) +2 str  3 = claymore(325g) +4 str  4 = broadsword(400g) +5 str  5 = get out')
    ans = input()
    try :
        int(ans)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        buy_sword()
    else :
        if int(ans) == 1 and int(money) - 125 >=0 :
            sword = 1
            money = money - 125
            buy()
        elif int(ans) == 2 and int(money) - 200 >=0 :
            sword = 2
            money = money - 200
            buy()
        elif int(ans) == 3 and int(money) - 325 >=0 : 
            sword = 4
            money = money - 325
            buy()
        elif int(ans) == 4 and int(money) - 400 >=0 :
            sword = 5
            money = money - 400
            buy()
        elif int(ans) == 5 :
            buy()
        else :
            print('you cannot buy that')
            buy()

        
def buy_shield() :
    global money, shields
    print('1 = wooden shield(100g) 6HP  2 = round shield(200g) 12HP  3 = kite shield(300g) 24HP  4 = get out')
    ans = input()
    try :
        int(ans)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        buy_shield()
    else :
        if int(ans) == 1 and int(money) - 100 >=0 :
            shields = 6
            money = money - 100
            buy()
        elif int(ans) == 2 and int(money) - 200 >=0 :
            shields = 12
            money = money - 200
            buy()
        elif int(ans) == 3 and int(money) - 300 >=0 : 
            shields = 24
            money = money - 300
            buy()
        elif int(ans) == 4 :
            buy()
        else :
            print('you cannot buy that')
            buy()
        

def buy_armor() :
    global money, armor
    print('1 = leather armor(225g) +2 def  2 = chainmail(300g) +3 def  3 = platemail(325g) +4 def  4 = reenforced steel armor(375g) +5 def  5 = get out')
    ans = input()
    try :
        int(ans)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        buy_armor()
    else :
        if int(ans) == 1 and int(money) - 225 >=0 :
            armor = 2
            money = money - 225
            buy()
        elif int(ans) == 2 and int(money) - 300 >=0 :
            armor = 3
            money = money - 300
            buy()
        elif int(ans) == 3 and int(money) - 325 >=0 : 
            armor = 4
            money = money - 325
            buy()
        elif int(ans) == 4 and int(money) - 375 >=0 :
            armor = 5
            money = money - 375
            buy()
        elif int(ans) == 5 :
            buy()
        else :
            print('you cannot buy that')
            buy()
        

def buy_horse() :
    global money, horse
    print('1 = pony(75g) +2 spd  2 = stallion(125g) +4 spd  3 = war horse(250g) +3 spd +2 str  4 = get out')
    ans = input()
    try :
        int(ans)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        buy_horse()
    else :
        if int(ans) == 1 and int(money) - 75 >=0 :
            horse = 2
            money = money - 75
            buy()
        elif int(ans) == 2 and int(money) - 125 >=0 :
            horse = 4
            money = money - 125
            buy()
        elif int(ans) == 3 and int(money) - 350 >=0 : 
            horse = 3
            sword = sword +2
            money = money - 350
            buy()
        elif int(ans) == 4 :
            buy()
        else :
            print('you cannot buy that')
            buy()
        

def buy_package() :
    global money, horse, shields, armor, sword
    print('1 = Round shield + platemail(500g) +4 def 12HP  2 = war horse + short sword + wooden shield(500g) +3 spd 6HP +4 str  3 = claymore + round shield(475) +4 str 12HP  4 = get out')
    ans = input()
    try :
        int(ans)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        buy_package()
    else :
        if int(ans) == 1 and int(money) - 500 >=0 :
            shields = 12
            armor = 4
            money = money - 500
            buy()
        elif int(ans) == 2 and int(money) - 500 >=0 :
            sword = 4
            shields = 6
            horse = 3
            money = money - 500
            buy()
        elif int(ans) == 3 and int(money) - 475 >=0 : 
            shields = 12
            sword = 4
            money = money - 475
            buy()
        elif int(ans) == 4 :
            buy()
        else :
            print('you cannot buy that')
            buy()
        

#def AI_mode(monster,mon_health,mon_strength,mon_dext,mon_def,mon) :
def AI_mode() :
    global mon, monster, mon_health, mon_strength, mon_dext, mon_speed
    print('1 = Gladiator')
    print('2 = Dragon')
    print('3 = Goblin')
    print('4 = Orc')
    print('5 = Troll')
    print('6 = Wyvern')
    print('7 = Random')
    print('What enemy do you want to face? ')
    ans = input()
    try :
        int(ans)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        AI_mode()
    else :
        if int(ans) == 7 :
            ans = random.randint(1,6)
        if int(ans) == 1 :
            mon = 7
            monster = "Gladiator"
            mon_health = 55
            mon_strength = 3
            mon_dext = 3
            #mon_def = 2
            mon_speed = 1
        elif int(ans) == 2 :
            mon = 8
            monster = "Dragon"
            mon_health = 60
            mon_strength = 5
            mon_dext = 2
            #mon_def = 4
            mon_speed = 1
        if int(ans) == 3 :
            mon = 1
            monster = "Goblin"
            mon_health = 50
            mon_strength = 2
            mon_dext = 3
            #mon_def = 0
            mon_speed = 3
        elif int(ans) == 4 :
            mon = 2
            monster = "Troll"
            mon_health = 60
            mon_strength = 4
            mon_dext = -1
            #mon_def = 2
            mon_speed = -1
        elif int(ans) == 5 :
            mon = 3
            monster = "Orc"
            mon_health = 48
            mon_strength = 5
            mon_dext = 2
            #mon_def = 2
            mon_speed = 2
        elif int(ans) == 6 :
            mon = 9
            monster = "Wyvern"
            mon_health = 40
            mon_strength = 3
            mon_dext = 4
            #mon_def = 1
            mon_speed = 2
    
def CheckAbility(time, damage) :
    global health, defense, focus
    damage = int(damage)
    time = str(time)
    if name == 'Swordmaster' and time == 'YourTurn' :
        crit = random.randint(1,20)
        if crit == 19 or crit == 20 :
            print('You got a critical hit.')
            return 'crit'
    elif name == 'Knight' and time == 'StartTurn' :
        pitstop = random.randint(1,5)
        if pitstop > 3 :
            print('Your page repaired your armor, +3 def')
            defense += 3
    elif name == 'Wizard' and time == 'StartTurn' :
        if mon_health >= 30 :
            mana += 5
            print('You gained some mana, +5 mana')
    elif name == 'Prince' and time == 'MonsterTurn' :
        if damage == 7 or damage == 17 or damage == 27 or damage == 37 :
            print('You absorbed that hit')
            health += damage
    elif name == 'Princess' and time == 'StartTurn' :
        if int(health) <= int(mon_health) :
            print('You evened the tables')
            newHP = mon_health - health
            health += newHP
    elif name == 'Archer' :
        pass
    elif name == 'Berserker' and time == 'StartTurn' :
        constition = random.randint(1,5)
        if int(constition) == 5 :
            print('You feel refreshed and ready to face anything')
            focus += 1
    elif name == 'Zombie' and time == 'StartTurn' :
        health += 5
        print('You healed 5 HP')
        #print_health()
    elif name == 'Overlord' :
        pass
    elif name == 'Gladiator' :
        pass
    elif name == 'Goblin' :
        pass
    elif name == 'Dragon' and time == 'MonsterTurn' :
        if damage >= 35 :
            health += 15
            print('Your scales reflected some of the damage')
    elif name == 'Troll' :
        pass
    elif name == 'Orc' and time == 'YourTurn' :
        if mon_health >= 30 :
            return 5
    elif name == 'Wyvern' and time == 'MonsterTurn':
        dodge = random.randint(1,10)
        if dodge == 10 :
            print('You absorbed that hit')
            health += damage
    else :
        return None
    
    
def journey_mode():
    global max_health, journey
    journey = journey + 1
    # change to have different tests
    if journey == 1 :
        choose_quest()
    else :
        easy = random.randint(1,3)
        if easy == 1 and int(journey) > 2 :
            journey = journey - 1
        add_stat()
        rest_stop()
        next_battle()
        first_turn()
        update()
    #make each battle harder
    #add a stat each battle

def choose_quest() :
    global quest
    print('1 = Kill 4 Goblins, 2 = kill 3 Orcs, 3 = kill 2 Trolls, 4 = kill 6 monsters')
    time.sleep(0.75)
    print('Which quest do you want?')
    ans = input()
    try :
        int(ans)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        choose_quest()
    else :
        if int(ans) == 1 :
            quest = 'gob'
        elif int(ans) == 2 :
            quest = 'orc'         
        elif int(ans) == 3 :
            quest = 'tro'
        elif int(ans) == 4 :
            quest = 'mon'
        else :
            print('that was not an option')
            choose_quest()
        
def rest_stop():
    global health, max_health, power_move, mana, b_mode, strength, mon_strength, focus
    if name == 'Berserker' :
        b_mode = 0
        strength = strength - 10
        mon_strength = mon_strength - 8
    power_move = 0
    if name == 'Wizard' :
        mana = mana + 10
    else :
        mana = mana + 1
    if name == 'Knight' :
        defence = defence - 3
    max_health = max_health + 5
    health = max_health
    print('You made it to the next camp and rested up.')
    
def add_stat() :
    global strength, speed, dexterity, defence, max_health, focus
    print('You leveled up')
    time.sleep(0.75)
    print('Which stat do you want to increase? str, spd, dex, HP, def or fortify self(for)')
    ans = input()
    if ans == 'str':
        strength = int(strength) + 1        
    elif ans == 'spd':
        speed = int(speed) + 1
    elif ans == 'dex':
        dexterity = int(dexterity) + 1
    elif ans == 'def':
        defence = int(defence) + 1
    elif ans == 'HP' :
        max_health = int(max_health) + 5
    elif ans == 'for' :
        focus = int(focus) + 1
    else :
        print('that was not an option')
        time.sleep(0.75)
        print('you do not get any stat bonuses')
    
def next_battle() :
    global monster, mon, mon_health, mon_strength, mon_dext
    if journey <= 4 :
        mon = random.randint(1,3)
    else :
        mon = random.randint(1,6)
    if mon == 1 :
        monster = "Goblin"
        mon_health = 50 + 5*journey
        mon_strength = 2 + 1*journey
        mon_dext = 3 + 1*journey
    elif mon == 2:
        monster = "Troll"
        mon_health = 60 + 5*journey
        mon_strength = 4 + 1*journey
        mon_dext = -1 + 1*journey
    elif mon == 3:
        monster = 'Orc'
        mon_health = 48 + 5*journey
        mon_strength = 5 + 1*journey
        mon_dext = 2 + 1*journey
    elif mon == 4:
        monster = 'Goblin Theif'
        mon_health = 20 + 5*journey
        mon_strength = 5 + 2*journey
        mon_dext = 3 + 1*journey
    elif mon == 5:
        monster = 'Cave Troll'
        mon_health = 100 
        mon_strength = 3 + 1*journey
        mon_dext = -2 + 1*journey
    elif mon == 6:
        monster = 'Orc Warlord'
        mon_health = 58 + 5*journey
        mon_strength = 6 + 1*journey
        mon_dext = 3 + 1*journey
        
def crazy_mode() :
    global monster, mon, mon_health, mon_strength
    mon = random.randint(1,6)
    if int(mon) == 1:
        monster = 'Goblin'
        mon_health = 51
        mon_strength = 2
    elif int(mon) == 2:
        monster = 'Troll'
        mon_health = 59
        mon_strength = 5
    elif int(mon) == 3:
        monster = 'Orc'
        mon_health = 44
        mon_strength = 7
    elif int(mon) == 4:
        monster = 'Goblin Mage'
        mon_health = random.randint(20,70)
        mon_strength = random.randint(2,13)
    elif int(mon) == 5:
        monster = 'Tough Troll'
        mon_health = 71
        mon_strength = 1
    elif int(mon) == 6:
        monster = 'Orc Warrior'
        mon_health = 43
        mon_strength = 6
        
def choose_hard_mon() :
    global monster, mon, mon_health, mon_strength, mon_dext
    mon = random.randint(1,3)
    if mon == 1 :
        monster = "Goblin"
        mon_health = 50
        mon_strength = 2
        mon_dext = 3
    elif mon == 2:
        monster = "Troll"
        mon_health = 60
        mon_strength = 4
        mon_dext = -1
    elif mon == 3:
        monster = 'Orc'
        mon_health = 48 
        mon_strength = 5
        mon_dext = 2
        
def choose_mon() :
    global monster, mon, mon_health, mon_dext
    mon = random.randint(1,3)
    if mon == 1 :
        monster = "Goblin"
        mon_health = 38
        mon_dext = 1
    elif mon == 2:
        monster = "Troll"
        mon_health = 45
        mon_dext = -1
    elif mon == 3:
        monster = 'Orc'
        mon_health = 42
        mon_dext = 1

def gladiator_fighters() :
    global FirstSelected, speed, strength, health, name, ans, defence, p_attack, dexterity, lose, max_health, mana, magic_discription
    print('Choose your fighter:')
    print('1 = Gladiator   str: +3  spd: +1  HP: 55   def: +2   dex: +3')
    print('2 = Dragon      str: +5  spd: +1  HP: 60   def: +4   dex: +2')
    print('3 = Goblin      str: +2  spd: +3  HP: 50   def: 0    dex: +3')
    print('4 = Troll       str: +4  spd: -1  HP: 60   def: +2   dex: -1')
    print('5 = Orc         str: +5  spd: +2  HP: 48   def: +2   dex: +2')
    print('6 = Wyvern      str: +3  spd: +2  HP: 40   def: +1   dex: +4')
    ans = input()
    try :
        int(ans)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        gladiator_fighters()
    else :
        if int(ans) == 1 :
            name = "Gladiator"
            health = 55
            strength = 3
            dexterity = 3
            defence = 2
            speed = 1
            mana = 3
            magic_discription = '(-1 to each opponent stat, 5 damage)'
            p_attack = '(Deal 20-30 damage)'
        elif int(ans) == 2 :
            name = "Dragon"
            health = 60
            strength = 5
            dexterity = 2
            defence = 4
            speed = 1
            mana = 5
            magic_discription = '(breathe fire 1-20 damage)'
            p_attack = '(breathe gold fire - auto pierce)'
        if int(ans) == 3 :
            name = "Goblin"
            health = 50
            strength = 2
            dexterity = 3
            defence = 0
            speed = 3
            mana = 3
            magic_discription = '(gain 4 dex)'
            p_attack = '(auto crit)'
        elif int(ans) == 4 :
            name = "Troll"
            health = 60
            strength = 4
            dexterity = -1
            defence = 2
            speed = -1
            mana = 3
            magic_discription = '(deal 1-10 damage, heal the difference)'
            p_attack = '(If less than  10 HP, heal all damage)'
        elif int(ans) == 5 :
            name = "Orc"
            health = 48
            strength = 5
            dexterity = 2
            defence = 2
            speed = 2
            mana = 2
            magic_discription = '(Deal 18 damage)'
            p_attack = '(+1 to each stat)'
        elif int(ans) == 6 :
            name = "Wyvern"
            health = 40
            strength = 3
            dexterity = 4
            defence = 1
            speed = 2
            mana = 6
            magic_discription = '(fly in air, longer stay, more damage 20+5x)'
            p_attack = '(Heal all damage)'
        if double == True and FirstSelected == False :
            FirstSelected = True
            choose_fighter()
   #goes in choose_fighter         #name,strength,speed,health,defence,dexterity,mana,magic_discription,p_attack
def choose_fighter() :
    global FirstSelected, ans, lose, speed, strength, health, name, defence, p_attack, dexterity, max_health, mana, magic_discription
    print('Choose your fighter:')
    print('1 = Swordmaster str: +2  spd: +7  HP: 40    def: +1   dex: +3')
    print('2 = Knight      str: +3  spd: -1  HP: 38    def: +6   dex: -1')
    print('3 = Wizard      str: +6  spd: +2  HP: 35    def: 0    dex: +3')
    print('4 = Prince      str: 1-9 spd: 1-8 HP: 30-42 def: +1-6 dex: +0,5')
    print('5 = Princess    str: -4  spd: +5  HP: 70    def: +2   dex: +1')
    print('6 = Archer      str: +2  spd: +4  HP: 25    def: +1   dex: +10')
    print('7 = Berserker   str: +2  spd: +1  HP: 50    def: 0    dex: 0 +str,-def at 1/2 HP')
    print('8 = Zombie      str: +3  spd: +5  HP: 35    def: 0    dex: +4 cannot die')
    print('9 = Overlord    str: __  spd: __  HP: __    def: __   dex: __ choose your stats')
    print('0 = Gladiator Mode fighters')
    ans = input()
    try :
        int(ans)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        choose_fighter()
    else :
        if int(ans) == 1:
            name = 'Swordmaster'
            strength = 2
            speed = 7
            health = 40
            defence = 1
            dexterity = 3
            mana = 2
            magic_discription = '(strength*6)'
            p_attack = '(damage taken last turn + 5)'
        elif int(ans) == 2:
            name = 'Knight'
            strength = 3
            speed = -1
            health = 35
            defence = 6
            dexterity = -1
            mana = 3
            magic_discription = '(copy opponent 5 less)'
            p_attack = '(+3 defence and 5-12 damage)'
        elif int(ans) == 3:
            name = 'Wizard'
            strength = 6
            speed = 2
            health = 35
            defence = 0
            dexterity = 3
            magic_discription = '(1 damage per mana used)'
            mana = 19
            p_attack = '(auto crit)'
        elif int(ans) == 4:
            name = 'Prince'
            strength = random.randint(1,9)
            speed = random.randint(1,8)
            health = random.randint(30,42)
            defence = random.randint(1,6)
            dexterity = random.randint(0,5)
            mana = random.randint(1,3)
            magic_discription = '(18 + strength)'
            print('str: ' + str(strength) + '  spd: ' + str(speed) + '  HP: ' + str(health) + '  defence: ' + str(defence))
            p_attack = '(change defense, strength and +5 health)'
        elif int(ans) == 5:
            name = 'Princess'
            strength = -4
            speed = 5
            health = 70
            defence = 2
            dexterity = 1
            mana = 1
            magic_discription = '(20 + strength)'
            p_attack = '(heal 25 damage)'
        elif int(ans) == 6:
            name = 'Archer'
            strength = 2
            speed = 4
            health = 25
            defence = 1
            dexterity = 10
            mana = 3
            magic_discription = '(shot 1-5 arrows 5 each)'
            p_attack = '(reset battle)'
        elif int(ans) == 7 :
            name = 'Berserker'
            strength = 2
            speed = 1
            health = 50
            max_health = 50
            defence = 0
            dexterity = 0
            mana = 4
            magic_discription = '(save from death once)'
            p_attack = '(Change health to strength 1:2)'
        elif int(ans) == 8 :
            name = 'Zombie'
            strength = 3
            speed = 5
            health = 35
            defence = 0
            dexterity = 4
            mana = 3
            magic_discription = '(life drain)'
            p_attack = '(change HP to 1)'
        elif int(ans) == 9 :
            name = 'Overlord'
            magic_discription = '(grows by 5 every time)'
            ol_points = 18
            print('Choose your stats (the rest will be health x5)')
            time.sleep(0.75)
            print('OL: ' + str(ol_points))
            time.sleep(0.75)
            print('Choose strength; -5,' + str(ol_points))
            ans = input()
            try :
                int(ans)
            except :
                print('That is not a number.')
                time.sleep(0.75)
                print('You will get 0 str')
                strength = 0
            else :
                if int(ans) <= ol_points and int(ans) >= -5 and int(ans) <= ol_points:
                    strength = ans
                    ol_points = int(ol_points) - int(ans)
                else :
                    print('You cannot use that amount')
                    time.sleep(0.75)
                    print('You will get 0 str')
                    strength = 0
            time.sleep(0.75)
            print('OL: ' + str(ol_points))
            print('Choose speed; -1,' + str(ol_points))
            ans = input()
            try :
                int(ans)
            except :
                print('That is not a number.')
                time.sleep(0.75)
                print('You will get 0 spd')
                speed = 0
            else :
                if int(ans) <= ol_points and int(ans) >= -1 and int(ans) <= ol_points:
                    speed = ans
                    ol_points = int(ol_points) - int(ans)
                else :
                    print('You cannot use that amount')
                    time.sleep(0.75)
                    print('You will get 0 spd')
                    speed = 0
            time.sleep(0.75)
            print('OL: ' + str(ol_points))
            print('Choose defence; -5,' + str(ol_points))
            ans = input()
            try :
                int(ans)
            except :
                print('That is not a number.')
                time.sleep(0.75)
                print('You will get 0 def')
                defence = 0
            else :
                if int(ans) <= ol_points and int(ans) >= -5 and int(ans) <= ol_points:
                    defence = ans
                    ol_points = int(ol_points) - int(ans)
                else :
                    print('You cannot use that amount')
                    time.sleep(0.75)
                    print('You will get 0 def')
                    defence = 0
            print('OL: ' + str(ol_points))
            print('Choose dexterity; -5,10')
            ans = input()
            try :
                int(ans)
            except :
                print('That is not a number.')
                time.sleep(0.75)
                print('You will get 0 dex')
                dexterity = 0
            else :
                if int(ans) <= ol_points and int(ans) >= -5 and int(ans) <= 10:
                    dexterity = ans
                    ol_points = int(ol_points) - int(ans)
                else :
                    print('You cannot use that amount')
                    time.sleep(0.75)
                    print('You will get 0 dex')
                    dexterity = 0
            health = ol_points*5
            if health <= 0 :
                print('You died by lack of health')
                time.sleep(0.75)
                lose = lose +1
                print('Do you want to play again?   Wins: ' + str(win) + '  Loses: ' + str(lose))
                ans = input()
                if ans == 'yes' or 'y' :
                    start_game()
                else :
                    end_game()
            print('HP: ' + str(health))
            mana = 6
            p_attack = "(gain two turns of invincibility)"
        elif int(ans) == 10:
            global santa_time
            name = 'Santa'
            strength = 44
            speed = 18
            health = 1
            defence = 0
            dexterity = 0
            santa_time = santa_time +1
            p_attack = '(-1000-1000 damage)'
        elif int(ans) == 0:
            gladiator_fighters()
        elif int(ans) == random.randint(11,20):
            name = 'King'
            speed = 100
            health = 100
            defence = 100
            dexterity = 100
            mana = 1
            print('You chose the correct number. You will be the King')
            time.sleep(0.75)
            print('How much strength do you want?')
            strength = int(input())
            p_attack = '(2 damage + strength)'
        elif int(ans) == 99:
            name = 'Test'
            print('How much strength do you want?')
            strength = int(input())
            print('How much speed do you want?')
            speed = int(input())
            print('How much health do you want?')
            health = int(input())
            print('How much defense do you want?')
            defence = int(input())
            print('How much dexerity do you want?')
            dexterity = int(input())
            print('How much mana do you want?')
            mana = int(input())
            p_attack = '(2 damage + strength)'
        else:
            print('That is not an option, you will be a footsoldier')
            name = 'Footsoldier'
            strength = -1
            speed = -1
            health = 25
            defence = 0
            dexterity = 1
            mana = 3
            p_attack = '(heal 10 damage, deal 1-20 damage)'
        if journey == 1 :
            max_health = health
            next_battle()
        if double == True and FirstSelected == False :
            FirstSelected = True
            choose_fighter()

def YourAttack() :
    global firstTurn
    if firstTurn :
        time.sleep(0.75)
        print('You are going first')
        firstTurn = False
    choose_move()
    time.sleep(0.75)
    print_health()
    if mon_health <= 0:
        beat_mon()

def MonsterAttack() :
    global firstTurn, focus, health
    if firstTurn :
        time.sleep(0.75)
        print('The ' + str(monster) + ' is going first')
        firstTurn = False
    if crazy == 1 :
        crazy_mon_miss()
    else :
        monster_attacks()
    time.sleep(0.75)
    print_health()
    if health <= 0 :
        if name == 'Zombie' :
            DetermineTurn()
        elif focus >= 1 :
            print('You clung on to life')
            health = 1
            print_health()
            focus = focus - 1
            DetermineTurn()
        else :
            die()

def DetermineTurn() :
    global MonsterTurn, YourTurn, yourSpeed, monsterSpeed
    if firstTurn :
        yourSpeed = 10 - speed
        monsterSpeed = 10 - mon_speed
        YourTurn = yourSpeed
        MonsterTurn = monsterSpeed
    if YourTurn > MonsterTurn :     #if monster is faster
        MonsterTurn += mon_speed    
        MonsterAttack()             #monster attacks
    else :                          #if you are faster
        YourTurn += yourSpeed
        YourAttack()                #you attack
    
        
def first_turn() :
    global f, monster, health, mon_health
    time.sleep(0.75)
    print('You will battle a ' + str(monster))
    first = int(random.randint(1,20)) + int(speed) - int(random.randint(1,20)) + int(horse)
    if double :
        pass
    if crazy == 1 :
        f = 0
        time.sleep(0.75)
        print('The ' + str(monster) + ' is going first')
        crazy_mon_miss()
        time.sleep(0.75)
        print(str(name) + ' HP: ' + str(health))
        print(str(monster) + ' HP: ' + str(mon_health))
        if health <= 0 :
            if name == 'Zombie' :
                update()
            else :
                die()
    elif speed_add :
        DetermineTurn()
    elif first > 1:
        f = 1
        time.sleep(0.75)
        print('You are going first.')
        choose_move()
        time.sleep(0.75)
        print(str(name) + ' HP: ' + str(health))
        print(str(monster) + ' HP: ' + str(mon_health))
        if int(shields) >= 1 :
            print('shield HP: ' + str(shields))
        if mon_health <= 0:
            beat_mon()
    else:
        f = 0
        time.sleep(0.75)
        print('The ' + str(monster) + ' is going first')
        monster_attacks()
        time.sleep(0.75)
        print(str(name) + ' HP: ' + str(health))
        print(str(monster) + ' HP: ' + str(mon_health))
        if int(shields) >= 1 :
            print('shield HP: ' + str(shields))
        if health <= 0 :
            if name == 'Zombie' :
                update()
            else :
                die()

def crazy_mon_miss() :
    global damage, arc, health, shield, temp_health, mon_damage, shields, invinc, mon_strength, b_mode, strength, br_shield, mon_health
    if int(ans) == 6 :
        arc = int(random.randint(1,3))
        if int(arc) == 3 :
            action = int(random.randint(1,7))
            if int(action) == 1 :
                time.sleep(0.75)
                print('The ' + str(monster) + ' fell on its face.')
            elif int(action) == 2 :
                time.sleep(0.75)
                print('The ' + str(monster) + ' got distracted by a butterfly.')
            elif int(action) == 3 :
                time.sleep(0.75)
                print('The ' + str(monster) + ' forgot its turn.')
            elif int(action) == 4 :
                damage = int(random.randint(1,4)) + int(mon_strength)
                mon_health = mon_health - damage
                time.sleep(0.75)
                print('The ' + str(monster) + ' attacked itself. (' + str(damage) + ' damage)') 
            elif int(action) == 5 :
                damage = int(random.randint(1,10))
                mon_health = mon_health - damage
                time.sleep(0.75)
                print('The ' + str(monster) + ' got ran over by a boulder. (' + str(damage) + ' damage)')
            elif int(action) == 6 :
                time.sleep(0.75)
                print('The ' + str(monster) + ' decided to code this game instead of attack.')
                time.sleep(0.75)
                print('So they got 5 health.')
                mon_health = mon_health + 5
            elif int(action) == 7 :
                damage = health - 1
                health = 1
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
        elif int(arc) == 2 :
            time.sleep(0.75)
            print('The ' + str(monster) + ' missed.')
        elif int(arc) == 1 :
            mon_damage = int(random.randint(1,20)) 
            damage_s = int(mon_damage) - int(defence) - int(shield) + int(mon_strength)*int(buy_modifier) - int(armor)
            damage = int(damage_s) - int(shields)
            if int(shields) != 0 :
                br_shield = 1
                shields = int(shields) - int(damage_s)
            if int(mon_damage) == 1 :
                time.sleep(0.75)
                print('The ' + str(monster) + ' missed.')
            elif int(damage) <= 0 and int(use_move) == 4 :
                time.sleep(0.75)
                print('You blocked the attack.')
                shield = 0
            elif int(damage) <= 0 :
                time.sleep(0.75)
                print('The ' + str(monster) + ' failed to hurt you.')
            elif int(invinc) == 1 :
                invinc = 0
                time.sleep(0.75)
                print('The ' + str(monster) + ' failed to hurt you')
            elif int(shields) >= 1 :
                time.sleep(0.75)
                print('You blocked the attack with your shield')    
            else :
                temp_health = health
                health = int(temp_health) - int(damage) 
                if int(shields) + int(damage_s) >= 1 and br_shield == 1 :
                    time.sleep(0.75)
                    print('Your shield broke')
                    shields = 0
                    br_shield = 0
                    time.sleep(0.75)
                    print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                else :
                    time.sleep(0.75)
                    print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                    shields = 0                        
    else :
        if crazy == 1 :
            action = int(random.randint(1,15))
            if int(action) == 1 :
                time.sleep(0.75)
                print('The ' + str(monster) + ' fell on its face.')
            elif int(action) == 2 :
                time.sleep(0.75)
                print('The ' + str(monster) + ' got distracted by a butterfly.')
            elif int(action) == 3 :
                time.sleep(0.75)
                print('The ' + str(monster) + ' forgot its turn.')
            elif int(action) == 4 :
                damage = int(random.randint(1,4)) + int(mon_strength)
                mon_health = mon_health - damage
                time.sleep(0.75)
                print('The ' + str(monster) + ' attacked itself. (' + str(damage) + ' damage)')
            elif int(action) == 5 :
                damage = int(random.randint(1,8)) + int(mon_strength)
                mon_health = mon_health - damage
                time.sleep(0.75)
                print('The ' + str(monster) + ' got ran over by a boulder. (' + str(damage) + ' damage)')
            elif int(action) == 6 :
                time.sleep(0.75)
                print('The ' + str(monster) + ' decided to code this game instead of attack.')
                time.sleep(0.75)
                print('So they got 5 health.')
                mon_health = mon_health + 5
            else :
                mon_damage = int(random.randint(1,20))
                damage_s = int(mon_damage) - int(defence) - int(shield) + int(mon_strength)*int(buy_modifier) - int(armor)
                damage = int(damage_s) - int(shields)
                if int(shields) != 0 :
                    br_shield = 1
                    shields = int(shields) - int(damage_s)
                if int(mon_damage) == 1 :
                    time.sleep(0.75)
                    print('The ' + str(monster) + ' missed.')
                elif int(shields) >= 1 :
                    print('You blocked the attack with your shield')
                elif damage <= 0 and int(use_move) == 4 :
                    time.sleep(0.75)
                    print('You blocked the attack.')
                    shield = 0
                elif damage <= 0 :
                    time.sleep(0.75)
                    print('The ' + str(monster) + ' failed to hurt you.')
                elif int(invinc) == 1 :
                    invinc = 0
                    time.sleep(0.75)
                    print('The ' + str(monster) + ' failed to hurt you')
                else :
                    temp_health = health
                    health = int(temp_health) - int(damage)
                    if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                        time.sleep(0.75)
                        print('Your shield broke')
                        shields = 0
                        br_shield = 0
                        time.sleep(0.75)
                        print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                        if name == 'Berserker' and int(health) <= max_health/2 and int(b_mode) == 0 :
                            print('You entered berserk mode; +10 str -8 def')
                            strength = strength + 10
                            mon_strength = mon_strength + 8
                            b_mode = 1
                    else :
                        time.sleep(0.75)
                        print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                        shields = 0
                        if name == 'Berserker' and int(health) <= max_health/2 and int(b_mode) == 0 :
                            print('You entered berserk mode; +10 str -8 def')
                            strength = strength + 10
                            mon_strength = mon_strength + 8
                            b_mode = 1
    if ability_add :
        CheckAbility('MonsterTurn', mon_damage)
'''                
def m1_f() :         
    turn_list = []
    time.sleep(0.75)
    print('The ' + str(monster) + ' is attacking')
    turn_list.append("m1")
    m1_attack()
    time.sleep(0.75)
    print('The ' + str(monster_2) + ' is attacking')
    turn_list.append("m2")
    m2_attack()
            
def m2_f() :            
    turn_list = []
    time.sleep(0.75)
    print('The ' + str(monster_2) + ' is attacking')
    turn_list.append("m2")
    m2_attack()
    time.sleep(0.75)
    print('The ' + str(monster) + ' is attacking')
    turn_list.append("m1")
    m1_attack()
    
def p1_f() :
    turn_list = []
    time.sleep(0.75)
    print("Player 1's turn")
    turn_list.append("p1")
    p1_attack()
    time.sleep(0.75)
    print("Player 2's turn")
    turn_list.append("p2")
    p2_attack()

def p2_f() :
    turn_list = []
    time.sleep(0.75)
    print("Player 2's turn")
    turn_list.append("p2")
    p2_attack()
    time.sleep(0.75)
    print("Player 1's turn")
    turn_list.append("p1")
    p1_attack()

def first_turn_2() :
    global f, health, mon_health, health_2, mon_health_2
    turn_list = []
    print('You will battle a ' + str(monster) + ' and a ' + str(monster_2))
    m1_first = int(random.randint(1,20))
    m2_first = int(random.randint(1,20))
    p1_first = int(random.randint(1,20)) + int(speed)
    p2_first = int(random.randint(1,20)) + int(speed_2)
    if int(m1_first) + int(m2_first) > int(p1_first) + int(p2_first) :
        if int(m1_first) > int(m2_first) :
            m1_f()
            if int(p1_first) > int(p2_first) :
                p1_f()    
            else:
                p2_f()    
        else :
            m2_f()
            if int(p1_first) > int(p2_first) :
                p1_f()
            else:
                p2_f()
    else:
        if int(p1_first) > int(p2_first) :
            p1_f()
            if int(m1_first) > int(m2_first) :
                m1_f()
            else:
                m2_f()
        else :
            p2_f()
            if int(m1_first) > int(m2_first) :
                m1_f()
            else:
                m2_f()

        f = 1
        time.sleep(0.75)
        print('You are going first')
        choose_move()
        time.sleep(0.75)
        print(str(name) + ' HP: ' + str(health))
        print(str(monster) + ' HP: ' + str(mon_health))
        if int(shields) >= 1 :
            print('shield HP: ' + str(shields))
        if mon_health <= 0:
            beat_mon()
        
        f = 0
        time.sleep(0.75)
        print('The ' + str(monster) + ' is going first')
        check_mon_miss()
        time.sleep(0.75)
        print(str(name) + ' HP: ' + str(health))
        print(str(monster) + ' HP: ' + str(mon_health))
        if int(shields) >= 1 :
            print('shield HP: ' + str(shields))
        if health <= 0 :
            if name == 'Zombie' :
                update()
            else :
                die()            

def p1_attack() :
    global damage, mon_health
    if mon_health >= 1 and mon_health_2 >= 1 :
        print('Who do you want to attack 1 = ' + str(monster) + ' 2 = ' + str(monster_2))
        if int(input()) == 1 :
            if damage <= 0 :
                time.sleep(0.75)
                print('You missed')
            elif damage - int(strength) - int(sword) <= 1 :
                time.sleep(0.75)
                print('You missed')
            else :
                temp_mon_health = mon_health
                mon_health = int(temp_mon_health) - int(damage)
                time.sleep(0.75)
                print('You dealt ' + str(damage) + ' damage')
        else :
            if damage_2 <= 0 :
                time.sleep(0.75)
                print('You missed')
            elif damage_2 - int(strength) - int(sword) <= 1 :
                time.sleep(0.75)
                print('You missed')
            else :
                temp_mon_health = mon_health_2
                mon_health_2 = int(temp_mon_health) - int(damage)
                time.sleep(0.75)
                print('You dealt ' + str(damage) + ' damage')
    
    

def p2_attack() :
    global damage, mon_health
    if damage <= 0 :
        time.sleep(0.75)
        print('You missed')
    elif damage - int(strength) - int(sword) <= 1 :
        time.sleep(0.75)
        print('You missed')
    else :
        temp_mon_health = mon_health
        mon_health = int(temp_mon_health) - int(damage)
        time.sleep(0.75)
        print('You dealt ' + str(damage) + ' damage')
'''
                
def ready_check_win() :
    global alive, done
    if mon_health <= 0:
        alive = False
        print('A')
    elif health <= 0 :
        if name == 'Zombie' :
            alive = True
        else :
            alive = False
    if crazy == 1 :
        crazy_miss()
    else :
        check_miss()
    done = True
                
def check_win() :
    global health, focus, f
    if mon_health <= 0:
        beat_mon()
    elif health <= 0 :
        if name == 'Zombie' :
            update()
        elif focus >= 1 :
            print('You clung on to life')
            health = 1
            print(str(name) + ' HP: ' + str(health))
            print(str(monster) + ' HP: ' + str(mon_health))
            if int(shields) >= 1 :
                print('shield HP: ' + str(shields))
            focus = focus - 1
            f = 0
            update()
        else :
            die()
    else :
        update()
        
def check_miss() :
    if alive == True :
        global damage, mon_health, crit, mon_dext
        hit = int(random.randint(1,20)) + int(dexterity) - int(mon_dext)
        crit = int(random.randint(1,5))
        if ability_add :
            if 'crit' == str(CheckAbility('YourTurn', 0)) :
                crit = 5
            if int(CheckAbility('YourTurn', 0)) == 5 :
                damage += 5
        if hit <= 1 :
            time.sleep(0.75)
            print('The ' + str(monster) + ' dodged your attack')        
        elif crit == 5 :
            crit = 2
            time.sleep(0.75)
            print('You got a critical hit')
            temp_mon_health = mon_health
            mon_health = int(temp_mon_health) - int(damage)*crit
            time.sleep(0.75)
            print('You dealt ' + str(damage*crit) + ' damage')
        elif damage <= 0 :
            time.sleep(0.75)
            print('You missed')
        elif damage - int(strength) - int(sword) <= 1 :
            time.sleep(0.75)
            print('You missed')
        else :
            temp_mon_health = mon_health
            mon_health = int(temp_mon_health) - int(damage)
            time.sleep(0.75)
            print('You dealt ' + str(damage) + ' damage')

def check_for_crazy_miss() :
    if crazy == 1 :
        crazy_miss()
    else :
        check_miss()
            
def crazy_miss() :
    global damage, mon_health, health
    if damage <= 0 :
        time.sleep(0.75)
        print('You failed to reach the ' + str(monster))
    elif damage - int(strength) - int(sword) <= 1 :
        time.sleep(0.75)
        print('You missed')
    else :
        action = int(random.randint(1,15))
        if int(action) == 1 :
            time.sleep(0.75)
            print('You fell on your face.')
        elif int(action) == 2 :
            time.sleep(0.75)
            print('You got distracted by a butterfly.')
        elif int(action) == 3 :
            time.sleep(0.75)
            print('You forgot your turn.')
        elif int(action) == 4 :
            damage = int(random.randint(1,4)) + int(strength)
            time.sleep(0.75)
            print('You attacked yourself. (' + str(damage) + ' damage)')
            health = health - damage
        elif int(action) == 5 :
            damage = int(random.randint(1,10))
            time.sleep(0.75)
            print('You got ran over by a boulder. (' + str(damage) + ' damage)')
            health = health - damage
        elif int(action) == 6 :
            time.sleep(0.75)
            print('You decided to sleep in')
        elif int(action) == 7 :
            time.sleep(0.75)
            print('Bonus!')
            bonus = int(random.randint(5,30))
            time.sleep(0.75)
            print('You got a bonus of ' + str(bonus) + ' damage')
            temp_mon_health = mon_health
            mon_health = int(temp_mon_health) - int(damage) - int(bonus)
            time.sleep(0.75)
            print('You dealt ' + str(damage + bonus) + ' damage')
        elif int(action) == 8 :
            time.sleep(0.75)
            print('You got a critical hit')
            temp_mon_health = mon_health
            mon_health = int(temp_mon_health) - int(damage)
            time.sleep(0.75)
            print('You dealt ' + str(damage*2) + ' damage')
        else :
            temp_mon_health = mon_health
            mon_health = int(temp_mon_health) - int(damage)
            time.sleep(0.75)
            print('You dealt ' + str(damage) + ' damage')        

def m_basic() :
    global mon_damage, mon_attacked
    if mon == 8 :
        fire = random.randint(1,20)
        time.sleep(0.75)
        if int(fire) < 8 :
            print('The Dragon breathed red fire.')
            mon_damage = int(fire) + int(mon_strength)
        elif int(fire) > 7 and int(fire) < 15 :
            print('The Dragon breathed black fire.')
            mon_damage = random.randint(1,35)
        elif int(fire) > 14 and int(fire) < 19 :
            print('The Dragon breathed blue fire.')
            mon_damage = int(fire) + int(mon_strength)
        else :
            print('The Dragon breathed gold fire.')
            mon_damage = int(fire) + int(mon_strength) + int(defence)
    else :
        mon_damage = random.randint(1,20) + int(mon_strength)
    mon_attacked = True

def m_sure() :
    global mon_damage, mon_attacked
    '''
    if mon = '9' :
        time.sleep(0.75)
        print('The Wyvern flew up preparing to dive')
    '''
    mon_damage = 10 + int(mon_strength)
    mon_attacked = True

def m_power() :
    global mon_damage, mp_used, mon_attacked
    if int(mon) == '8' :
        time.sleep(0.75)
        print('The Dragon swung its tail at you.')
        dodge = random.randint(1,20) + int(dexterity)
        if int(dodge) > 19 :
            time.sleep(0.75)
            print('You dodged the attack')
        elif int(dodge) > 14 :
            mon_damage = random.randint(5,25) + int(mon_strength)
        else :
            mon_damage = random.randint(10,35) + int(mon_strength)
    else :
        mon_damage = random.randint(10,30) + int(mon_strength)
        time.sleep(0.75)
        print('The ' + str(monster) + ' used its power move.')
    mp_used = True
    mon_attacked = True

def choose_mon_move() :
    if mp_used == True :
        move = random.randint(1,2)
        if move == 2 or health == 20 + int(mon_strength)*2 - int(defence)*2 or health <= 10 + int(mon_strength) - int(defence) :
            m_sure()
        else :
            m_basic()
    else :
        move = random.randint(1,5)
        if move == 1 or health == 20 + int(mon_strength)*2 - int(defence)*2  or health <= 10 + int(mon_strength) - int(defence) :
            m_sure()
        elif move == 2 :
            m_basic()
        else :
            m_power()
    check_mon_miss()

def monster_attacks() :
    if ai == True :
        choose_mon_move()
    elif crazy == 1 :
        crazy_mon_miss()
    else :
        check_mon_miss()
    
def check_mon_miss() :
    global damage, arc, health, shield, temp_health, mon_damage, shields, invinc, mon_strength, b_mode, strength, br_shield, crit, mon_dext
    hit = int(random.randint(1,20)) - int(dexterity) + int(mon_dext)
    crit = int(random.randint(1,5))
    if crit == 5 :
        crit = 2
    if ai == False :
        mon_damage = int(random.randint(1,20))
    damage_s = int(mon_damage) - int(defence) - int(shield) + int(mon_strength)*int(buy_modifier) - int(armor)
    damage = int(damage_s) - int(shields)
    if int(shields) != 0 :
        br_shield = 1
        shields = int(shields) - int(damage_s)
    if int(mon_damage) == 1 :
        time.sleep(0.75)
        print('The ' + str(monster) + ' missed.')
    elif int(shields) >= 1 :
        print('You blocked the attack with your shield')
    elif damage <= 0 and int(use_move) == 4 :
        time.sleep(0.75)
        print('You blocked the attack.')
        shield = 0
    elif hit <= 1 :
        time.sleep(0.75)
        print('You dodged the ' + str(monster) + "'s attack")
    elif damage <= 0 :
        time.sleep(0.75)
        print('The ' + str(monster) + ' failed to hurt you.')
    elif int(invinc) == 1 :
        invinc = 0
        time.sleep(0.75)
        print('The ' + str(monster) + ' failed to hurt you')
    else :
        temp_health = health
        if crit != 2 :
            health = int(temp_health) - int(damage)
            if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                time.sleep(0.75)
                print('Your shield broke')
                shields = 0
                br_shield = 0
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                if name == 'Berserker' and int(health) <= max_health/2 and int(b_mode) == 0 :
                    print('You entered berserk mode; +10 str -8 def')
                    strength = strength + 10
                    mon_strength = mon_strength + 8
                    b_mode = 1
            else :
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                shields = 0
                if name == 'Berserker' and int(health) <= max_health/2  and int(b_mode) == 0 :
                    print('You entered berserk mode; +10 str -8 def')
                    strength = strength + 10
                    mon_strength = mon_strength + 8
                    b_mode = 1
        else :
            time.sleep(0.75)
            print('The ' + str(monster) + ' got a critical hit')
            health = int(temp_health) - int(damage)*crit
            if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                time.sleep(0.75)
                print('Your shield broke')
                shields = 0
                br_shield = 0
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage*crit) + ' damage')
                if name == 'Berserker' and int(health) <= max_health/2 and int(b_mode) == 0 :
                    print('You entered berserk mode; +10 str -8 def')
                    strength = strength + 10
                    mon_strength = mon_strength + 8
                    b_mode = 1
            else :
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage*crit) + ' damage')
                shields = 0
                if name == 'Berserker' and int(health) <= max_health/2 and int(b_mode) == 0 :
                    print('You entered berserk mode; +10 str -8 def')
                    strength = strength + 10
                    mon_strength = mon_strength + 8
                    b_mode = 1
    if ability_add :
        CheckAbility('MonsterTurn', mon_damage)                 
def ready_attack() :
    global damage, health, shield, temp_health, mon_damage, shields, invinc, mon_strength, b_mode, br_shield, strength, crit
    time.sleep(0.75)
    print('You are readying your attack')
    hit = int(random.randint(1,20)) - int(dexterity) + int(mon_dext)
    crit = int(random.randint(1,5))
    if crit == 5 :
        crit = 2
    mon_damage = int(random.randint(1,20))
    damage_s = int(mon_damage) - int(defence) - int(shield) + int(mon_strength)*int(buy_modifier) - int(armor)
    damage = int(damage_s) - int(shields)
    if int(shields) != 0 :
        br_shield = 1
        shields = int(shields) - int(damage_s)
    if int(mon_damage) == 1 :
        time.sleep(0.75)
        print('The ' + str(monster) + ' missed.')
    elif hit <= 1 :
        time.sleep(0.75)
        print('You dodged the ' + str(monster) + "'s attack")
    elif int(shields) >= 1 :
        time.sleep(0.75)
        print('You blocked the attack with your shield')
    elif damage <= 0 :
        time.sleep(0.75)
        print('The ' + str(monster) + ' failed to hurt you.')
    elif int(invinc) == 1 :
        invinc = 0
        time.sleep(0.75)
        print('The ' + str(monster) + ' failed to hurt you')
    else :
        temp_health = health
        if crit != 2 :
            health = int(temp_health) - int(damage)
            if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                time.sleep(0.75)
                print('Your shield broke')
                shields = 0
                br_shield = 0
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                if name == 'Berserker' and int(health) <= max_health/2 and int(b_mode) == 0 :
                    print('You entered berserk mode; +10 str -8 def')
                    strength = strength + 10
                    mon_strength = mon_strength + 8
                    b_mode = 1
            else :
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                shields = 0
                if name == 'Berserker' and int(health) <= max_health/2 and int(b_mode) == 0 :
                    print('You entered berserk mode; +10 str -8 def')
                    strength = strength + 10
                    mon_strength = mon_strength + 8
                    b_mode = 1
        else :
            time.sleep(0.75)
            print('The ' + str(monster) + ' got a critical hit')
            health = int(temp_health) - int(damage)*crit
            if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                time.sleep(0.75)
                print('Your shield broke')
                shields = 0
                br_shield = 0
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage*crit) + ' damage')
                if name == 'Berserker' and int(health) <= max_health/2 and int(b_mode) == 0 :
                    print('You entered berserk mode; +10 str -8 def')
                    strength = strength + 10
                    mon_strength = mon_strength + 8
                    b_mode = 1
            else :
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage*crit) + ' damage')
                shields = 0
                if name == 'Berserker' and int(health) <= max_health/2 and int(b_mode) == 0 :
                    print('You entered berserk mode; +10 str -8 def')
                    strength = strength + 10
                    mon_strength = mon_strength + 8
                    b_mode = 1

        if health >= 1 :
            time.sleep(0.75)
            print(str(name) + ' HP: ' + str(health))
            print(str(monster) + ' HP: ' + str(mon_health))
            if int(shields) >= 1 :
                print('shield HP: ' + str(shields))
            if mon_health <= 0:
                beat_mon()
            elif health <= 0 :
                if name == 'Zombie' :
                    update()
                else :
                    die()

def move_1() :
    global damage
    if name == 'Swordmaster' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Knight' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Wizard' :
        damage = int(random.randint(-1,22)) + int(strength) + int(sword)
    elif name == 'Prince' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Princess' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Archer' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Berserker' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Zombie' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Overlord' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Gladiator' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Dragon' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Goblin' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Troll' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Orc' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Wyvern' :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    elif name == 'Santa' :
        damage = int(random.randint(1,10)) + int(strength) + int(sword)
    elif name == 'King' :
        damage = 2 + int(strength) + int(sword)                   
    elif name == 'Test' :
        damage = 2 + int(strength) + int(sword)       
    else :
        damage = int(random.randint(1,20)) + int(strength) + int(sword)
    check_for_crazy_miss()       
            
def move_2() :
    global damage, defence, arc, health, shield, temp_health, mon_damage, invinc, shields, br_shield, crit, done
    done = False
    while alive == True and done == False :
        if name == 'Swordmaster' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Knight' :
            defence = defence + 2
            ready_attack()
            damage = int(random.randint(15,26)) + int(strength) + int(sword)
            ready_check_win()
            defence = defence - 2
        elif name == 'Wizard' :
            ready_attack()
            damage = int(random.randint(12,40)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Prince' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Princess' :
            ready_attack()
            damage = int(random.randint(15,28)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Archer' :
            time.sleep(0.75)
            print('You are readying your attack')
            hit = int(random.randint(1,20)) - dexterity + mon_dext
            crit = int(random.randint(1,5))
            if crit == 5 :
                crit = 2
            temp_health = health
            if crit != 2 :
                health = int(temp_health) - int(damage)
                if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                    time.sleep(0.75)
                    print('Your shield broke')
                    shields = 0
                    br_shield = 0
                    time.sleep(0.75)
                    print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                else :
                    time.sleep(0.75)
                    print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                    shields = 0
            else :
                time.sleep(0.75)
                print('The ' + str(monster) + ' got a critical hit')
                health = int(temp_health) - int(damage)*crit
                if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                    time.sleep(0.75)
                    print('Your shield broke')
                    shields = 0
                    br_shield = 0
                    time.sleep(0.75)
                    print('The ' + str(monster) + ' dealt ' + str(damage*crit) + ' damage')

                else :
                    time.sleep(0.75)
                    print('The ' + str(monster) + ' dealt ' + str(damage*crit) + ' damage')
                    shields = 0
            time.sleep(0.75)
            print(str(name) + ' HP: ' + str(health))
            print(str(monster) + ' HP: ' + str(mon_health))
            if int(shields) >= 1 :
                print('shield HP: ' + str(shields))
            damage = int(random.randint(5,25)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Berserker' :
            ready_attack()
            damage = int(random.randint(28,35)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Zombie' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Overlord' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Gladiator' :
            ready_attack()
            damage = int(random.randint(25,35)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Dragon' :
            ready_attack()
            damage = int(random.randint(18,32)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Goblin' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Troll' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Orc' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Wyvern' :
            ready_attack()
            damage = int(random.randint(10,40)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'Santa' :
            ready_attack()
            damage = int(random.randint(100,200)) + int(strength) + int(sword)
            ready_check_win()
        elif name == 'King' :
            ready_attack()
            damage = 2 + int(strength) + int(sword)            
            ready_check_win()
        elif name == 'Test' :
            ready_attack()
            damage = 2 + int(strength) + int(sword)
            ready_check_win()
        else :
            ready_attack()
            damage = int(random.randint(20,30)) + int(strength) + int(sword)
            ready_check_win()
            
def move_3() :
    global damage, power_move, strength, speed, defence, health, shields, mon_strength, b_mode, name, mon_health, dexterity
    if power_move == 0 :
        power_move = 1
        if name == 'Swordmaster' :
            if damage == 0 :
                damage = 15
            if crit == 2 :
                damage = int(damage)*2 + 3 + int(strength) + int(sword)    
            else :
                damage = int(damage) + 3 + int(strength) + int(sword)
            check_for_crazy_miss()
        elif name == 'Knight' :
            damage = int(random.randint(2,7)) + int(strength) + int(sword)
            defence = defence + 3
            check_for_crazy_miss()
        elif name == 'Wizard' :
            damage = int(random.randint(1,20)) + int(strength)*2 + int(sword)
            time.sleep(0.75)
            print('You got a critical hit')
            temp_mon_health = mon_health
            mon_health = int(temp_mon_health) - int(damage)*2
            time.sleep(0.75)
            print('You dealt ' + str(damage*2) + ' damage')
        elif name == 'Prince' :
            strength = random.randint(2,10)
            health = health + 5
            defence = random.randint(2,7)
            print('str: ' + str(strength) + '  HP: ' + str(health) + '  defence: ' + str(defence))
            damage = int(random.randint(1,20)) + int(strength) + int(sword)
            check_for_crazy_miss()
        elif name == 'Princess' :
            health = health + 25
            print('You healed 25 damage')
        elif name == 'Archer' :
            health = 25
            mon_health = 30 + int(mon_strength)*2
        elif name == 'Berserker' :
            print('How much health do you want to convert(round down)')
            ans = input()
            try :
                int(ans)
            except :
                print('That is not a number.')
                time.sleep(0.75)
                move_3()
            else :
                strength = strength + int(ans)*2
                health = health - int(ans)
        elif name == 'Zombie' :
            health = 1
        elif name == 'Overlord' :
            global invinc
            invinc = 1
            time.sleep(0.75)
            print('You gained two turns of invincibility')
            time.sleep(0.75)
            print('The ' + str(monster) + ' failed to hurt you')
            choose_move()
        elif name == 'Gladiator' :
            damage = int(random.randint(20,30)) + int(strength) + int(sword)
            check_for_crazy_miss()
        elif name == 'Dragon' :
            print('You breathed gold fire.')
            fire = random.randint(15,20)
            damage = int(fire) + int(strength) + int(defence)
            check_for_crazy_miss()
        elif name == 'Troll' :
            if health < 11 :
                health = 60
                print('Healed all damage')
            else :
                print('*grunted')
        elif name == 'Orc' :
            strength += 1
            health += 5
            dexterity += 1
            defence += 1
        elif name == 'Wyvern' :
            health = 40
        elif name == 'Goblin' :
            damage = int(random.randint(1,20)) + int(strength)*2 + int(sword)
            time.sleep(0.75)
            print('You got a critical hit')
            temp_mon_health = mon_health
            mon_health = int(temp_mon_health) - int(damage)*2
            time.sleep(0.75)
            print('You dealt ' + str(damage*2) + ' damage')
        elif name == 'Santa' :
            time.sleep(0.75)
            print('Bomb')
            damage = int(random.randint(-1000,1000)) + int(strength) + int(sword)
            check_for_crazy_miss()
        elif name == 'King' :
            damage = 2 + int(strength) + int(sword)            
            check_for_crazy_miss()
        elif name == 'Test' :
            damage = 2 + int(strength) + int(sword)
            check_for_crazy_miss()
        else :
            health = health + 10
            print('You healed 10 damage')
            damage = int(random.randint(1,20)) + int(strength) + int(sword)
            check_for_crazy_miss()
    else :
        time.sleep(0.75)
        print('You have already used your power move.')
        choose_move()

def move_magic():        
    global fly, dexterity, health, focus, damage, mana, ol_charge, mon_strength, mon_health, mon_dex
    if mana > 0 :
        mana = mana - 1
        if name == 'Swordmaster' :
            damage = strength*6
            check_for_crazy_miss()
        elif name == 'Knight' :
            if damage == 0 :
                damage = 15 
            if crit == 2 :
                damage = int(damage)*2 - 10   
            else :
                damage = int(damage) - 5
            check_for_crazy_miss()
        elif name == 'Wizard' :
            mana = mana + 1
            print('Mana: ' + str(mana))
            time.sleep(0.75)
            print('How much mana do you want to use?')
            ans = input()
            try :
                int(ans)
            except :
                print('That is not a number.')
                time.sleep(0.75)
                move_magic()
            else :
                if int(ans) <= int(mana) :
                    mana = int(mana) - int(ans)
                    damage = int(ans) + int(strength) + int(sword)
                    check_for_crazy_miss()
                else :
                    time.sleep(0.75)
                    print('You do not have that amount')
                    choose_move()           
        elif name == 'Prince' :
            damage = 18 + int(strength) + int(sword)
            check_for_crazy_miss()
        elif name == 'Princess' :
            damage = 20 + int(strength) + int(sword)
            check_for_crazy_miss()
        elif name == 'Archer' : 
            arrows = random.randint(1,5)
            time.sleep(0.75)
            print('You fired ' + str(arrows) + ' arrows')
            damage = arrows*5 + int(strength) + int(sword)
            check_for_crazy_miss()
        elif name == 'Berserker' :
            focus = focus + 1
            time.sleep(0.75)
            print('You fortified yourself')
        elif name == 'Zombie' :
            damage = random.randint(2,10)
            heal = damage/2
            health = health + heal
            check_for_crazy_miss()
            time.sleep(0.75)
            print('You drained ' + str(damage) + ' life and healed ' + str(heal) + ' damage')
        elif name == 'Overlord' :
            ol_charge = ol_charge + 5
            damage = 5 + ol_charge + int(strength) + int(sword) 
            check_for_crazy_miss()
        elif name == 'Gladiator' :
            mon_strength -= 1
            mon_health -= 5
            mon_dex -= 1
        elif name == 'Dragon' :
            fire = random.randint(1,20)
            time.sleep(0.75)
            if int(fire) < 8 :
                print('You breathed red fire.')
                damage = int(fire) + int(strength)
            elif int(fire) > 7 and int(fire) < 15 :
                print('You breathed black fire.')
                damage = random.randint(1,35) 
            elif int(fire) > 14 and int(fire) < 19 :
                print('You breathed blue fire.')
                damage = int(fire) + int(strength)
            else :
                print('You breathed gold fire.')
                damage = int(fire) + int(strength) + int(defence)
            check_for_crazy_miss()
        elif name == 'Goblin' :
            dexterity += 4
        elif name == 'Troll' :
            damage = random.randint(1,10)
            health = health + (11 - damage)
            check_for_crazy_miss()
        elif name == 'Orc' :
            damage = 13 + int(strength)
            check_for_crazy_miss()
        elif name == 'Wyvern' :
            if fly == False :
                print('You flew into the air')
                damage = 20
            else :
                print('Do you want to stay in the air? ')
                ans = input()
                if ans == 'y' or 'yes' :
                    damage += 5
                    print('The',str(monster),'missed.')
                    choose_move()
                else :
                    print('You dove down')
                    check_for_crazy_miss()
        elif name == 'Santa' :
            time.sleep(0.75)
            print('Santa does not have magic')
        elif name == 'King' :
            health = health + 100
            time.sleep(0.75)
            print('The King healed 100 damage')
        elif name == 'Test' :
            time.sleep(0.75)
            print('You used 1 mana')
        else :
            damage = random.randint(1,30)
            check_for_crazy_miss()   
    else :
        time.sleep(0.75)
        print('You do not have any more mana')
        choose_move()
def block() :
    global damage, shield, defence, health
    if name == 'Swordmaster' :
        shield = int(random.randint(3,8))
        heal = int(random.randint(3,8))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Knight' :
        shield = int(random.randint(4,9))
        heal = int(random.randint(3,6))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Wizard' :
        shield = int(random.randint(1,11))
        heal = int(random.randint(1,10))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Prince' :
        shield = int(random.randint(4,13))
        heal = int(random.randint(3,7))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Princess' :
        shield = int(random.randint(2,7))
        heal = int(random.randint(5,13))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Archer' :
        shield = int(random.randint(5,13))
        heal = int(random.randint(2,4))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Berserker' :
        shield = int(random.randint(3,9))
        heal = int(random.randint(2,8))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Zombie' :
        shield = int(random.randint(1,4))
        heal = int(random.randint(8,15))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Overlord' :
        shield = int(random.randint(2,9))
        heal = int(random.randint(3,5))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Gladiator' :
        shield = int(random.randint(3,8))
        heal = int(random.randint(3,8))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Dragon' :
        shield = int(random.randint(5,10))
        heal = int(random.randint(6,10))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Goblin' :
        shield = int(random.randint(2,7))
        heal = int(random.randint(5,7))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Troll' :
        shield = int(random.randint(4,9))
        heal = int(random.randint(2,6))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Orc' :
        shield = int(random.randint(3,8))
        heal = int(random.randint(3,8))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Wyvern' :
        shield = int(random.randint(2,8))
        heal = int(random.randint(4,9))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif name == 'Santa' :
        shield = 0
        time.sleep(0.75)
        print('Santa cannot defend himself')
    elif name == 'King' :
        shield = 100
        heal = 100
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')      
    elif name == 'Test' :
        print('What shield do you want?')
        shield = input()
        heal = int(random.randint(3,10))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')        
    else :
        shield = int(random.randint(3,8))
        heal = int(random.randint(3,10))
        health = health + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')

def use_item() :
    if item >= 1 :
        print('What item do you want to use? 1 = bomb  2 = strength potion  3 = health potion  4 = invincible potion  5 = temporary shield  6 = use different move')
        ans = input()
        try :
            int(ans)
        except :
            print('That is not a number.')
            time.sleep(0.75)
            use_item()
        else :
            if int(ans) == 1 and int(bomb) >= 1 :
                use_bomb()
            elif int(ans) == 2 and int(str_pot) >= 1 :
                use_str_pot() 
            elif int(ans) == 3 and int(heal_pot) >= 1 :
                use_heal_pot()
            elif int(ans) == 4 and int(invincible_pot) >= 1 :
                use_invincible_pot()
            elif int(ans) == 5 and int(temp_shield) >= 1 :
                use_temp_shield() 
            elif int(ans) == 6 :
                choose_move()
            else :
                print('You do not have any')
                use_item()
    else : 
        print('You do not have any items')
        choose_move()

def use_bomb() :
    global bomb, item
    bomb = bomb - 1
    item = item - 1
    damage = random.randint(-5,70)
    time.sleep(0.75)
    print('You used a bomb')
    if crazy == 1 :
        crazy_miss()
    else :
        check_miss()

def use_str_pot() :
    global str_pot, item, strength
    str_pot = str_pot - 1
    item = item - 1
    strength = strength +7
    time.sleep(0.75)
    print('You used a strength potion and gained +7 strength')
    
def use_heal_pot() :
    global health, item, heal_pot
    heal_pot = heal_pot - 1
    item = item - 1
    heal = random.randint(18,25)
    health = health + int(heal)
    time.sleep(0.75)
    print('You healed ' + str(heal) + ' damage')
    
def use_invincible_pot() :
    global invincible_pot, item, invinc
    invincible_pot = invincible_pot - 1
    item = item - 1
    invinc = 1
    time.sleep(0.75)
    print('You used a invincible potion and gained two turns of invincibility')
    time.sleep(0.75)
    print('The ' + str(monster) + ' failed to hurt you')
    choose_move()

def use_temp_shield() :    
    global shields, temp_shield, item
    shields = shields + 20 
    temp_shield = temp_shield - 1
    item = item - 1
    time.sleep(0.75)
    print('You used a temporary shield and gained 20 shield')

def turn_back_time() :
    if int(health) >= 0 :
        print('You mysteriously came back to life')
    else :
        print('Miraculously, time started going backward')
    health = temp_health
    time.sleep(0.75)
    choose_move()
    
def choose_move() :
    global use_move, shield
    shield = 0
    time.sleep(0.75)
    print('What move do you want? 7 = list of moves')
    use_move = input()
    if use_move == 'turn back time' :
        turn_back_time()
    try :
        int(use_move)
    except :
        print('That is not a number.')
        time.sleep(0.75)
        choose_move()
    else :
        if int(use_move) == 1 :
            move_1() 
        elif int(use_move) == 2 :
            move_2() 
        elif int(use_move) == 3 :
            move_magic()
        elif int(use_move) == 4 :
            move_3()
        elif int(use_move) == 5 :
            block()
        elif int(use_move) == 6 :
            use_item()
        elif int(use_move) == 7 :
            print('1 = normal attack 2 = charge attack 3 = magic move (mana: ' + str(mana) + ') ' + str(magic_discription) + ' 4 = power attack ' + str(p_attack) + ' 5 = defend 6 = use item')
            choose_move()
        else :
            print('That is not a move')
            time.sleep(0.75)
            choose_move()
        
def end_game() :
    global highscore
    point = gob_killed/2 + troll_killed*3/2 + orc_killed - lose*3 - santa_time + hp_points + hard
    if highscore < point :
        highscore = point
    if int(crazy) == 1 :
        print('Points: ' + str(point))
        time.sleep(0.75)
        print('Highscore: ' + str(highscore))
        time.sleep(0.75)
        print('Thanks for playing.')
    else :
        print('You killed ' + str(gob_killed) + ' goblins, ' + str(troll_killed) + ' trolls, and ' + str(orc_killed) + ' orcs' + '      Points: ' + str(point))
        time.sleep(0.75)
        print('Highscore: ' + str(highscore))
        time.sleep(0.75)
        sys.exit('Thanks for playing!')

def beat_mon() :
    global win, lose, gob_killed, troll_killed, orc_killed, hp_points
    time.sleep(0.75)
    print('You beat the ' + str(monster))
    time.sleep(0.75)
    hp_points = int(hp_points) - int(mon_health)/10 + int(health)/10
    win = win +1
    if journey == None :
        if mon == 1 :
            gob_killed = gob_killed +1
        elif mon == 2 :
            troll_killed = troll_killed +1
        elif mon == 3 :
            orc_killed = orc_killed +1
        print('Do you want to play again?   Wins: ' + str(win) + '  Loses: ' + str(lose))
        ans = input()
        if ans == 'yes' or 'y':
            start_game()
        else :
            end_game()
    else :
        time.sleep(0.75)
        if quest == 'gob' and gob_killed >= 4 :
            print('You achieved your quest.')
            time.sleep(0.75)
            print('Do you want to continue your journey?')
        elif quest == 'orc' and orc_killed >= 3 :
            print('You achieved your quest.')
            time.sleep(0.75)
            print('Do you want to continue your journey?')
        elif quest == 'tro' and troll_killed >= 2 :
            print('You achieved your quest.')
            time.sleep(0.75)
            print('Do you want to continue your journey?')
        elif quest == 'gob' and win >= 6 :
            print('You achieved your quest.')
            time.sleep(0.75)
            print('Do you want to continue your journey?')
        else :
            print('Do you want to continue your quest?')
        ans = input()
        if ans == 'yes' or ans == '' or ans == 'y' :
            journey_mode()
        else :
            end_game()
        
def die() :
    global lose
    time.sleep(0.75)
    print('You died')
    lose = lose +1
    if journey == None :
        time.sleep(0.75)
        print('Do you want to play again?   Wins: ' + str(win) + '  Loses: ' + str(lose))
        ans = input()
        if ans == 'yes' or 'y':
            start_game()
        elif ans == 'turn back time' :
            turn_back_time()
        else :
            end_game()
    else :
        time.sleep(0.75)
        print('You failed the quest, better luck next time.')
        time.sleep(0.75)
        print('Do you want to play again?   Wins: ' + str(win) + '  Loses: ' + str(lose))
        ans = input()
        if ans == 'yes' or 'y':
            start_game()
        elif ans == 'turn back time' :
            turn_back_time()
        else :
            end_game()

def print_health() :
    print(str(name) + ' HP: ' + str(health))
    print(str(monster) + ' HP: ' + str(mon_health))
    if int(shields) >= 1 :
        print('shield HP: ' + str(shields))
    
def update() :
    if speed_add :
        DetermineTurn()
    else :
        if ability_add :
            CheckAbility('StartTurn', 0)
        if crazy == 1 :
            choose_move()
            time.sleep(0.75)
            print_health()
            if mon_health >= 1:
                crazy_mon_miss()
                time.sleep(0.75)
                print_health()
        elif health >= 1 and mon_health >= 1:
            if f == 1:
                monster_attacks()
                time.sleep(0.75)
                print_health()
                if health >= 1 or name == 'Zombie' :
                    choose_move()
                    time.sleep(0.75)
                    print_health()
            else:
                choose_move()
                time.sleep(0.75)
                print_health()
                if mon_health >= 1:
                    monster_attacks()
                    time.sleep(0.75)
                    print_health()
        check_win()
    
def start_game() :
    choose_mode()
    choose_fighter()
    '''
    choose_fighter(name,strength,speed,health,defence,dexterity,mana,magic_discription,p_attack)
    if double :
        choose_fighter(name2,strength2,speed2,health2,defence2,dexterity2,mana2,magic_discription2,p_attack2)
    '''
    first_turn()
    update()
        
   #if int(two_p) == 1 :
        #first_turn_2()    

start_game()
