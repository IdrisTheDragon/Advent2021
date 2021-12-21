from collections import defaultdict

# input 
Player_1 = 7
Player_2 = 5

# example
# Player_1 = 4
# Player_2 = 8

p1 = 0
p2 = 0

rollcount = 0

while True:
    p1_roll = rollcount+1 + rollcount+2 + rollcount+3
    rollcount+=3

    Player_1 = Player_1 + p1_roll
    while Player_1 > 10:
        Player_1 -= 10
    p1+=Player_1
    print("p1",Player_1,p1)
    if p1 >= 1000:
        print(p2,rollcount,p2*rollcount)
        break
    p2_roll = rollcount+1 + rollcount+2 + rollcount+3
    rollcount+=3

    Player_2 = Player_2 + p2_roll
    while Player_2 > 10:
        Player_2 -= 10
    p2+=Player_2
    print("p2",Player_2,p2)
    if p2 >= 1000:
        print(p1,rollcount,p1*rollcount)
        break


# input 
Player_1 = 7
Player_2 = 5

# example
# Player_1 = 4
# Player_2 = 8

p1 = 0
p2 = 0

universes = dict()
universes[(Player_1,Player_2,p1,p2)] = 1
wins = [0,0]
ROLLS = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}


while len(universes) > 0:
    new_universes = defaultdict(int)
    # p1
    for universe, count in universes.items():
        (Player_1,Player_2,p1,p2) = universe
        for R,c in ROLLS.items():
            newPlayer_1 = Player_1 + R
            while newPlayer_1 > 10:
                newPlayer_1 -= 10
            newp1 = p1 + newPlayer_1
            if newp1 >= 21:
                wins[0] += count * c
            else:
                new_universes[(newPlayer_1,Player_2,newp1,p2)] += count * c

    universes = new_universes
    new_universes = defaultdict(int)

    for universe, count in universes.items():
        (Player_1,Player_2,p1,p2) = universe
        for R,c in ROLLS.items():
            newPlayer_2 = Player_2 + R
            while newPlayer_2 > 10:
                newPlayer_2 -= 10
            newp2 = p2 + newPlayer_2
            if newp2 >= 21:
                wins[1] += count * c
            else:
                new_universes[(Player_1,newPlayer_2,p1,newp2)] += count * c
    universes = new_universes

print(wins)

