import random
'''
shots = 0
player = 0
bullets = ['0','0','1','0','0']
players = ['']
print('The one who catches a bullet - dies')
players_count = int(input('How many players will play:'))
for i in range(players_count):
    players.append(input('Write the name of the player №' + str(i + 1)))
    if player > players_count - 1:
        player = 0
    print("Shoots " + players[player])
    print("Press enter to shoot")
    input()
    shot = random.choice(bullets)
    bullets.remove(shot)
    if shot == 1:
        print("Boom!You dead!")
        break 
    else:
        print("Clack...Lucky...")	
        print("Passing on to the next player.")
    player += 1
    shots += 1
'''
shots=0
bullets=[0,0,0,0,0,1]
player = 0
print("Правила: Это игра, в которой два оппонента решают спор при помощи револьвера, который заряжен только одним патроном. Каждый участник игры стреляет по очереди. Побеждает тот, кто выживет.")
players = []
player_count = int(input("Количество игроков"))
while player_count > 3:
    player_count = int(input("Количество игроков"))
for i in range(player_count):
    players.append(input("Имя игрова № "+str(i+1)))
while shots < 6:
    if player > player_count - 1:
        player = 0
    print('Стреляет '+players[player])
    print('Enter')
    input()
    
    shot=random.choice(bullets)
    if shot == 1:
        print("Ты убит!")
        break
    else:
        print("Можно стрелять, ход переходит второму игроку")
    player += 1
    shots += 1

