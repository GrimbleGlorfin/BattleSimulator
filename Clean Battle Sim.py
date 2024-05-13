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
shield = 0
use_move = 0
mon_damage = 0
power_move = 0
mon_strength = 0
crazy = 0
heal = 0
p_attack = 0
shields = 0
item = 0
damage_s = 0
invinc = 0
hp_points = 0
hard = 0
br_shield = 0
bonus = 0
action = 0
crit = 0
highscore = 0
hit = 0
mon_dext = 0
b_mode = 0
damage = 0
quest = 0
focus = 0
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
    global speed_add, b_mode, double, firstTurn, ability_add, crazy, shields, item, shield, power_move, bonus, action, crit, alive, done, journey, focus, ol_charge, ai, mp_used
    crazy = 0
    shields = 0
    item = 0
    shield = 0
    power_move = 0
    bonus = 0
    b_mode = 0
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
    global ability_add, speed_add, crazy, hard, journey, ai
    clear_stats()
    print('1 = easy mode  2 = hard mode  3 = crazy mode  4 = journey mode  5 = AI mode')
    if ability_add == False and speed_add == False : #always happens??
        print('7 = speed addition  8 = ability addition')
    elif not ability_add :
        print('8 = ability addition')
    elif not speed_add :
        print('7 = speed addition')       
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
            journey = 0
            journey_mode()
        elif int(ans) == 5 :
            ai = True
            AI_mode()
            #AI_mode(monster,mon_health,mon_strength,mon_dext,'''mon_def''',mon)
        elif int(ans) == 7 :
            speed_add = True
            choose_mode()
        elif int(ans) == 8 :
            ability_add = True
            choose_mode()
        else :
            choose_mon()

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
    global focus
    damage = int(damage)
    time = str(time)
    if player_stats['name'] == 'Swordmaster' and time == 'YourTurn' :
        crit = random.randint(1,20)
        if crit == 19 or crit == 20 :
            print('You got a critical hit.')
            return 'crit'
    elif player_stats['name'] == 'Knight' and time == 'StartTurn' :
        pitstop = random.randint(1,5)
        if pitstop > 3 :
            print('Your page repaired your armor, +3 def')
            player_stats['defense'] += 3
    elif player_stats['name'] == 'Wizard' and time == 'StartTurn' :
        if mon_health >= 30 :
            mana += 5
            print('You gained some mana, +5 mana')
    elif player_stats['name'] == 'Prince' and time == 'MonsterTurn' :
        if damage == 7 or damage == 17 or damage == 27 or damage == 37 :
            print('You absorbed that hit')
            player_stats['health'] += damage
    elif player_stats['name'] == 'Princess' and time == 'StartTurn' :
        if int(health) <= int(mon_health) :
            print('You evened the tables')
            newHP = mon_health - health
            player_stats['health'] += newHP
    elif player_stats['name'] == 'Archer' :
        pass
    elif player_stats['name'] == 'Berserker' and time == 'StartTurn' :
        constition = random.randint(1,5)
        if int(constition) == 5 :
            print('You feel refreshed and ready to face anything')
            focus += 1
    elif player_stats['name'] == 'Zombie' and time == 'StartTurn' :
        player_stats['health'] += 5
        print('You healed 5 HP')
        #print_health()
    elif player_stats['name'] == 'Overlord' :
        pass
    elif player_stats['name'] == 'Gladiator' :
        pass
    elif player_stats['name'] == 'Goblin' :
        pass
    elif player_stats['name'] == 'Dragon' and time == 'MonsterTurn' :
        if damage >= 35 :
            player_stats['health'] += 15
            print('Your scales reflected some of the damage')
    elif player_stats['name'] == 'Troll' :
        pass
    elif player_stats['name'] == 'Orc' and time == 'YourTurn' :
        if mon_health >= 30 :
            return 5
    elif player_stats['name'] == 'Wyvern' and time == 'MonsterTurn':
        dodge = random.randint(1,10)
        if dodge == 10 :
            print('You absorbed that hit')
            player_stats['health'] += damage
    else :
        return None
    
    
def journey_mode():
    global journey
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
    global power_move, mana, b_mode, mon_strength, focus
    if player_stats['name'] == 'Berserker' :
        b_mode = 0
        player_stats['strength'] = player_stats['strength'] - 10
        mon_strength = mon_strength - 8
    power_move = 0
    if player_stats['name'] == 'Wizard' :
        player_stats['mana'] += 10
    else :
        player_stats['mana'] += 1
    if player_stats['name'] == 'Knight' :
        player_stats['defense'] = player_stats['defense'] - 3
    player_stats['max_health'] = player_stats['max_health'] + 5
    player_stats['health'] = player_stats['max_health']
    print('You made it to the next camp and rested up.')
    
def add_stat() :
    global focus
    print('You leveled up')
    time.sleep(0.75)
    print('Which stat do you want to increase? str, spd, dex, HP, def or fortify self(for)')
    ans = input()
    if ans == 'str':
        player_stats['strength'] += 1        
    elif ans == 'spd':
        player_stats['speed'] += 1
    elif ans == 'dex':
        player_stats['dexterity'] += 1
    elif ans == 'def':
        player_stats['defense'] += 1
    elif ans == 'HP' :
        player_stats['max_health'] += 5
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
    global FirstSelected, lose
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
            player_stats['name'] = 'Gladiator'
            player_stats['strength'] = 3
            player_stats['speed'] = 1
            player_stats['health'] = 55
            player_stats['defense'] = 2
            player_stats['dexterity'] = 3
            player_stats['mana'] = 3
            player_stats['magic_discription'] = '(-1 to each opponent stat, 5 damage)'
            player_stats['p_attack'] = '(Deal 20-30 damage)'
        elif int(ans) == 2 :
            player_stats['name'] = 'Dragon'
            player_stats['strength'] = 5
            player_stats['speed'] = 1
            player_stats['health'] = 60
            player_stats['defense'] = 4
            player_stats['dexterity'] = 2
            player_stats['mana'] = 5
            player_stats['magic_discription'] = '(breathe fire 1-20 damage)'
            player_stats['p_attack'] = '(breathe gold fire - auto pierce)'
        if int(ans) == 3 :
            player_stats['name'] = 'Goblin'
            player_stats['strength'] = 2
            player_stats['speed'] = 3
            player_stats['health'] = 50
            player_stats['defense'] = 0
            player_stats['dexterity'] = 3
            player_stats['mana'] = 3
            player_stats['magic_discription'] = '(gain 4 dex)'
            player_stats['p_attack'] = '(auto crit)'
        elif int(ans) == 4 :
            player_stats['name'] = 'Troll'
            player_stats['strength'] = 4
            player_stats['speed'] = -1
            player_stats['health'] = 60
            player_stats['defense'] = 2
            player_stats['dexterity'] = -1
            player_stats['mana'] = 3
            player_stats['magic_discription'] = '(deal 1-10 damage, heal the difference)'
            player_stats['p_attack'] = '(If less than  10 HP, heal all damage)'
        elif int(ans) == 5 :
            player_stats['name'] = 'Orc'
            player_stats['strength'] = 5
            player_stats['speed'] = 2
            player_stats['health'] = 48
            player_stats['defense'] = 2
            player_stats['dexterity'] = 2
            player_stats['mana'] = 2
            player_stats['magic_discription'] = '(Deal 18 damage)'
            player_stats['p_attack'] = '(+1 to each stat)'
        elif int(ans) == 6 :
            player_stats['name'] = 'Wyvern'
            player_stats['strength'] = 3
            player_stats['speed'] = 2
            player_stats['health'] = 40
            player_stats['defense'] = 1
            player_stats['dexterity'] = 4
            player_stats['mana'] = 6
            player_stats['magic_discription'] = '(fly in air, longer stay, more damage 20+5x)'
            player_stats['p_attack'] = '(Heal all damage)'
        if double == True and FirstSelected == False :
            FirstSelected = True
            choose_fighter(player_stats)
   #goes in choose_fighter         #name,strength,speed,health,defense,dexterity,mana,magic_discription,p_attack
def choose_fighter(player_stats) :
    global lose
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
        choose_fighter(player_stats)
    else :
        if int(ans) == 1:
            player_stats['name'] = 'Swordmaster'
            player_stats['strength'] = 2
            player_stats['speed'] = 7
            player_stats['health'] = 40
            player_stats['defense'] = 1
            player_stats['dexterity'] = 3
            player_stats['mana'] = 2
            player_stats['magic_discription'] = '(strength*6)'
            player_stats['p_attack'] = '(damage taken last turn + 5)'
        elif int(ans) == 2:
            player_stats['name'] = 'Knight'
            player_stats['strength'] = 3
            player_stats['speed'] = -1
            player_stats['health'] = 35
            player_stats['defense'] = 6
            player_stats['dexterity'] = -1
            player_stats['mana'] = 3
            player_stats['magic_discription'] = '(copy opponent 5 less)'
            player_stats['p_attack'] = '(+3 defense and 5-12 damage)'
        elif int(ans) == 3:
            player_stats['name'] = 'Wizard'
            player_stats['strength'] = 6
            player_stats['speed'] = 2
            player_stats['health'] = 35
            player_stats['defense'] = 0
            player_stats['dexterity'] = 3
            player_stats['mana'] = 19
            player_stats['magic_discription'] = '(1 damage per mana used)'
            player_stats['p_attack'] = '(auto crit)'
        elif int(ans) == 4:
            player_stats['name'] = 'Prince'
            player_stats['strength'] = random.randint(1,9)
            player_stats['speed'] = random.randint(1,8)
            player_stats['health'] = random.randint(30,42)
            player_stats['defense'] = random.randint(1,6)
            player_stats['dexterity'] = random.randint(0,5)
            player_stats['mana'] = random.randint(1,3)
            player_stats['magic_discription'] = '(18 + strength)'
            player_stats['p_attack'] = '(change defense, strength and +5 health)'
            print('str: ' + str(player_stats[strength]) + '  spd: ' + str(player_stats[speed]) + '  HP: ' + str(player_stats[health]) + '  defense: ' + str(player_stats[defense]) + '  dexterity: ' + str(player_stats[dexterity]))
        elif int(ans) == 5:
            player_stats['name'] = 'Princess'
            player_stats['strength'] = -4
            player_stats['speed'] =  5
            player_stats['health'] = 70
            player_stats['defense'] = 2
            player_stats['dexterity'] = 1
            player_stats['mana'] = 1
            player_stats['magic_discription'] = '(20 + strength)'
            player_stats['p_attack'] = '(heal 25 damage)'
        elif int(ans) == 6:
            player_stats['name'] = 'Archer'
            player_stats['strength'] = 2
            player_stats['speed'] = 4
            player_stats['health'] = 25
            player_stats['defense'] = 1
            player_stats['dexterity'] = 10
            player_stats['mana'] = 3
            player_stats['magic_discription'] = '(shot 1-5 arrows 5 each)'
            player_stats['p_attack'] = '(reset battle)'
        elif int(ans) == 7 :
            player_stats['name'] = 'Berserker'
            player_stats['strength'] = 2
            player_stats['speed'] = 1
            player_stats['health'] = 50
            player_stats['defense'] = 0
            player_stats['dexterity'] = 0
            player_stats['mana'] = 4
            player_stats['magic_discription'] = '(save from death once)'
            player_stats['p_attack'] = '(Change health to strength 1:2)'
        elif int(ans) == 8 :
            player_stats['name'] = 'Zombie'
            player_stats['strength'] = 3
            player_stats['speed'] = 5
            player_stats['health'] = 35
            player_stats['defense'] = 0
            player_stats['dexterity'] = 4
            player_stats['mana'] = 3
            player_stats['magic_discription'] = '(life drain)'
            player_stats['p_attack'] = '(change HP to 1)'
        elif int(ans) == 9 :
            player_stats['name'] = 'Overlord'
            player_stats['strength'] = 0
            player_stats['speed'] = 0
            player_stats['health'] = 0
            player_stats['defense'] = 0
            player_stats['dexterity'] = 0
            player_stats['mana'] = 6
            player_stats['magic_discription'] = '(grows by 5 every time)'
            player_stats['p_attack'] = '(gain two turns of invincibility)'
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
            else :
                if int(ans) <= ol_points and int(ans) >= -5 and int(ans) <= ol_points:
                    player_stats['strength'] = ans
                    ol_points = int(ol_points) - int(ans)
                else :
                    print('You cannot use that amount')
                    time.sleep(0.75)
                    print('You will get 0 str')
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
            else :
                if int(ans) <= ol_points and int(ans) >= -1 and int(ans) <= ol_points:
                    player_stats['speed'] = ans
                    ol_points = int(ol_points) - int(ans)
                else :
                    print('You cannot use that amount')
                    time.sleep(0.75)
                    print('You will get 0 spd')
            time.sleep(0.75)
            print('OL: ' + str(ol_points))
            print('Choose defense; -5,' + str(ol_points))
            ans = input()
            try :
                int(ans)
            except :
                print('That is not a number.')
                time.sleep(0.75)
                print('You will get 0 def')
            else :
                if int(ans) <= ol_points and int(ans) >= -5 and int(ans) <= ol_points:
                    player_stats['defense'] = ans
                    ol_points = int(ol_points) - int(ans)
                else :
                    print('You cannot use that amount')
                    time.sleep(0.75)
                    print('You will get 0 def')
            print('OL: ' + str(ol_points))
            print('Choose dexterity; -5,10')
            ans = input()
            try :
                int(ans)
            except :
                print('That is not a number.')
                time.sleep(0.75)
                print('You will get 0 dex')
            else :
                if int(ans) <= ol_points and int(ans) >= -5 and int(ans) <= 10:
                    player_stats['dexterity'] = ans
                    ol_points = int(ol_points) - int(ans)
                else :
                    print('You cannot use that amount')
                    time.sleep(0.75)
                    print('You will get 0 dex')
            player_stats['health'] = ol_points*5
            if player_stats['health'] <= 0 :
                print('You died by lack of health')
                time.sleep(0.75)
                lose = lose +1
                print('Do you want to play again?   Wins: ' + str(win) + '  Loses: ' + str(lose))
                ans = input()
                if ans == 'yes' or 'y' :
                    start_game()
                else :
                    end_game()
            print('HP: ' + str(player_stats['health']))
        elif int(ans) == 10:
            player_stats['name'] = 'Santa'
            player_stats['strength'] = 44
            player_stats['speed'] = 18
            player_stats['health'] = 1
            player_stats['defense'] = 0
            player_stats['dexterity'] = 0
            player_stats['mana'] = 1
            player_stats['magic_discription'] = '(santa time)'
            player_stats['p_attack'] = '(-1000-1000 damage)'
            global santa_time
            santa_time = santa_time +1
        elif int(ans) == 0:
            gladiator_fighters()
        elif int(ans) == random.randint(11,20):
            player_stats['name'] = 'King'
            player_stats['strength'] = 100
            player_stats['speed'] = 100
            player_stats['health'] = 100
            player_stats['defense'] = 100
            player_stats['dexterity'] = 100
            player_stats['mana'] = 0
            player_stats['magic_discription'] = '(nothing)'
            player_stats['p_attack'] = '(2 damage + strength)'
            print('You chose the correct number. You will be the King')
        elif int(ans) == 99:
            player_stats['name'] = 'Test'
            player_stats['magic_discription'] = '(nothing)'
            player_stats['p_attack'] = '(2 damage + strength)'
            print('How much strength do you want?')
            player_stats['strength'] = int(input())
            print('How much speed do you want?')
            player_stats['speed'] = int(input())
            print('How much health do you want?')
            player_stats['health'] = int(input())
            print('How much defense do you want?')
            player_stats['defense'] = int(input())
            print('How much dexerity do you want?')
            player_stats['dexterity'] = int(input())
            print('How much mana do you want?')
            player_stats['mana'] = int(input())
        else:
            player_stats['name'] = 'Footsoldier'
            player_stats['strength'] = -1
            player_stats['speed'] = -1
            player_stats['health'] = 25
            player_stats['defense'] = 0
            player_stats['dexterity'] = 1
            player_stats['mana'] = 3
            player_stats['magic_discription'] = '(???)'
            player_stats['p_attack'] = '(heal 10 damage, deal 1-20 damage)'
            print('That is not an option, you will be a footsoldier')
        if journey == 1 :
            player_stats['max_health'] = player_stats['health']
            next_battle()
        if double == True and FirstSelected == False :
            FirstSelected = True
            choose_fighter(player_stats)

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
    if player_stats['health'] <= 0 :
        if name == 'Zombie' :
            DetermineTurn()
        elif focus >= 1 :
            print('You clung on to life')
            player_stats['health'] = 1
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
    global f, monster, mon_health
    time.sleep(0.75)
    print('You will battle a ' + str(monster))
    first = int(random.randint(1,20)) + int(player_stats['speed']) - int(random.randint(1,20))
    if double :
        pass
    if crazy == 1 :
        f = 0
        time.sleep(0.75)
        print('The ' + str(monster) + ' is going first')
        crazy_mon_miss()
        time.sleep(0.75)
        print(str(player_stats['name']) + ' HP: ' + str(player_stats['health']))
        print(str(monster) + ' HP: ' + str(mon_health))
        if player_stats['health'] <= 0 :
            if player_stats['name'] == 'Zombie' :
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
        print(str(player_stats['name']) + ' HP: ' + str(player_stats['health']))
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
        print(str(player_stats['name']) + ' HP: ' + str(player_stats['health']))
        print(str(monster) + ' HP: ' + str(mon_health))
        if int(shields) >= 1 :
            print('shield HP: ' + str(shields))
        if player_stats['health'] <= 0 :
            if player_stats['name'] == 'Zombie' :
                update()
            else :
                die()

def crazy_mon_miss() :
    global damage, arc, shield, temp_health, mon_damage, shields, invinc, mon_strength, b_mode, br_shield, mon_health
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
                damage = player_stats['health'] - 1
                player_stats['health'] = 1
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
        elif int(arc) == 2 :
            time.sleep(0.75)
            print('The ' + str(monster) + ' missed.')
        elif int(arc) == 1 :
            mon_damage = int(random.randint(1,20)) 
            damage_s = int(mon_damage) - int(player_stats['defense']) - int(shield) + int(mon_strength)
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
                temp_health = player_stats['health']
                player_stats['health'] = int(temp_health) - int(damage) 
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
                damage_s = int(mon_damage) - int(player_stats['defense']) - int(shield) + int(mon_strength)
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
                    temp_health = player_stats['health']
                    player_stats['health'] = int(temp_health) - int(damage)
                    if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                        time.sleep(0.75)
                        print('Your shield broke')
                        shields = 0
                        br_shield = 0
                        time.sleep(0.75)
                        print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                        BerserkerRage()
                    else :
                        time.sleep(0.75)
                        print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                        shields = 0
                        BerserkerRage()
    if ability_add :
        CheckAbility('MonsterTurn', mon_damage)

                
def ready_check_win() :
    global alive, done
    if mon_health <= 0:
        alive = False
        print('A')
    elif player_stats['health'] <= 0 :
        if player_stats['name'] == 'Zombie' :
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
    elif player_stats['health'] <= 0 :
        if player_stats['name'] == 'Zombie' :
            update()
        elif focus >= 1 :
            print('You clung on to life')
            player_stats['health'] = 1
            print(str(player_stats['name']) + ' HP: ' + str(player_stats['health']))
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
        hit = int(random.randint(1,20)) + int(player_stats['dexterity']) - int(mon_dext)
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
        elif damage - int(player_stats['strength']) <= 1 :
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
    global damage, mon_health
    if damage <= 0 :
        time.sleep(0.75)
        print('You failed to reach the ' + str(monster))
    elif damage - int(player_stats['strength']) <= 1 :
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
            damage = int(random.randint(1,4)) + int(player_stats['strength'])
            time.sleep(0.75)
            print('You attacked yourself. (' + str(damage) + ' damage)')
            player_stats['health'] = player_stats['health'] - damage
        elif int(action) == 5 :
            damage = int(random.randint(1,10))
            time.sleep(0.75)
            print('You got ran over by a boulder. (' + str(damage) + ' damage)')
            player_stats['health'] = player_stats['health'] - damage
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
            mon_damage = int(fire) + int(mon_strength) + int(player_stats['defense'])
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
        dodge = random.randint(1,20) + int(player_stats['dexterity'])
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
        if move == 2 or player_stats['health'] == 20 + int(mon_strength)*2 - int(player_stats['defense'])*2 or player_stats['health'] <= 10 + int(mon_strength) - int(player_stats['defense']) :
            m_sure()
        else :
            m_basic()
    else :
        move = random.randint(1,5)
        if move == 1 or player_stats['health'] == 20 + int(mon_strength)*2 - int(player_stats['defense'])*2  or player_stats['health'] <= 10 + int(mon_strength) - int(player_stats['defense']) :
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
    global damage, arc, shield, temp_health, mon_damage, shields, invinc, mon_strength, b_mode, br_shield, crit, mon_dext
    hit = int(random.randint(1,20)) - int(player_stats['dexterity']) + int(mon_dext)
    crit = int(random.randint(1,5))
    if crit == 5 :
        crit = 2
    if ai == False :
        mon_damage = int(random.randint(1,20))
    damage_s = int(mon_damage) - int(player_stats['defense']) - int(shield) + int(mon_strength)
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
        temp_health = player_stats['health']
        if crit != 2 :
            player_stats['health'] = int(temp_health) - int(damage)
            if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                time.sleep(0.75)
                print('Your shield broke')
                shields = 0
                br_shield = 0
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                BerserkerRage()
            else :
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                shields = 0
                BerserkerRage()
        else :
            time.sleep(0.75)
            print('The ' + str(monster) + ' got a critical hit')
            player_stats['health'] = int(temp_health) - int(damage)*crit
            if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                time.sleep(0.75)
                print('Your shield broke')
                shields = 0
                br_shield = 0
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage*crit) + ' damage')
                BerserkerRage()
            else :
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage*crit) + ' damage')
                shields = 0
                BerserkerRage()
    if ability_add :
        CheckAbility('MonsterTurn', mon_damage)  

def BerserkerRage() :
    global b_mode, mon_strength
    if player_stats['name'] == 'Berserker' and player_stats['health'] <= player_stats['max_health']/2 and int(b_mode) == 0 :
        print('You entered berserk mode; +10 str -8 def')
        player_stats['strength'] = player_stats['strength'] + 10
        mon_strength = mon_strength + 8
        b_mode = 1        

def ready_attack() :
    global damage, shield, temp_health, mon_damage, shields, invinc, mon_strength, b_mode, br_shield, crit
    time.sleep(0.75)
    print('You are readying your attack')
    hit = int(random.randint(1,20)) - int(player_stats['dexterity']) + int(mon_dext)
    crit = int(random.randint(1,5))
    if crit == 5 :
        crit = 2
    mon_damage = int(random.randint(1,20))
    damage_s = int(mon_damage) - int(player_stats['defense']) - int(shield) + int(mon_strength)
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
        temp_health = player_stats['health']
        if crit != 2 :
            player_stats['health'] = int(temp_health) - int(damage)
            if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                time.sleep(0.75)
                print('Your shield broke')
                shields = 0
                br_shield = 0
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                BerserkerRage()
            else :
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage) + ' damage')
                shields = 0
                BerserkerRage()
        else :
            time.sleep(0.75)
            print('The ' + str(monster) + ' got a critical hit')
            player_stats['health'] = int(temp_health) - int(damage)*crit
            if int(shields) + int(damage_s) >= 1  and br_shield == 1 :
                time.sleep(0.75)
                print('Your shield broke')
                shields = 0
                br_shield = 0
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage*crit) + ' damage')
                BerserkerRage()
            else :
                time.sleep(0.75)
                print('The ' + str(monster) + ' dealt ' + str(damage*crit) + ' damage')
                shields = 0
                BerserkerRage()

        if player_stats['health'] >= 1 :
            time.sleep(0.75)
            print(str(player_stats['name']) + ' HP: ' + str(player_stats['health']))
            print(str(monster) + ' HP: ' + str(mon_health))
            if int(shields) >= 1 :
                print('shield HP: ' + str(shields))
            if mon_health <= 0:
                beat_mon()
            elif player_stats['health'] <= 0 :
                if player_stats['name'] == 'Zombie' :
                    update()
                else :
                    die()

def move_1() :
    global damage
    if player_stats['name']  == 'Swordmaster' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Knight' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Wizard' :
        damage = int(random.randint(-1,22)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Prince' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Princess' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Archer' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Berserker' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Zombie' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Overlord' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Gladiator' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Dragon' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Goblin' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Troll' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Orc' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Wyvern' :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    elif player_stats['name']  == 'Santa' :
        damage = int(random.randint(1,10)) + int(player_stats['strength'])
    elif player_stats['name']  == 'King' :
        damage = 2 + int(player_stats['strength'])                  
    elif player_stats['name']  == 'Test' :
        damage = 2 + int(player_stats['strength'])      
    else :
        damage = int(random.randint(1,20)) + int(player_stats['strength'])
    check_for_crazy_miss()       
            
def move_2() :
    global damage, defense, arc, health, shield, temp_health, mon_damage, invinc, shields, br_shield, crit, done
    done = False
    while alive == True and done == False :
        if player_stats['name']  == 'Swordmaster' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Knight' :
            player_stats['defense'] = player_stats['defense'] + 2
            ready_attack()
            damage = int(random.randint(15,26)) + int(player_stats['strength'])
            ready_check_win()
            player_stats['defense'] = player_stats['defense'] - 2
        elif player_stats['name']  == 'Wizard' :
            ready_attack()
            damage = int(random.randint(12,40)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Prince' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Princess' :
            ready_attack()
            damage = int(random.randint(15,28)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Archer' :
            time.sleep(0.75)
            print('You are readying your attack')
            hit = int(random.randint(1,20)) - player_stats['dexterity'] + mon_dext
            crit = int(random.randint(1,5))
            if crit == 5 :
                crit = 2
            temp_health = player_stats['health']
            if crit != 2 :
                player_stats['health'] = int(temp_health) - int(damage)
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
                player_stats['health'] = int(temp_health) - int(damage)*crit
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
            print(str(player_stats['name'] ) + ' HP: ' + str(player_stats['health']))
            print(str(monster) + ' HP: ' + str(mon_health))
            if int(shields) >= 1 :
                print('shield HP: ' + str(shields))
            damage = int(random.randint(5,25)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Berserker' :
            ready_attack()
            damage = int(random.randint(28,35)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Zombie' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Overlord' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Gladiator' :
            ready_attack()
            damage = int(random.randint(25,35)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Dragon' :
            ready_attack()
            damage = int(random.randint(18,32)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Goblin' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Troll' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Orc' :
            ready_attack()
            damage = int(random.randint(20,30)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Wyvern' :
            ready_attack()
            damage = int(random.randint(10,40)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'Santa' :
            ready_attack()
            damage = int(random.randint(100,200)) + int(player_stats['strength'])
            ready_check_win()
        elif player_stats['name']  == 'King' :
            ready_attack()
            damage = 2 + int(player_stats['strength'])           
            ready_check_win()
        elif player_stats['name']  == 'Test' :
            ready_attack()
            damage = 2 + int(player_stats['strength'])
            ready_check_win()
        else :
            ready_attack()
            damage = int(random.randint(20,30)) + int(player_stats['strength'])
            ready_check_win()
            
def move_3() :
    global damage, power_move, shields, mon_strength, b_mode, mon_health
    if power_move == 0 :
        power_move = 1
        if player_stats['name']  == 'Swordmaster' :
            if damage == 0 :
                damage = 15
            if crit == 2 :
                damage = int(damage)*2 + 3 + int(player_stats['strength'])    
            else :
                damage = int(damage) + 3 + int(player_stats['strength'])
            check_for_crazy_miss()
        elif player_stats['name']  == 'Knight' :
            damage = int(random.randint(2,7)) + int(player_stats['strength'])
            player_stats['defense'] = player_stats['defense'] + 3
            check_for_crazy_miss()
        elif player_stats['name']  == 'Wizard' :
            damage = int(random.randint(1,20)) + int(player_stats['strength'])*2
            time.sleep(0.75)
            print('You got a critical hit')
            temp_mon_health = mon_health
            mon_health = int(temp_mon_health) - int(damage)*2
            time.sleep(0.75)
            print('You dealt ' + str(damage*2) + ' damage')
        elif player_stats['name']  == 'Prince' :
            player_stats['strength'] = random.randint(2,10)
            player_stats['health'] = player_stats['health'] + 5
            player_stats['defense'] = random.randint(2,7)
            print('str: ' + str(player_stats['strength']) + '  HP: ' + str(player_stats['health']) + '  defense: ' + str(player_stats['defense']))
            damage = int(random.randint(1,20)) + int(player_stats['strength'])
            check_for_crazy_miss()
        elif player_stats['name']  == 'Princess' :
            player_stats['health'] = player_stats['health'] + 25
            print('You healed 25 damage')
        elif player_stats['name']  == 'Archer' :
            player_stats['health'] = 25
            mon_health = 30 + int(mon_strength)*2
        elif player_stats['name']  == 'Berserker' :
            print('How much health do you want to convert(round down)')
            ans = input()
            try :
                int(ans)
            except :
                print('That is not a number.')
                time.sleep(0.75)
                move_3()
            else :
                player_stats['strength'] = player_stats['strength'] + int(ans)*2
                player_stats['health'] = player_stats['health'] - int(ans)
        elif player_stats['name']  == 'Zombie' :
            player_stats['health'] = 1
        elif player_stats['name']  == 'Overlord' :
            global invinc
            invinc = 1
            time.sleep(0.75)
            print('You gained two turns of invincibility')
            time.sleep(0.75)
            print('The ' + str(monster) + ' failed to hurt you')
            choose_move()
        elif player_stats['name']  == 'Gladiator' :
            damage = int(random.randint(20,30)) + int(player_stats['strength'])
            check_for_crazy_miss()
        elif player_stats['name']  == 'Dragon' :
            print('You breathed gold fire.')
            fire = random.randint(15,20)
            damage = int(fire) + int(player_stats['strength']) + int(player_stats['defense'])
            check_for_crazy_miss()
        elif player_stats['name']  == 'Troll' :
            if player_stats['health'] < 11 :
                player_stats['health'] = 60
                print('Healed all damage')
            else :
                print('*grunted')
        elif player_stats['name']  == 'Orc' :
            player_stats['strength'] += 1
            player_stats['health'] += 5
            player_stats['dexterity'] += 1
            player_stats['defense'] += 1
        elif player_stats['name']  == 'Wyvern' :
            player_stats['health'] = 40
        elif player_stats['name']  == 'Goblin' :
            damage = int(random.randint(1,20)) + int(player_stats['strength'])*2
            time.sleep(0.75)
            print('You got a critical hit')
            temp_mon_health = mon_health
            mon_health = int(temp_mon_health) - int(damage)*2
            time.sleep(0.75)
            print('You dealt ' + str(damage*2) + ' damage')
        elif player_stats['name']  == 'Santa' :
            time.sleep(0.75)
            print('Bomb')
            damage = int(random.randint(-1000,1000)) + int(player_stats['strength'])
            check_for_crazy_miss()
        elif player_stats['name']  == 'King' :
            damage = 2 + int(player_stats['strength'])           
            check_for_crazy_miss()
        elif player_stats['name']  == 'Test' :
            damage = 2 + int(player_stats['strength'])
            check_for_crazy_miss()
        else :
            player_stats['health'] = player_stats['health'] + 10
            print('You healed 10 damage')
            damage = int(random.randint(1,20)) + int(player_stats['strength'])
            check_for_crazy_miss()
    else :
        time.sleep(0.75)
        print('You have already used your power move.')
        choose_move()

def move_magic():        
    global fly,focus, damage, mana, ol_charge, mon_strength, mon_health
    if mana > 0 :
        mana = mana - 1
        if player_stats['name']  == 'Swordmaster' :
            damage = player_stats['strength']*6
            check_for_crazy_miss()
        elif player_stats['name']  == 'Knight' :
            if damage == 0 :
                damage = 15 
            if crit == 2 :
                damage = int(damage)*2 - 10   
            else :
                damage = int(damage) - 5
            check_for_crazy_miss()
        elif player_stats['name']  == 'Wizard' :
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
                    damage = int(ans) + int(player_stats['strength'])
                    check_for_crazy_miss()
                else :
                    time.sleep(0.75)
                    print('You do not have that amount')
                    choose_move()           
        elif player_stats['name'] == 'Prince' :
            damage = 18 + int(player_stats['strength'])
            check_for_crazy_miss()
        elif player_stats['name']  == 'Princess' :
            damage = 20 + int(player_stats['strength'])
            check_for_crazy_miss()
        elif player_stats['name']  == 'Archer' : 
            arrows = random.randint(1,5)
            time.sleep(0.75)
            print('You fired ' + str(arrows) + ' arrows')
            damage = arrows*5 + int(player_stats['strength'])
            check_for_crazy_miss()
        elif player_stats['name']  == 'Berserker' :
            focus = focus + 1
            time.sleep(0.75)
            print('You fortified yourself')
        elif player_stats['name']  == 'Zombie' :
            damage = random.randint(2,10)
            heal = damage/2
            player_stats['health'] = player_stats['health'] + heal
            check_for_crazy_miss()
            time.sleep(0.75)
            print('You drained ' + str(damage) + ' life and healed ' + str(heal) + ' damage')
        elif player_stats['name']  == 'Overlord' :
            ol_charge = ol_charge + 5
            damage = 5 + ol_charge + int(player_stats['strength'])
            check_for_crazy_miss()
        elif player_stats['name']  == 'Gladiator' :
            mon_strength -= 1
            mon_health -= 5
            mon_dex -= 1
        elif player_stats['name']  == 'Dragon' :
            fire = random.randint(1,20)
            time.sleep(0.75)
            if int(fire) < 8 :
                print('You breathed red fire.')
                damage = int(fire) + int(player_stats['strength'])
            elif int(fire) > 7 and int(fire) < 15 :
                print('You breathed black fire.')
                damage = random.randint(1,35) 
            elif int(fire) > 14 and int(fire) < 19 :
                print('You breathed blue fire.')
                damage = int(fire) + int(player_stats['strength'])
            else :
                print('You breathed gold fire.')
                damage = int(fire) + int(player_stats['strength']) + int(player_stats['defense'])
            check_for_crazy_miss()
        elif player_stats['name']  == 'Goblin' :
            player_stats['dexterity'] += 4
        elif player_stats['name']  == 'Troll' :
            damage = random.randint(1,10)
            player_stats['health'] = player_stats['health'] + (11 - damage)
            check_for_crazy_miss()
        elif player_stats['name']  == 'Orc' :
            damage = 13 + int(player_stats['strength'])
            check_for_crazy_miss()
        elif player_stats['name']  == 'Wyvern' :
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
        elif player_stats['name']  == 'Santa' :
            time.sleep(0.75)
            print('Santa does not have magic')
        elif player_stats['name']  == 'King' :
            player_stats['health'] = player_stats['health'] + 100
            time.sleep(0.75)
            print('The King healed 100 damage')
        elif player_stats['name']  == 'Test' :
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
    global damage, shield
    if player_stats['name']  == 'Swordmaster' :
        shield = int(random.randint(3,8))
        heal = int(random.randint(3,8))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Knight' :
        shield = int(random.randint(4,9))
        heal = int(random.randint(3,6))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Wizard' :
        shield = int(random.randint(1,11))
        heal = int(random.randint(1,10))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Prince' :
        shield = int(random.randint(4,13))
        heal = int(random.randint(3,7))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Princess' :
        shield = int(random.randint(2,7))
        heal = int(random.randint(5,13))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Archer' :
        shield = int(random.randint(5,13))
        heal = int(random.randint(2,4))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Berserker' :
        shield = int(random.randint(3,9))
        heal = int(random.randint(2,8))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Zombie' :
        shield = int(random.randint(1,4))
        heal = int(random.randint(8,15))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Overlord' :
        shield = int(random.randint(2,9))
        heal = int(random.randint(3,5))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Gladiator' :
        shield = int(random.randint(3,8))
        heal = int(random.randint(3,8))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Dragon' :
        shield = int(random.randint(5,10))
        heal = int(random.randint(6,10))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Goblin' :
        shield = int(random.randint(2,7))
        heal = int(random.randint(5,7))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Troll' :
        shield = int(random.randint(4,9))
        heal = int(random.randint(2,6))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Orc' :
        shield = int(random.randint(3,8))
        heal = int(random.randint(3,8))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Wyvern' :
        shield = int(random.randint(2,8))
        heal = int(random.randint(4,9))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')
    elif player_stats['name']  == 'Santa' :
        shield = 0
        time.sleep(0.75)
        print('Santa cannot defend himself')
    elif player_stats['name']  == 'King' :
        shield = 100
        heal = 100
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')      
    elif player_stats['name']  == 'Test' :
        print('What shield do you want?')
        shield = input()
        heal = int(random.randint(3,10))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')        
    else :
        shield = int(random.randint(3,8))
        heal = int(random.randint(3,10))
        player_stats['health'] = player_stats['health'] + heal
        time.sleep(0.75)
        print('You defended yourself with ' + str(shield) + ' shield and healed ' + str(heal) + ' damage')

def turn_back_time() :
    if int(player_stats['health']) >= 0 :
        print('You mysteriously came back to life')
    else :
        print('Miraculously, time started going backward')
    player_stats['health'] = temp_health
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
            pass
        elif int(use_move) == 7 :
            print('1 = normal attack 2 = charge attack 3 = magic move (mana: ' + str(player_stats['mana']) + ') ' + str(player_stats['magic_discription']) + ' 4 = power attack ' + str(p_attack) + ' 5 = defend 6 = use item')
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
    print(str(player_stats['name'] ) + ' HP: ' + str(player_stats['health']))
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
        elif player_stats['health'] >= 1 and mon_health >= 1:
            if f == 1:
                monster_attacks()
                time.sleep(0.75)
                print_health()
                if player_stats['health'] >= 1 or player_stats['name']  == 'Zombie' :
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



player_stats = {'name':'none','strength':0,'speed':0,'health':0,'max_health':0,'defense':0,'dexterity':0,'mana':0,'magic':'none','p_attack':'none'}

def start_game() :
    choose_mode()
    choose_fighter(player_stats)
    first_turn()
    update()
        
   #if int(two_p) == 1 :
        #first_turn_2()    

start_game()
